class FixError(Exception):
    """Base FIX error."""


class PluginValidationError(FixError):
    """Raised when plugin input is invalid."""


class MediaProcessingError(FixError):
    """Raised when FFmpeg/FFprobe processing fails."""
