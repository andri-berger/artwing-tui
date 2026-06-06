from textual.app import App, ComposeResult
from .model import ImageTab
from .builds import TableApp
from pathlib import Path
from .models import helsing
import json

PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
STATIC_BAC = PATH_FILE.parent / "Backend"
CSS_PATHS = STATIC_BAC / "style.tcss"
CONFIG = PATH_FILE.parent / "build.json"
CONFIGS = PATH_FILE.parent / "Formula/za.json"
TEST = PATH_FILE.parent / "uread.png"

class CLIApp(App):
    COMMAND_PALETTE_DISPLAY = None
    NOTIFICATION_TIMEOUT = 10
    CSS_PATH = CSS_PATHS
    AUTO_FOCUS = '*'

    def __init__(self):
        super().__init__()
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
        f0 = self.query_one("#dir-tree-1")
        f1 = self.query_one(ImageTab)
        f5 = self.app.stores
        f6 = str(TEST) or ""
        f2 = helsing(f5,f6)
        self.notify(f"00:::: {f2}")
        self.set_focus(f0)

        if f2[-2]:
            f1.config = f2

    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()

