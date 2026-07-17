import sys

import logfire

from app.config import settings

_configured = False


def _configure_windows_console_utf8() -> None:
    if sys.platform != "win32":
        return
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="replace")


def configure_logfire(service_name: str = "enterprise-rag") -> None:
    """Configure Logfire once per process. Set LOGFIRE_TOKEN in .env to send traces."""
    global _configured
    if _configured:
        return

    _configure_windows_console_utf8()

    kwargs = {
        "service_name": service_name,
        "send_to_logfire": "if-token-present",
    }
    if settings.LOGFIRE_TOKEN:
        kwargs["token"] = settings.LOGFIRE_TOKEN

    logfire.configure(**kwargs)
    _configured = True
