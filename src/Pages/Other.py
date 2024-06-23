import gi

gi.require_version("Gtk", "4.0")
from libpardus import Ptk
from gi.repository import Gtk


class Menu(Ptk.ScrolledWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.set_child(Ptk.Label(label="Not Implemented Yet"))
