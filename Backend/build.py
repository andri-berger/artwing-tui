import json
from pathlib import Path

from textual.app import App, ComposeResult

from .builds import MainApp
from .model import MainTab
from .script import script_f5, script_f7

PORT = Path(__file__).parent
PORT_0 = PORT.parent / "Backend"
PORT_1 = PORT.parent / "Fontend"
PORT_2 = PORT.parent / "Formula"
PATH_2 = PORT.parent / "uread.png"
PATH_3 = PORT.parent / "build.json"
PATH_4 = PORT_0 / "style.tcss"
PATH_5 = PORT_2 / "var.json"


class CLIApp(App):
    AUTO_FOCUS = None
    COMMAND_PALETTE_DISPLAY = None
    ENABLE_COMMAND_PALETTE = False
    NOTIFICATION_TIMEOUT = 3
    CSS_PATH = PATH_4

    def __init__(self) -> None:
        super().__init__()
        self.vertical = 1
        self.horizontal = 0
        self.clipboards = ""
        self.textfield = ""
        self.textfields = None
        self.store = json.loads(PATH_3.read_text())
        self.stores = json.loads(PATH_5.read_text()) if PATH_5.exists() else {}
        f0 = self.store.get("0", [])
        f1 = self.store.get("1", [])
        f2 = self.stores.get("_blank", [])
        f3 = "textual-dark"

        f4 = len(f2) > 1
        f5 = len(f2) > 2
        f6 = f2[1] if f4 else 0
        f7 = f2[2] if f5 else 0
        self.initial = f7 or 0
        self.theme = f1[f7] if len(f1) > f7 else f3
        f8 = f6 or 3
        f9 = f0[f8 - 1]
        self.f6 = f"#{f9}"

    def on_mount(self) -> None:
        f0 = self.query_one(MainTab)
        f1 = script_f5(str(PATH_2), self.stores)

        if f1[-2]:
            f0.config = f1
            script_f7(self, f1[-2])

        self.set_focus(self.query_one(self.f6))

    def compose(self) -> ComposeResult:
        yield MainApp()
