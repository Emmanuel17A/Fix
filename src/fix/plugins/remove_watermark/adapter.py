from __future__ import annotations

from pathlib import Path

from fix.core.errors import PluginValidationError
from fix.core.models import OperationContext, OperationPlan
from fix.core.plugin import PluginAdapter
from fix.media.ffmpeg import remove_watermark
from fix.media.validation import validate_output


class RemoveWatermarkAdapter(PluginAdapter):
    def validate(self, context: OperationContext) -> None:
        if not context.source.exists():
            raise PluginValidationError("Source video does not exist.")
        if not context.selections:
            raise PluginValidationError("Draw at least one selection first.")
        if context.output is None:
            raise PluginValidationError("Output path is required.")

    def build_plan(self, context: OperationContext) -> OperationPlan:
        self.validate(context)
        output = Path(context.output)

        def runner(progress):
            result = remove_watermark(
                source=context.source,
                output=output,
                selections=context.selections,
                media=context.media,
                progress=progress,
            )
            validate_output(result)
            return result

        return OperationPlan(
            label="Remove Watermark",
            runner=runner,
            output=output,
        )
