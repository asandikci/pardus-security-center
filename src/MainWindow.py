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
LICENSE = "GPL-3"

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
        self.schema = "com.asandikci.pardus-security-center"
        self.app = app

        self.load_data()

        self.setup_finished()  # TEMPORARY DEVELOPMENT

        self.setup_ui()

    # == SETUP FUNCTIONS ==
    def load_data(self):
        Ptk.utils.load_css(
            os.path.dirname(os.path.abspath(__file__)) + "/../data/style.css"
        )

    def check_setup_complete(self):
        """returns boolean value to check if initial applicaton setup completed"""
        self.setup_completed = bool(
            Ptk.utils.gsettings_get(self.schema, "setup-completed")
        )
        if self.setup_completed:
            return 1
        return 0

    def setup_ui(self):
        self.headerbar = Adw.HeaderBar()
        self.about_button = Ptk.Button(icon="dialog-information-symbolic")
        self.about_button.connect("clicked", self._show_about)

        if self.check_setup_complete():
            print("SETUP COMPLETED, LOADING HEADER BAR")
            self.headerbar.pack_end(self.about_button)
            self.setup_ui_menu(self.headerbar)
        else:
            print("SETUP NOT COMPLETED YET")
            self.headerbar.pack_end(self.about_button)
            pass

        self.window.set_titlebar(self.headerbar)

    def setup_ui_menu(self, headerbar):
        self.stack = Ptk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(500)

        from Pages import (
            MalwareScan,
            Firewall,
            Other,
        )

        self.stack.add_titled(MalwareScan.Menu(app=self.app), "malware-scan", _("Malware Scan"))
        self.stack.add_titled(Firewall.Menu(), "firewall", _("Firewall"))
        self.stack.add_titled(Other.Menu(), "other", _("Other"))

        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)

        headerbar.set_title_widget(self.stack_switcher)
        self.window.set_child(self.stack)

    def setup_finished(self):
        """update schema when application setup finished"""
        Ptk.utils.gsettings_set(
            self.schema, "setup-completed", GLib.Variant.new_boolean(True)
        )

    # == FUNCTIONS ==
    def _show_about(self, button):
        dialog = Ptk.AboutWindow(
            application_name=APPNAME,
            version=VERSION,
            developer_name=APPNAME,
            license_type=LICENSE,
            comments=_("Secure and Monitor Pardus"),
            website=WEBSITE,
            issue_url=WEBSITE,
            credit_section=[_("Contributors"), [DEV]],
            translator_credits=DEV,
            copyright="Aliberk Sandıkçı | 2024",
            developers=[DEV],
            application_icon=ICON,
            transient_for=self.window,
            modal=True,
        )
        dialog.show()
