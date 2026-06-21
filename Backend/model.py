from textual.widgets import DirectoryTree
from textual.app import ComposeResult
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widget import Widget
from textual import on, work

from .script import (script_f1,
                     script_f0, script_f3, script_f2)

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


# fouc flickering
# tcss overhaul
# delete file from local filepicker
# viewport height / fullwidth switch


# remove background only gerüst
# style switcher border/outline
# BOX-SIZING ???
# action key bindings
# inline markup [b]
# self.notify, markup=false
# structure widget vs app vs custom => analyze
# color / background structure range / tint
# scan and categorize all import modules


class ImageTab(Widget):
    config: reactive[dict] = reactive(
        dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(PATH_2)

    def on_mount(self) -> None:
        self.query_one(Image).styles.width = "auto"
        self.query_one(Image).styles.height = "100%"

    @work(exclusive=True)
    async def watch_config(self, value: dict):
        f0 = self.app.query_one("#data-table")
        f1 = self.app.store["2"]
        f2 = self.app.store["0"]
        f3 = value[3:-2]
        f4 = value[-2]
        f5 = value[-1]

        if self.query(Image):
            (self.query_one(Image)
             .remove())

        if value[0] == 0:
            with self.app.batch_update():
                f0.clear(columns=False)
                f7 = f1.get(f"{f4}",[])
                for row_i in range(9):
                    f8 = len(f7) > row_i
                    f9 = len(f3) > row_i
                    f10 = f3[row_i] if f9 else ""
                    f11 = f7[row_i] if f8 else [""]
                    f0.add_row(f11[0],f10 or "")

                f0.move_cursor(
                    row=value[1],
                    column=value[2])

        if value[0] <= 1:
            f6 = f2.get(f4, f4)
            f12 = ",".join(str(p) for p in f3)
            f13 = [x for x in f3 if x != ""]
            f14 = f12 if len(f13) else ","

            f15 = await (asyncio
            .create_subprocess_exec(
                "gmic", str(f5),
                f6, f14, '-output', str(PATH_5),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL))
            await f15.communicate()
            f16 = Image(PATH_5)
            script_f3(f16, self.size, PATH_5)
            await self.mount(f16)

        if value[0] == 2:
            f17 = Image(f5)
            script_f3(f17, self.size, f5)
            await self.mount(f17)

    def render(self):
        return ""


class FileTypeTree(DirectoryTree):
    show_root = False

    def __init__(self, path, file_type: str, **kwargs):
        self.file_type = file_type
        super().__init__(path, **kwargs)

    def filter_paths(self, paths):
        return [p for p in paths
                if self.is_allowed(p)
                and not p.name.startswith(".")]

    def is_allowed(self, p):
        f0 = p.suffix
        f1 = f0.lower()
        if p.is_dir():
            return True

        match self.file_type:
            case "naked":
                return f0 == ""
            case "multi":
                return (f1 == ".png"
                        or f1 == ".json")
        return False


    @on(DirectoryTree.FileSelected) #Enter only
    async def selected(self, event: DirectoryTree.FileSelected) -> None:
        f2 = self.app.query_one("#data-table")
        f0 = self.app.query_one("#dir-tree-1")
        f1 = self.app.query_one("#label-0")
        f3 = self.app.query_one(ImageTab)
        f4 = self.app.store["1"]
        f5 = self.app.stores
        f6 = event.control.id
        f7 = f5['_blank'][4]
        f8 = f5['_blank'][3]
        f9 = event.path
        f10 = f9.name
        f11 = str(PATH_2)
        f12 = str(f9)


        if not f9.is_file():
            return

        if (f6 == "dir-tree-0"
                or f6 == "dir-tree-2"):
            fx6 = f10.split(".")[-1]

            if fx6 == "json":
                shutil.copy2(f9, PATH_4)
                f13 = f9.read_text()
                f14 = json.loads(f13)
                self.app.stores = f14
                f15 = script_f1(f14, f11)

                if f15[-2]:
                    f3.config = f15
                    script_f0(self, f15[-2])
                    self.reload()

            elif fx6 == "png":
                f16 = script_f2(self, f8, f12)
                f3.config = [2,*f16,f8,f12]

                f17 = f0.cursor_node
                if f17 and f17.parent:
                    f17.parent.collapse()
                f0.move_cursor(
                    f0.root.children[0])

                PATH_4.write_text(
                    json.dumps(f5))

        elif f6 == "dir-tree-1":
                f18 = f4.get(f10, [])
                f19 = f5.get(f8,[])
                f20 = len(f18) > 1
                f21 = script_f2(self, f10, f7)
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
