from textual.widgets import DirectoryTree
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widgets import DataTable
from textual.widget import Widget
from pathlib import Path
from textual import on
from .scripts import open_fred
from textual.app import ComposeResult
from .script import testlauf
import subprocess
import asyncio
import shutil
import time
import json


CWD = Path.cwd()
APP = Path(__file__)
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR.parent / "Fontend"
ASSETS = ASSETS_DIR / "Formula/za.png"
CONFIGS = APP_DIR.parent / "Formula/za.json"
IMAGES = APP_DIR.parent / "Formula/za.png"
TEST = APP_DIR.parent / "tconfig.png"

class ImageTab(Widget):
    config: reactive[dict] = reactive(dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(TEST)

    def on_mount(self) -> None:
        self.query_one(Image).styles.width = "auto"
        self.query_one(Image).styles.height = "100%"

    # 2 2 boxfit {}
    async def watch_config(self, value: dict):
        f02 = self.app.query_one("#label-0")
        f003 = self.app.store["0"]
        f03 = self.app.store["3"]

        f0 = self.app.query_one("#cont-switch-1")
        f1 = int(f0.current.split("-")[-1])
        f2 = self.app.query(DataTable)
        f3 = self.app.stores
        self.notify(f"model: {value}")
        test = value[2][2:-1]
        testr = value[2][-1]


        if value[0] == 1:
            with ((self.app.batch_update())):
                f2[0].clear(columns=False)
                f07 = f003[f"{self.app.now}"]
                for row_i in range(len(f07)):
                    ja = test[row_i] if len(test) > row_i else ""
                    row = [f07[row_i][0],ja]
                    f2[0].add_row(*row)

        def after_focus():
            f02.update(f03[self.app.now])
        self.call_after_refresh(
            after_focus)

        if value[1] == 1:
            f25 = int(time.time())
            f26 = CWD / f"{f25}.png"

        if value[1] == 0:
            params = ",".join(str(p) for p in test)
            check = [x for x in test if x != ""]
            params0 = params if len(check) else ","
            if self.query(Image):
                self.query_one(Image).remove()
            proc = await (asyncio
            .create_subprocess_exec(
                "gmic", str(TEST),
                testr, params0, '-output', str(IMAGES),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL))
            await proc.communicate()
            await self.mount(Image(IMAGES))
            testlauf(self,IMAGES,Image)

        CONFIGS.write_text(
        json.dumps(f3))

    def render(self):
        return ""


class FileTypeTree(DirectoryTree):
    show_root = False

    def __init__(self, path, file_type: str, **kwargs):
        self.file_type = file_type
        super().__init__(path, **kwargs)

    def filter_paths(self, paths):
        return [p for p in paths if not p.name.startswith(".")]

    def _is_allowed(self, p):
        if p.is_dir():
            return True  # always show dirs for navigation

        match self.file_type:
            case "multi":
                return (p.suffix.lower() == ".png"
                        or p.suffix.lower() == ".json")
        return False


    @on(DirectoryTree.FileSelected)
    async def selected(self, event: DirectoryTree.FileSelected) -> None:
        e_images = self.app.query_one(ImageTab)
        f0 = self.app.query_one("#cont-switch-2")
        f1 = self.app.query_one(f"#{f0.current}")
        f02 = self.app.query_one("#label-0")
        f2 = f0.current.split("-")[-1]
        f3 = self.app.stores
        f03 = self.app.store["3"]
        # f4 = self.app.coord
        f5 = event.control.id
        f6 = f5.split("-")[-1]
        f7 = ['4','5'][int(f6)-1]
        f8 = ["module","modules"]
        f9 = f8[int(f6)-1]
        f10 = event.path

        self.notify(f"File: {event.path.name}")

        if not f10.is_file():
            return

        if f5 == "dir-tree-0":
            shutil.copy2(f10, CONFIGS)
            f13 = f10.read_text()
            f14 = json.loads(f13)
            f14.update({'_': [2,1]})
            self.app.stores = f14
            self.e_images.config = f14
            await self.reload()

        elif f5 == "dir-tree-2":
            pass

        elif f5 == "dir-tree-1":
                self.app.now = f10.name
                # f15 = ASSETS_DIR / f9
                # f16 = f15 / f10.name
                # f02.update(f03[f10.name][0] or "")


                # f17 = f4.column
                # f18 = f4.row

                # if (int(f2) in [4, 5]
                #         and f17 == 12):
                #     f19 = f3.setdefault(f7, {})
                #     f20 = f19.setdefault(f18, {})
                #     f20[f17 or '11'] = f10.name
                #     f21 = f1.get_cell_at(f4)
                #     f22 = f15 / f21.name
                #     if f22.exists():
                #         f22.unlink()
                #     f1.update_cell_at(
                #         f4,f10.name)
                # else:
                #     f23 = f3.setdefault('0', {})
                #     f24 = f23.setdefault('40', {})
                #     f25 = f24[int(f6)-1] or ""
                #     f24[int(f6)-1] = f10.name
                #     f26 = f15 / f25
                #     if f26.exists():
                #         f26.unlink()

                f70 = self.app.store["0"]
                f05 = f70[self.app.now] or []

                test = sum(1 for row in f05
                           if row[0] != "")
                f06 = [""] * test
                self.notify(f"f05 {f06}")
                l93 = [0,0,*f06]
                l94 = [1,0,[*l93,f10.name]]
                self.app.stores[f10.name] = l93
                self.notify(f"l94 {l94}")
                e_images.config = l94
                # on_message(self,
                #            f10.name,
                #            "f0")
