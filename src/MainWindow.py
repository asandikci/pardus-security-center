import gi
import os
import json
import locale

gi.require_version("Adw", "1")
gi.require_version("Gtk", "4.0")

from libpardus import Ptk
from gi.repository import Adw, Gtk, GLib
from locale import gettext as _

VERSION = "0.0.1"
APPNAME = "Pardus Security Center"
DEV = "Aliberk Sandıkçı"
WEBSITE = "https://github.com/asandikci/pardus-security-center"
ICON = "pardus-security-center"

APPNAME_CODE = "pardus-security-greeter"
TRANSLATIONS_PATH = "/usr/share/locale"
locale.bindtextdomain(APPNAME_CODE, TRANSLATIONS_PATH)
locale.textdomain(APPNAME_CODE)


class MainWindow(Ptk.ApplicationWindow):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = Ptk.ApplicationWindow(
            title=_("Pardus Security Center"), width=850, height=580
        )
        self.window.set_application(app)

        self.load_data()

        self.handle_schema("com.asandikci.pardus-security-center")

    # == STARTUP FUNCTIONS ==
    def load_data(self):
        Ptk.utils.load_css(
            os.path.dirname(os.path.abspath(__file__)) + "/../data/style.css"
        )

        self.load_shortcuts("/../data/shortcuts.json")
        self.load_shortcuts("/../data/custom_shortcuts.json")

    def load_shortcuts(self, path):
        with open(os.path.dirname(os.path.abspath(__file__)) + path) as shortcut:
            self.shortcuts = json.loads(shortcut.read())
            # FIXME Shortcuts not handled 

    def handle_schema(self, schema):
        self.schema = schema
        self.first_run = bool(Ptk.utils.gsettings_get(self.schema, "first-run"))
        if self.first_run:
            Ptk.utils.gsettings_set(
                self.schema, "first-run", GLib.Variant.new_boolean(False)
            )
