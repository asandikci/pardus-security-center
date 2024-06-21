#!/usr/bin/env python3

import gi, sys

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gio, GLib, Adw


class Application(Adw.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="com.asandikci.pardus-security-center",
            flags=Gio.ApplicationFlags.NON_UNIQUE,
            **kwargs
        )
        self.connect("activate", self.on_activate)
        self.main_window = None

        GLib.set_prgname("com.asandikci.pardus-security-center")

    def on_activate(self, app):
        if not self.main_window:  # prevent opening multiple window
            from MainWindow import MainWindow

            self.main_window = MainWindow(app=app).window
            self.main_window.present()


app = Application()
app.run(sys.argv)
