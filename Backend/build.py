from textual.app import App, ComposeResult
from .model import ImageTab
from .builds import TableApp
from pathlib import Path
import json


PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
STATIC_BAC = PATH_FILE.parent / "Backend"
CSS_PATHS = STATIC_BAC / "model.tcss"
CONFIG = PATH_FILE.parent / "build.json"
CONFIGS = PATH_FILE.parent / "Formula/za.json"


class CLIApp(App):
    COMMAND_PALETTE_DISPLAY = None
    NOTIFICATION_TIMEOUT = 10
    CSS_PATH = CSS_PATHS
    AUTO_FOCUS = '*'

    def __init__(self):
        super().__init__()
        self.helpful = {}
        self.now = "_blank" # global operator
        self.page = None
        self._pw = None
        self._server = None
        self.store = json.loads(
            CONFIG.read_text())
        self.stores = json.loads(
            CONFIGS.read_text()) \
            if CONFIGS.exists() else {}

    def compose(self) -> ComposeResult:
        yield TableApp()

    async def on_mount(self) -> None:
        self.e_images = self.query_one(ImageTab)
        dt = self.query_one("#dir-tree-1")
        self.set_focus(dt)

        if self.stores:
            yy = self.stores
            l0 = yy.get("_blank",[])
            l1 = l0[2] if len(l0) > 2 else "_"
            l2 = yy.get(l1)
            if l2 is not None:
                l3 = [*l2,l1]
                self.e_images.config = [0,l3]

    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()


