from __future__ import annotations

from fix.core.plugin import FixPlugin, PluginMetadata
from .adapter import WatermarkOverlayAdapter


class WatermarkOverlayPlugin(FixPlugin):
    metadata = PluginMetadata(
        plugin_id="watermark_overlay",
        name="Add / Replace Watermark",
        version="1.0.0",
        description="Overlay a watermark for a selected duration without deleting existing pixels.",
    )

    def create_adapter(self) -> WatermarkOverlayAdapter:
        return WatermarkOverlayAdapter()
