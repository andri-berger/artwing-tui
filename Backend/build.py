import json
import shutil
from pathlib import Path
from textual.app import App, ComposeResult

from .builds import MainApp
from .model import MainTab
from .script import (script_f00,
                     script_f01,
                     script_f5,
                     script_f7)

PORT_0 = script_f01()
PORT_1 = Path(__file__).parent
PORT_2 = PORT_1.parent / "Backend"
PORT_3 = PORT_1.parent / "Fontend"
PATH_3 = PORT_1.parent / "uread.png"
PATH_4 = PORT_1.parent / "build.json"
PATH_5 = script_f00() / "var.json"
PATH_6 = PORT_2 / "style.tcss"

class CLIApp(App):
    AUTO_FOCUS = None
    COMMAND_PALETTE_DISPLAY = None
    ENABLE_COMMAND_PALETTE = False
    NOTIFICATION_TIMEOUT = 3
    CSS_PATH = PATH_6

    def __init__(self) -> None:
        super().__init__()
        self.vertical = 1
        self.horizontal = 0
        self.clipboards = ""
        self.textfield = ""
        self.textfields = None
        self.store = json.loads(
            PATH_4.read_text()
        )
        self.stores = (
            json.loads(PATH_5.read_text())
            if PATH_5.exists()
            else {}
        )
        f0 = self.store.get("0", [])
        f1 = self.store.get("1", [])
        f2 = self.stores.get("_blank", [])
        f3 = "textual-dark"

        f4 = len(f2) > 1
        f5 = len(f2) > 2
        f6 = f2[1] if f4 else 0
        f7 = f2[2] if f5 else 0
        self.initial = f7 or 0
        self.theme = (
            f1[f7] if len(f1) > f7 else f3
        )
        f8 = f6 or 3
        f9 = f0[f8 - 1]
        self.f6 = f"#{f9}"

        shutil.copytree(
            PORT_3, PORT_0, ignore=shutil.
            ignore_patterns(".idea"),
            dirs_exist_ok=True)

    def on_mount(self) -> None:
        f0 = self.query_one(MainTab)
        f1 = script_f5(str(PATH_3), self.stores)
        self.notify("hello!!!")

        if f1[-2]:
            f0.config = f1
            script_f7(self, f1[-2])

        self.set_focus(self.query_one(self.f6))

    def compose(self) -> ComposeResult:
        yield MainApp()
