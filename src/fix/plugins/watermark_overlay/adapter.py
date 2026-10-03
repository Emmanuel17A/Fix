from __future__ import annotations

from fix.core.errors import PluginValidationError
from fix.core.models import OperationContext, OperationPlan
from fix.core.plugin import PluginAdapter
from fix.media.ffmpeg import overlay_watermark_local
from fix.media.validation import validate_output


class WatermarkOverlayAdapter(PluginAdapter):
    def validate(self, context: OperationContext) -> None:
        if not context.source.exists():
            raise PluginValidationError("Source video does not exist.")
        if not context.selections:
            raise PluginValidationError("Draw at least one selection first.")
        if context.asset is None or not context.asset.exists():
            raise PluginValidationError("Choose a watermark image first.")
        if not context.duration_seconds or context.duration_seconds <= 0:
            raise PluginValidationError(
                "Watermark duration must be greater than zero."
            )

    def build_plan(self, context: OperationContext) -> OperationPlan:
        self.validate(context)

        def runner(progress):
            result = overlay_watermark_local(
                source=context.source,
                watermark=context.asset,
                selections=context.selections,
                media=context.media,
                edit_start=context.start_seconds,
                edit_duration=float(context.duration_seconds),
                progress=progress,
            )
            validate_output(result)
            return result

        return OperationPlan(
            label="Add / Replace Watermark",
            runner=runner,
            output=context.source,
            replace_source=True,
        )
