from __future__ import annotations

from pathlib import Path

from .models import OperationPlan, ProgressCallback


class OperationExecutor:
    def execute(
        self,
        plan: OperationPlan,
        progress: ProgressCallback,
    ) -> Path:
        return plan.runner(progress)
