import gi

gi.require_version("Gtk", "4.0")
from libpardus import Ptk
from gi.repository import Gtk


class Menu(Ptk.ScrolledWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.text_view = Gtk.TextView(
            monospace=True, left_margin=5, right_margin=5, top_margin=5
        )
        self.set_child(self.text_view)
