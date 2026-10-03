from __future__ import annotations

from .plugin import FixPlugin


class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: dict[str, FixPlugin] = {}

    def register(self, plugin: FixPlugin) -> None:
        plugin_id = plugin.metadata.plugin_id
        if not plugin_id:
            raise ValueError("Plugin ID cannot be empty.")
        if plugin_id in self._plugins:
            raise ValueError(f"Plugin already registered: {plugin_id}")
        self._plugins[plugin_id] = plugin

    def get(self, plugin_id: str) -> FixPlugin:
        try:
            return self._plugins[plugin_id]
        except KeyError as exc:
            raise KeyError(f"Unknown plugin: {plugin_id}") from exc

    def all(self) -> tuple[FixPlugin, ...]:
        return tuple(self._plugins.values())
