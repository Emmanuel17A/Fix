from __future__ import annotations

import gi
gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from fix.ui.main_window import MainWindow


class FixApplication(Gtk.Application):
    def __init__(self):
        super().__init__(
            application_id="com.compilertechnologies.fix"
        )

    def do_activate(self):
        window = self.props.active_window
        if window is None:
            window = MainWindow(self)
        window.present()


def main() -> int:
    app = FixApplication()
    return app.run(None)
