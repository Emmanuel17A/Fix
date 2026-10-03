#!/usr/bin/env python3
from __future__ import annotations

import importlib
import shutil
import sys


def check_module(name: str, label: str) -> bool:
    try:
        importlib.import_module(name)
        print(f"[OK] {label}")
        return True
    except Exception as exc:
        print(f"[MISSING] {label}: {exc}")
        return False


def check_command(name: str) -> bool:
    path = shutil.which(name)
    if path:
        print(f"[OK] {name}: {path}")
        return True
    print(f"[MISSING] {name}")
    return False


def main() -> int:
    ok = True

    try:
        import gi
        gi.require_version("Gtk", "4.0")
        from gi.repository import Gtk  # noqa: F401
        print("[OK] GTK 4 / PyGObject")
    except Exception as exc:
        print(f"[MISSING] GTK 4 / PyGObject: {exc}")
        ok = False

    ok &= check_module("cairo", "PyCairo")
    ok &= check_module("cv2", "OpenCV")
    ok &= check_command("ffmpeg")
    ok &= check_command("ffprobe")

    if not ok:
        print()
        print("FIX cannot start until the missing dependencies are installed.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
