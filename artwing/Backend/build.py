import json
import shutil
from pathlib import Path

from textual.app import App, ComposeResult

from .builds import MainApp
from .model import MainTab
from .script import (
    PATH_00,
    _ignore,
    script_f01,
    script_f5,
    script_f7,
)

PORT_0 = script_f01()
PORT_1 = Path(__file__).parent
PORT_2 = PORT_1.parent / "Backend"
PORT_3 = PORT_1.parent / "Frontend"
PATH_3 = PORT_1.parent / "build.png"
PATH_4 = PORT_1.parent / "build.json"
PATH_6 = PORT_2 / "style.tcss"
PATH_7 = PORT_0 / "_blank"



shutil.copytree(
    PORT_3,
    PORT_0,
    ignore=_ignore,
    dirs_exist_ok=True,
)
for entry in PATH_7.iterdir():
    shutil.rmtree(
        entry
    ) if entry.is_dir() else entry.unlink()


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
        self.toasts = {}
        self.store = json.loads(
            PATH_4.read_text()
        )
        self.stores = (
            json.loads(PATH_00.read_text())
            if PATH_00.exists()
            else {}
        )
        # drop themes this textual version
        # doesn't ship (e.g. textual-ansi)
        self.store["1"] = [
            h
            for h in self.store.get("1", [])
            if h in self.available_themes
        ]
        f0 = self.store.get("0", [])
        f1 = self.store.get("1", [])
        f2 = self.stores.get("_blank", [])
        f3 = "textual-dark"

        f4 = len(f2) > 1
        f5 = len(f2) > 2
        f6 = f2[1] if f4 else 0
        f7 = f2[2] if f5 else 0
        # the theme is stored by name, older
        # states hold an index into the list
        if f7 in f1:
            f7 = f1.index(f7)
        elif not (
            isinstance(f7, int)
            and 0 <= f7 < len(f1)
        ):
            f7 = 0
        self.initial = f7
        self.theme = f1[f7] if f1 else f3
        f8 = f6 or 3
        f9 = f0[f8 - 1]
        self.f6 = f"#{f9}"
        # what on_mount restores, MainTab skips
        # the fallback image when there is one
        self.restored = script_f5(
            str(PATH_3), self.stores
        )

    def notify(self, h, **kwargs) -> None:
        # Info toasts: each text only the
        # first 3 times per app start;
        # warnings and errors always show
        f0 = kwargs.get("severity", "information")
        f1 = self.toasts.get(h, 0)
        if f0 == "information" and f1 >= 3:
            return
        self.toasts[h] = f1 + 1
        # One toast at a time: a new one
        # replaces the current one (queued,
        # as notify itself is a message)
        self.call_later(self.clear_toasts)
        super().notify(h, **kwargs)

    def clear_toasts(self) -> None:
        # Holders stay behind cleared toasts
        # and would push the next one down
        self.clear_notifications()
        self.screen.query("ToastHolder").remove()

    def on_mount(self) -> None:
        f0 = self.query_one(MainTab)
        f1 = self.restored

        if f1[-1]:
            f0.config = f1
        if f1[-2]:
            script_f7(self, f1[-2])

        # reopen the left tree at the last file,
        # queued behind the tree's own first load
        f2 = self.stores["_blank"][4]
        f3 = self.query_one("#dir-tree-0")
        if f2 != str(PATH_3):
            f3.call_later(f3.reveal, f2)

        self.set_focus(self.query_one(self.f6))

    def compose(self) -> ComposeResult:
        yield MainApp()
