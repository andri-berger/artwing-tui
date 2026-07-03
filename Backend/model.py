import asyncio
import json
from pathlib import Path

from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DirectoryTree
from textual_image.widget import Image

from .script import (
    script_f00,
    script_f3,
    script_f4,
    script_f5,
    script_f6,
    script_f7,
)

PORT = Path(__file__)
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Formula"
PATH_1 = PORT_0.parent / "uread.png"
PATH_2 = PORT_0.parent / "project.png"
PATH_3 = script_f00() / "var.json"
PATH_4 = script_f00() / "var.png"


class MainTab(Widget):
    config: reactive[dict] = reactive(
        dict, init=False
    )

    def compose(self) -> ComposeResult:
        yield Image(PATH_1)

    def on_mount(self) -> None:
        f0 = self.query_one(Image)
        f0.styles.width = "auto"
        f0.styles.height = "100%"

    @work(exclusive=True)
    async def watch_config(self, path) -> None:
        f0 = self.app.query_one("#data-table")
        f1 = self.app.store["7"]
        f2 = self.app.store["5"]
        f3 = path[3:-2]
        f4 = path[-2]
        f5 = path[-1]

        if self.query_one(Image):
            (self.query_one(Image).remove())

        if path[0] <= 1:
            f12 = f2.get(f4, f4)
            f13 = ",".join(str(h0) for h0 in f3)
            f14 = [h1 for h1 in f3 if h1 != ""]
            f15 = f13 if len(f14) else ","

            f16 = await (asyncio.
            create_subprocess_exec(
                "gmic",
                str(f5),
                f12,
                f15,
                "-output",
                str(PATH_4),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL,
            ))
            await f16.communicate()

            f17 = Image(PATH_4)
            f18 = self.size
            script_f4(f18, f17, PATH_4)
            await self.mount(f17)

        if path[0] == 2:
            f19 = Image(f5)
            f20 = self.size
            script_f4(f19, f20, f5)
            await self.mount(f19)

        if path[0] == 0:
            with self.app.batch_update():
                f0.clear(columns=False)
                f6 = f1.get(f"{f4}", [])
                f7 = max(len(f6), 10)

                for h in range(f7):
                    f8 = len(f6) > h
                    f9 = len(f3) > h
                    f10 = f3[h] if f9 else ""
                    f11 = f6[h] if f8 else [""]
                    f0.add_row(
                        f11[0], str(f10), ""
                    )

                f0.move_cursor(
                    row=path[1], column=path[2]
                )

    def render(self):
        return ""


class FileTree(DirectoryTree):
    show_root = False
    show_guides = True
    guide_depth = 4
    BINDINGS = [
        Binding(
            "space", "select_cursor", "Select"
        )
    ]

    def __init__(
        self, path, file_type, **kwargs
    ) -> None:
        super().__init__(path, **kwargs)
        self.file_type = file_type

    def filter_paths(self, path) -> list:
        f0 = self.file_type
        f1 = f0 == "file-2"
        f2 = (".png", ".json")
        return [
            h0
            for h0 in path
            if (
                h0.suffix.lower() in f2
                or h0.is_dir()
                or f1
            )
            and not h0.name.startswith(".")
            and not (
                h0.parent.name == "_blank"
                and f0 == "file-1"
            )
        ]

    @on(DirectoryTree.DirectorySelected)
    def select(
        self,
        event: DirectoryTree.DirectorySelected,
    ):
        f0 = self.app.query_one(MainTab)
        f1 = self.app.stores
        f2 = event.path.name
        f3 = f1["_blank"]
        if f2 == "_blank":
            f4 = [f3[3], str(PATH_1)]
            f5 = script_f6(self, *f4)
            f0.config = [2, *f5, *f4]

            f3[3] = 0 or ""
            PATH_3.write_text(json.dumps(f1))

    @on(DirectoryTree.FileSelected)
    def selected(
        self, event: DirectoryTree.FileSelected
    ):
        f0 = self.app.query_one("#data-table")
        f1 = self.app.query_one("#label-0")
        f2 = self.app.query_one(MainTab)
        f3 = f0.cursor_coordinate
        f4 = self.app.store
        f5 = self.app.stores
        f6 = event.control.id
        f7 = f6.split("-")[-1]
        f8 = f5["_blank"]
        f9 = event.path
        f10 = f9.name

        if int(f7) <= 1:
            f11 = f10.split(".")
            if f11[-1] == "png":
                f12 = 2 - f8[0] or 0
                f13 = [f8[3], str(f9)]
                f14 = script_f6(self, *f13)
                f2.config = [f12, *f14, *f13]

            elif f11[-1] == "json":
                f15 = str(PATH_1)
                f16 = f9.read_text()
                f17 = json.loads(f16)
                self.app.stores = f17
                f18 = script_f5(f15, f17)

                if f18[-2]:
                    f19 = f18[-2]
                    f2.config = f18
                    script_f7(self.app, f19)

            script_f3(self, f6, f10)
            f20 = self.app.stores
            PATH_3.write_text(json.dumps(f20))

        elif int(f7) == 2:
            f21 = f4["6"]
            f22 = f21.get(f10)
            f23 = f5.get(f8[3])
            if f22 is not None:
                f24 = [f10, f8[4]]
                f25 = len(f22) > 1
                f26 = f22[1] if f25 else ""
                f27 = script_f6(self, *f24)
                f2.config = [0, *f27, *f24]
                self.app.textfield = f26
                f1.update(f26)

            if f23 is not None:
                if len(f23) > 1:
                    f23[0] = f3.row
                    f23[1] = f3.column

            PATH_3.write_text(json.dumps(f5))
