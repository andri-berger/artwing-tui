from textual.app import ComposeResult
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widgets import DirectoryTree
from textual.binding import Binding
from textual.widget import Widget
from textual import on, work
from .script import (script_f4,
                     script_f7,
                     script_f6,
                     script_f5)
from pathlib import Path
import asyncio
import json

PORT = Path(__file__)
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Formula"
PATH_1 = PORT_0.parent / "uread.png"
PATH_2 = PORT_0.parent / "project.png"
PATH_3 = PORT_1 / "za.json"
PATH_4 = PORT_1 / "za.png"

# OK
class MainTab(Widget):
    config: reactive[dict] = reactive(
        dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(PATH_1)

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
                f13, f16, '-output', str(PATH_4),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL))
            await f17.communicate()

            f18 = Image(PATH_4)
            f19 = self.size
            script_f6(
                f18, f19, PATH_4)
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
    BINDINGS = [
        Binding("space",
        "select_cursor",
        "Select")]

    def __init__(self, path,
                 file_type, **kwargs) -> None:
        super().__init__(path, **kwargs)
        self.file_type = file_type

    def filter_paths(self, path) -> list:
        f0 = self.file_type
        f1 = f0 == "file-2"
        f2 = (".png",".json")
        return [h0 for h0 in path
                if (h0.suffix.lower() in
                    f2 or h0.is_dir() or f1)
                and not h0.name.startswith(".")
                and not (h0.parent.name == "_blank"
                         and f0 == "file-1")]

    @on(DirectoryTree.DirectorySelected)
    def select(self, event: DirectoryTree.DirectorySelected):
        f0 = self.app.query_one(MainTab)
        f1 = self.app.stores
        f2 = event.path.name
        f3 = f1['_blank']
        if f2 == "_blank":
            f4 = [f3[3], str(PATH_1)]
            f5 = script_f5(self, *f4)
            f0.config = [2, *f5, *f4]

            f3[3] = 0 or ""
            PATH_3.write_text(
                json.dumps(f1))

    @on(DirectoryTree.FileSelected)
    def selected(self, event: DirectoryTree.FileSelected):
        f0 = self.app.query_one("#data-table")
        f1 = self.app.query_one("#label-0")
        f2 = self.app.query_one(MainTab)
        f3 = f0.cursor_coordinate
        f4 = self.app.store
        f5 = self.app.stores
        f6 = event.control.id
        f7 = f6.split("-")[-1]
        f8 = f5['_blank']
        f9 = event.path
        f10 = f9.name

        if int(f7) <= 1:
            f11 = f10.split(".")
            if f11[-1] == "png":
                f12 = 2 - f8[0] or 0
                f13 = [f8[3], str(f9)]
                f14 = script_f5(self,*f13)
                f2.config = [f12,*f14,*f13]

            elif f11[-1] == "json":
                f15 = str(PATH_1)
                f16 = f9.read_text()
                f17 = json.loads(f16)
                self.app.stores = f17
                f18 = script_f4(f15, f17)

                if f18[-2]:
                    f19 = f18[-2]
                    f2.config = f18
                    script_f7(
                        self.app, f19)

            f20 = self.app.stores
            PATH_3.write_text(
                json.dumps(f20))

        elif int(f7) == 2:
            f21 = f4["1"]
            f22 = f21.get(f10)
            f23 = f5.get(f8[3])
            if f22 is not None:
                f24 = [f10, f8[4]]
                f25 = len(f22) > 1
                f26 = f22[1] if f25 else ""
                f27 = script_f5(self, *f24)
                f2.config = [0, *f27, *f24]
                self.app.textfield = f26
                f1.update(f26)

            if f23 is not None:
                if len(f23) > 0:
                    f23[0] = f3.row
                    f23[1] = f3.column

            PATH_3.write_text(
                json.dumps(f5))
