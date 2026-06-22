from typing import Any

from textual.widgets import DirectoryTree
from textual.app import ComposeResult
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widget import Widget
from textual import on, work
from .script import (script_f4,
                     script_f7,
                     script_f6,
                     script_f5)
from pathlib import Path
import asyncio
import shutil
import json


PORT = Path(__file__)
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Formula"
PATH_2 = PORT_0.parent / "uread.png"
PATH_3 = PORT_0.parent / "project.png"
PATH_4 = PORT_1 / "za.json"
PATH_5 = PORT_1 / "za.png"


# click on _blank show default-file
# rename global custom variables
# delete file from local filepicker
# übersicht space/enter/etc. auf functions
# var adjustments grid (current value in input, no input on propert-text)
# implementation real-time effect !!
# add json on top of png on CREATE-PRESS
# go through full funcionality filepicker selectedEvent

# OK
class MainTab(Widget):
    config: reactive[dict] = reactive(
        dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(PATH_2)

    def on_mount(self) -> None:
        f0 = self.query_one(Image)
        f0.styles.width = "auto"
        f0.styles.height = "100%"

    @work(exclusive=True)
    async def watch_config(self, value) -> None:
        f1 = self.app.query_one("#data-table")
        f2 = self.app.store["2"]
        f3 = self.app.store["0"]
        f4 = value[3:-2]
        f5 = value[-2]
        f6 = value[-1]

        if self.query(Image):
            (self.query_one(Image)
             .remove())

        if value[0] == 0:
            with self.app.batch_update():
                f1.clear(columns=False)
                f7 = f2.get(f"{f5}",[])
                f8 = max(len(f7),10)

                for row_i in range(f8):
                    f9 = len(f7) > row_i
                    f10 = len(f4) > row_i
                    f11 = f4[row_i] if f10 else ""
                    f12 = f7[row_i] if f9 else [""]
                    f1.add_row(f12[0],str(f11))

                f1.move_cursor(
                    row=value[1],
                    column=value[2])

        if value[0] <= 1:
            f13 = f3.get(f5, f5)
            f14 = ",".join(str(p) for p in f4)
            f15 = [x for x in f4 if x != ""]
            f16 = f14 if len(f15) else ","

            f17 = await (asyncio
            .create_subprocess_exec(
                "gmic", str(f6),
                f13, f16, '-output', str(PATH_5),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL))
            await f17.communicate()

            f18 = Image(PATH_5)
            f19 = self.size
            script_f6(
                f18, f19, PATH_5)
            await self.mount(f18)

        if value[0] == 2:
            f20 = Image(f6)
            f21 = self.size
            script_f6(f20, f21, f6)
            await self.mount(f20)

    def render(self):
        return ""


class FileTree(DirectoryTree):
    show_root = False

    def __init__(self, path,
                 file_type, **kwargs) -> None:
        super().__init__(path, **kwargs)
        self.file_type = file_type

    def filter_paths(self, h0) -> list:
        f0 = self.file_type
        f1 = f0 == "file-2"
        f2 = (".png",".json")
        return [h1 for h1 in h0
                if (h1.suffix.lower() in
                    f2 or h1.is_dir() or f1)
                and not h1.name.startswith(".")
                and not (h1.parent.name == "_blank"
                         and f0 == "file-1")]

    @on(DirectoryTree.FileSelected) #Enter only
    async def selected(self, event: DirectoryTree.FileSelected):
        f3 = self.app.query_one(MainTab)
        f2 = self.app.query_one("#data-table")
        f0 = self.app.query_one("#dir-tree-2")
        f1 = self.app.query_one("#label-0")
        f4 = self.app.store["1"]
        f5 = self.app.stores
        f6 = event.control.id
        f7 = f5['_blank'][4]
        f8 = f5['_blank'][3]
        f9 = event.path
        f10 = f9.name
        f12 = str(f9)
        f11 = str(PATH_2)

        if not f9.is_file():
            return

        if (f6 == "dir-tree-0"
                or f6 == "dir-tree-1"):
            fx6 = f10.split(".")[-1]

            if fx6 == "json":
                shutil.copy2(f9, PATH_4)
                f13 = f9.read_text()
                f14 = json.loads(f13)
                self.app.stores = f14
                f15 = script_f4(f11, f14)

                if f15[-2]:
                    f3.config = f15
                    script_f7(self, f15[-2])
                    self.reload()

            elif fx6 == "png":
                f16 = script_f5(self, f8, f12)
                f3.config = [2,*f16,f8,f12]

                f17 = f0.cursor_node
                if f17 and f17.parent:
                    f17.parent.collapse()
                f0.move_cursor(
                    f0.root.children[0])

                PATH_4.write_text(
                    json.dumps(f5))

        elif f6 == "dir-tree-2":
                f18 = f4.get(f10, [])
                f19 = f5.get(f8,[])
                f20 = len(f18) > 1
                f21 = script_f5(self, f10, f7)
                f22 = f2.cursor_coordinate
                f3.config = [0,*f21,f10,f7]

                f23 = f18[1] if f20 else ""
                self.app.textfield = f23
                f1.update(f23)

                if len(f19) > 0:
                    f19[0] = f22.row if len(f19) > 0 else 0
                    f19[1] = f22.column if len(f19) > 0 else 0

                PATH_4.write_text(
                    json.dumps(f5))
