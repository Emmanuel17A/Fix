from __future__ import annotations

from fix.core.plugin import FixPlugin, PluginMetadata
from .adapter import RemoveWatermarkAdapter


class RemoveWatermarkPlugin(FixPlugin):
    metadata = PluginMetadata(
        plugin_id="remove_watermark",
        name="Remove Watermark",
        version="1.0.0",
        description="Remove selected watermark regions using FFmpeg delogo.",
    )

    def create_adapter(self) -> RemoveWatermarkAdapter:
        return RemoveWatermarkAdapter()
