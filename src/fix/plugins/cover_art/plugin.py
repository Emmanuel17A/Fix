from __future__ import annotations

from fix.core.plugin import FixPlugin, PluginMetadata
from .adapter import CoverArtAdapter


class CoverArtPlugin(FixPlugin):
    metadata = PluginMetadata(
        plugin_id="cover_art",
        name="Thumbnail / Cover",
        version="1.0.0",
        description="Replace embedded cover artwork without re-encoding the main video.",
    )

    def create_adapter(self) -> CoverArtAdapter:
        return CoverArtAdapter()
