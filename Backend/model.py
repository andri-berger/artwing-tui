from textual.widgets import (
    DirectoryTree,DataTable)
from textual.app import ComposeResult
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widget import Widget
from pathlib import Path
from textual import on,work

from .models import (
    testlauf,helsing,tester)

import asyncio
import shutil
import json


APP = Path(__file__)
APP_DIR = Path(__file__).parent
TEST = APP_DIR.parent / "uread.png"
IMAGES = APP_DIR.parent / "Formula" / "za.png"
CONFIGS = APP_DIR.parent / "Formula" / "za.json"


# worker @work
# changing themes
# remove background only gerüst
# style switcher border/outline
# BINDINGS = [Binding("ctrl+z", "suspend_process")]
# BOX-SIZING ???
# action key bindings
# inline markup [b]
# self.notify, markup=false
# structure widget vs app vs custom => analyze
# color / background structure range / tint
# scan and categorize all import modules
# https://github.com/jpfleury/gmic-filters-overview
# https://jpfleury.github.io/gfo-demos/demos/fruits-400/index.html#362a98b9c342


class ImageTab(Widget):
    config: reactive[dict] = reactive(dict, init=False)

    def compose(self) -> ComposeResult:
       yield Image(TEST)

    def on_mount(self) -> None:
        self.query_one(Image).styles.width = "auto"
        self.query_one(Image).styles.height = "100%"

    def _select_child(self, parent_node, f8,tree) -> None:
        for child in parent_node.children:
            if child.data.path.name == f8:
                tree.move_cursor(child)
                break

    @work(exclusive=True)
    async def watch_config(self, value: dict):
        f1 = self.app.query_one("#dir-tree-1")
        f0 = self.app.query_one(DataTable)
        f2 = self.app.store["0"]
        f02 = self.app.store["3"]
        f4 = value[3:-2]
        f5 = value[-2]
        f3 = value[-1]

        # (self.app.
        #  clear_notifications())
        # self.notify(f"00: {value}")

        if value[0] == 0:
            with self.app.batch_update():
                f0.clear(columns=False)
                f6 = f2[f"{f5}"]
                for row_i in range(9):
                    f7 = f6[row_i] if len(f6) > row_i else [""]
                    f8 = f4[row_i] if len(f4) > row_i else ""
                    f9 = [f7[0],f8]
                    f0.add_row(*f9)

                f0.move_cursor(
                    row=value[1],
                    column=value[2])

            f10 = f02.get(f5,[])
            f11 = f10[1] if len(f10) > 1 else ""
            f12 = Path(f1.path).resolve()
            for node in f1.root.children:
                f13 = node.data.path
                f14 = f13.relative_to(f12)
                if f14 == Path(f11):
                    node.expand()
                    self.call_after_refresh(
                        self._select_child,
                        node, f5,f1)
                    break

        if self.query(Image):
            self.query_one(Image).remove()

        if value[0] <= 1:
            f15 = ",".join(str(p) for p in f4)
            f16 = [x for x in f4 if x != ""]
            f17 = f15 if len(f16) else ","

            self.notify(f"00: {f17}")

            f18 = await (asyncio
            .create_subprocess_exec(
                "gmic", str(f3),
                f5, f17, '-output', str(IMAGES),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL))
            await f18.communicate()
            f19 = Image(IMAGES)
            testlauf(f19,self.size,IMAGES)
            await self.mount(f19)
            # self.post_message("")

        if value[0] == 2:
            f20 = Image(f3)
            testlauf(f20,self.size,f3)
            await self.mount(f20)

    def render(self):
        return ""


class FileTypeTree(DirectoryTree):
    show_root = False

    def __init__(self, path, file_type: str, **kwargs):
        self.file_type = file_type
        super().__init__(path, **kwargs)

    def filter_paths(self, paths):
        return [p for p in paths if not p.name.startswith(".") and self._is_allowed(p)]

    def _is_allowed(self, p):
        if p.is_dir():
            return True  # always show dirs for navigation

        match self.file_type:
            case "naked":
                return p.suffix == ""
            case "multi":
                return (p.suffix.lower() == ".png"
                        or p.suffix.lower() == ".json")
        return False


    @on(DirectoryTree.FileSelected) #Enter only
    async def selected(self, event: DirectoryTree.FileSelected) -> None:
        f0 = self.app.query_one("#dir-tree-1")
        f1 = self.app.query_one("#label-0")
        f2 = self.app.query_one(DataTable)
        f3 = self.app.query_one(ImageTab)
        f4 = self.app.store["3"]
        f5 = self.app.stores
        f6 = event.control.id
        f7 = f5['_blank'][4]
        f8 = f5['_blank'][3]
        f9 = event.path
        f10 = f9.name
        f11 = str(TEST)
        f12 = str(f9)

        self.notify(f"File selected: {event}")

        if not f9.is_file():
            return

        if (f6 == "dir-tree-0"
                or f6 == "dir-tree-2"):
            fx6 = f10.split(".")[-1]

            if fx6 == "json":
                shutil.copy2(f9, CONFIGS)
                f13 = f9.read_text()
                f14 = json.loads(f13)
                self.app.stores = f14
                f15 = helsing(f14,f11)
                f3.config = f15
                self.reload()

            elif fx6 == "png":
                f16 = tester(self,f8,f12)
                f3.config = [2,*f16,f8,f12]

                f17 = f0.cursor_node
                if f17 and f17.parent:
                    f17.parent.collapse()
                f0.move_cursor(
                    f0.root.children[0])

                CONFIGS.write_text(
                    json.dumps(f5))

        elif f6 == "dir-tree-1":
                f18 = f4.get(f10, [])
                f19 = f5.get(f8,[])
                f20 = len(f18) > 2
                f21 = tester(self,f10,f7)
                f22 = f2.cursor_coordinate
                f3.config = [0,*f21,f10,f7]

                f23 = f18[2] if f20 else ""
                f1.update(f23)

                if len(f19) > 0:
                    f19[0] = f22.row if len(f19) > 0 else 0
                    f19[1] = f22.column if len(f19) > 0 else 0

                CONFIGS.write_text(
                    json.dumps(f5))
