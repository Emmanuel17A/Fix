from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from fix.core.models import MediaInfo, OperationContext
from fix.plugins.trim.adapter import TrimAdapter


def media_info(source: Path, duration: float = 10.0) -> MediaInfo:
    return MediaInfo(
        path=source,
        duration=duration,
        width=1280,
        height=720,
        fps=30.0,
        video_codec="h264",
        video_bitrate=1_000_000,
        size_bytes=1000,
    )


def test_valid_trim_range_builds_new_output_plan(tmp_path):
    source = tmp_path / "source.mp4"
    source.write_bytes(b"source")
    output = tmp_path / "trimmed.mp4"
    context = OperationContext(
        source=source,
        media=media_info(source),
        output=output,
        start_seconds=2.5,
        end_seconds=7.25,
    )

    plan = TrimAdapter().build_plan(context)

    assert plan.output == output
    assert plan.replace_source is False


def test_trim_end_exceeding_duration_is_silently_clamped(tmp_path, monkeypatch):
    """End times beyond the video duration are silently clamped."""
    source = tmp_path / "source.mp4"
    source.write_bytes(b"source")
    output = tmp_path / "trimmed.mp4"
    calls = {}

    def fake_trim_video(**kwargs):
        calls.update(kwargs)
        kwargs["output"].write_bytes(b"trimmed")
        return kwargs["output"]

    monkeypatch.setattr(
        "fix.plugins.trim.adapter.trim_video",
        fake_trim_video,
    )
    monkeypatch.setattr(
        "fix.plugins.trim.adapter.validate_output",
        lambda path: None,
    )

    plan = TrimAdapter().build_plan(OperationContext(
        source=source,
        media=media_info(source, duration=10.0),
        output=output,
        start_seconds=8.0,
        end_seconds=15.0,
    ))
    plan.runner(lambda fraction, label: None)

    assert calls["start_seconds"] == 8.0
    assert calls["end_seconds"] == 10.0
