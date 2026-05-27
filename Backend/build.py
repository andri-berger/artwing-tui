from textual.app import App, ComposeResult
from .script import (make_layer, make_layers,
make_new, make_news, make_news_0)
from .model import ImageTab
from .builds import TableApp
from pathlib import Path
import json
import time


PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
CSS_PATHS = STATIC_DIR / "style.tcss"
CONFIG = STATIC_DIR / "build.json"
CONFIGS = STATIC_DIR / "model.json"


class CLIApp(App):
    COMMAND_PALETTE_DISPLAY = None
    NOTIFICATION_TIMEOUT = 2
    CSS_PATH = CSS_PATHS
    AUTO_FOCUS = '*'

    def __init__(self):
        super().__init__()
        self.helpful = {}
        self.page = None
        self._pw = None
        self._server = None
        self.store = json.loads(
            CONFIG.read_text())
        self.stores = json.loads(
            CONFIGS.read_text()) \
            if CONFIGS.exists() else {}

        self.store["1-4"] = make_new("Image")
        self.store["1-5"] = make_new("Text")
        self.store["2-4"] = make_news_0("Image")
        self.store["2-5"] = make_news_0("Text")
        self.store["3-4"] = make_news("Image")
        self.store["3-5"] = make_news("Text")

        self.store["00"] = [
            make_layer("1"),
            make_layer("2"),
            make_layer("-3"),
            make_layer("808080"),
            make_layer("ffffff"),
            make_layers("ffffff"),
            make_layers("808080"),
            make_layers("0"),
            make_layers("1"),
            make_layers("2")]


    def compose(self) -> ComposeResult:
        yield TableApp()

    async def on_mount(self) -> None:
        self.e_images = self.query_one(ImageTab)
        dt = self.query_one("#data-table-0")
        self.set_focus(dt)

        if self.stores == {}:
            f1 = self.stores
            now = int(time.time())
            ss = f1.setdefault('0', {})
            st = ss.setdefault('39', {})
            for k in ['0', '1', '2']:
                    st[k] = now

        l0 = {**self.stores}
        l0['_'] = [2,1 if l0 else 2]
        self.e_images.config = l0


    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()
