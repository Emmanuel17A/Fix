from __future__ import annotations

from fix.core.registry import PluginRegistry
from .remove_watermark.plugin import RemoveWatermarkPlugin
from .watermark_overlay.plugin import WatermarkOverlayPlugin
from .cover_art.plugin import CoverArtPlugin


def build_registry() -> PluginRegistry:
    registry = PluginRegistry()
    registry.register(RemoveWatermarkPlugin())
    registry.register(WatermarkOverlayPlugin())
    registry.register(CoverArtPlugin())
    return registry
