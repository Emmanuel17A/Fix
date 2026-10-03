from __future__ import annotations

from pathlib import Path

from fix.core.errors import MediaProcessingError
from .ffprobe import probe_media


def validate_output(path: Path) -> None:
    if not path.exists():
        raise MediaProcessingError("Expected output file was not created.")
    if path.stat().st_size <= 0:
        raise MediaProcessingError("Output file is empty.")
    info = probe_media(path)
    if info.width <= 0 or info.height <= 0:
        raise MediaProcessingError("Output does not contain a readable video stream.")
