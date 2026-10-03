from __future__ import annotations

from pathlib import Path

from fix.core.errors import PluginValidationError
from fix.core.models import OperationContext, OperationPlan
from fix.core.plugin import PluginAdapter
from fix.media.ffmpeg import replace_cover
from fix.media.validation import validate_output


class CoverArtAdapter(PluginAdapter):
    def validate(self, context: OperationContext) -> None:
        if not context.source.exists():
            raise PluginValidationError("Source video does not exist.")
        if context.asset is None or not context.asset.exists():
            raise PluginValidationError("Choose a cover image first.")
        if context.output is None:
            raise PluginValidationError("Output path is required.")

    def build_plan(self, context: OperationContext) -> OperationPlan:
        self.validate(context)
        output = Path(context.output)

        def runner(progress):
            result = replace_cover(
                source=context.source,
                cover=context.asset,
                output=output,
                media=context.media,
                progress=progress,
            )
            validate_output(result)
            return result

        return OperationPlan(
            label="Thumbnail / Cover",
            runner=runner,
            output=output,
        )
