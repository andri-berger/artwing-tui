from textual.app import App, ComposeResult
from pathlib import Path
from .model import ImageTab
from .builds import TableApp
from .script import (script_f1,
                     script_f0)
import json


PORT = Path(__file__).parent
PORT_0 = PORT.parent / "Formula"
PORT_1 = PORT.parent / "Fontend"
PORT_2 = PORT.parent / "Backend"
PATH_4 = PORT.parent / "uread.png"
PATH_3 = PORT.parent / "build.json"
PATH_5 = PORT_2 / "style.tcss"
PATH_6 = PORT_0 / "za.json"


class CLIApp(App):
    ENABLE_COMMAND_PALETTE = False
    COMMAND_PALETTE_DISPLAY = None
    NOTIFICATION_TIMEOUT = 10
    CSS_PATH = PATH_5
    AUTO_FOCUS = None

    def __init__(self):
        super().__init__()
        self.textfield = ''
        self.textfields = None
        self.store = json.loads(
            PATH_3.read_text())
        self.stores = json.loads(
            PATH_6.read_text()) \
            if PATH_6.exists() else {}

        f0 = self.store.get("4",[])
        f1 = self.store.get("5",[])
        f2 = self.stores.get("_blank",[])
        f3 = f2[1] if len(f2) > 0 else 0
        f4 = f2[2] if len(f2) > 2 else 3
        self.initial = f4 or 3
        self.theme = f1[f4] \
            if len(f1) > f4 \
            else "textual-dark"
        f5 = f0[f3] \
            if len(f0) > f3 \
            else "dir-tree-1"
        self.f6 = f"#{f5}"

    def compose(self) -> ComposeResult:
        yield TableApp()

    def on_mount(self) -> None:
        f0 = self.query_one(ImageTab)
        f1 = self.stores or {}
        f2 = str(PATH_4) or ""
        f3 = script_f1(f1, f2)

        if f3[-2]:
            f0.config = f3
            script_f0(self, f3[-2])

        self.set_focus(
            self.query_one(
                self.f6))
