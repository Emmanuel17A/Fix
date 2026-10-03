from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from .models import OperationContext, OperationPlan


@dataclass(frozen=True)
class PluginMetadata:
    plugin_id: str
    name: str
    version: str
    description: str


class PluginAdapter(ABC):
    @abstractmethod
    def validate(self, context: OperationContext) -> None:
        raise NotImplementedError

    @abstractmethod
    def build_plan(self, context: OperationContext) -> OperationPlan:
        raise NotImplementedError


class FixPlugin(ABC):
    metadata: PluginMetadata

    @abstractmethod
    def create_adapter(self) -> PluginAdapter:
        raise NotImplementedError
