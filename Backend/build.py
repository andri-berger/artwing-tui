from textual.app import (
    App, ComposeResult)
from pathlib import Path
from .model import MainTab
from .builds import MainApp
from .script import (script_f4,
                     script_f7)
import json

PORT = Path(__file__).parent
PORT_0 = PORT.parent / "Formula"
PORT_1 = PORT.parent / "Fontend"
PORT_2 = PORT.parent / "Backend"
PATH_2 = PORT.parent / "uread.png"
PATH_3 = PORT.parent / "build.json"
PATH_4 = PORT_2 / "style.tcss"
PATH_5 = PORT_0 / "za.json"

class CLIApp(App):
    AUTO_FOCUS = None
    COMMAND_PALETTE_DISPLAY = None
    ENABLE_COMMAND_PALETTE = False
    NOTIFICATION_TIMEOUT = 10
    CSS_PATH = PATH_4

    def __init__(self) -> None:
        super().__init__()
        self.vertical = 1
        self.horizontal = 0
        self.clipboards = 0
        self.textfield = ''
        self.textfields = None
        self.store = json.loads(
            PATH_3.read_text())
        self.stores = json.loads(
            PATH_5.read_text()) \
            if PATH_5.exists() else {}

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
            else "dir-tree-2"
        self.f6 = f"#{f5}"

    def on_mount(self) -> None:
        f0 = self.query_one(
            MainTab)
        f1 = script_f4(
            str(PATH_2),
            self.stores)

        if f1[-2]:
            f0.config = f1
            script_f7(self, f1[-2])

        self.set_focus(
            self.query_one(self.f6))

    def compose(self) -> ComposeResult:
        yield MainApp()
