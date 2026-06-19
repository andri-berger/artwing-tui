from textual.app import App, ComposeResult
from pathlib import Path
from .model import ImageTab
from .builds import TableApp
from .script import helsing
from .script import checker
import json


PATH = Path(__file__).parent
PATH_0 = PATH.parent / "Formula"
PATH_1 = PATH.parent / "Fontend"
PATH_2 = PATH.parent / "Backend"
PATH_3 = PATH.parent / "build.json"
PATH_4 = PATH.parent / "uread.png"
PATH_5 = PATH_2 / "style.tcss"
PATH_6 = PATH_0 / "za.json"


class CLIApp(App):
    COMMAND_PALETTE_DISPLAY = None
    NOTIFICATION_TIMEOUT = 10
    CSS_PATH = PATH_5
    AUTO_FOCUS = '*'

    def __init__(self):
        super().__init__()
        self.page = None
        self.pw = None
        self.server = None
        self.store = json.loads(
            PATH_3.read_text())
        self.stores = json.loads(
            PATH_6.read_text()) \
            if PATH_6.exists() else {}

    def compose(self) -> ComposeResult:
        yield TableApp()

    def on_mount(self) -> None:
        f0 = self.query_one("#dir-tree-1")
        f1 = self.query_one(ImageTab)
        f5 = self.app.stores
        f6 = str(PATH_4) or ""
        f2 = helsing(f5,f6)
        self.set_focus(f0)

        if f2[-2]:
            f1.config = f2
        checker(self,f2[-2])


    async def on_unmount(self) -> None:
        if self.server:
            self.server.shutdown()
        if self.pw:
            await self.pw.stop()

