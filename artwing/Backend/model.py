import asyncio
from pathlib import Path

from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DirectoryTree, Input
from textual_image.widget import Image

from .script import (
    FORMATS,
    PATH_01,
    PATH_03,
    script_f3,
    script_f4,
    script_f5,
    script_f6,
    script_f7,
    script_f8,
    script_f9,
    script_f12,
    script_f13,
)

PORT_1 = Path(__file__)
PORT_2 = PORT_1.parent.parent
PATH_3 = PORT_2 / "build.png"



class MainTab(Widget):
    config: reactive[dict] = reactive(
        dict, init=False
    )
    # what PATH_01 holds: [effect, image],
    # effect "" for raw; None while a render
    # runs or after it failed
    rendered = None

    def compose(self) -> ComposeResult:
        # a restored image follows right after
        # startup, no fallback image before it
        if not self.app.restored[-1]:
            yield Image(PATH_3)

    def on_mount(self) -> None:
        for f0 in self.query(Image):
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
        f12 = Path(f5).name
        f19 = None
        f23 = None
        self.rendered = None

        if path[0] <= 1:
            f13 = ",".join(str(h0) for h0 in f3)
            f14 = [h1 for h1 in f3 if h1 != ""]
            f15 = f13 if len(f14) else ","
            # only listed effects and plain values
            # reach gmic, a loaded json could hold
            # commands (exec) or {..}/$ expansions
            f24 = set(f13) & set("{}$")
            if f4 in f1 and not f24:
                f12 = f2.get(f4, f4)
                f19 = [f12, f15]
            else:
                self.app.notify(
                    f"{f4}: not allowed",
                    severity="error",
                )

        # the raw view (2) runs gmic without
        # an effect, so CREATE and EXPORT
        # save the image that is shown
        if path[0] == 2:
            f19 = []

        # an effect clears the preview at once,
        # its result shows when gmic is done,
        # never a stale image before it
        if f19:
            await self.query(Image).remove()

        if f19 is not None:
            f16 = await asyncio.create_subprocess_exec(
                "gmic",
                str(script_f13(f5)),
                # gif/tiff can hold several
                # frames, use the first only
                "-keep[0]",
                *f19,
                "-output",
                str(PATH_03),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.PIPE,
            )
            try:
                f21 = await f16.communicate()
            except asyncio.CancelledError:
                # a newer call replaced this
                # worker, stop gmic so it can't
                # overwrite the newer result
                f16.kill()
                raise
            if f16.returncode:
                f22 = script_f8(f21[1])
                self.app.notify(
                    f"gmic {f12}: {f22}",
                    severity="error",
                )
                # show the base image, the old
                # output must not pose as new
                f23 = f5
            else:
                PATH_03.replace(PATH_01)
                f28 = f4 if path[0] <= 1 else ""
                self.rendered = [f28, f5]
                if path[0] <= 1:
                    f23 = PATH_01

        if path[0] == 2:
            f23 = f5

        # swap in the new image once gmic is
        # done, a raw view keeps the old till then
        if f23 is not None:
            try:
                f17 = Image(f23)
                f18 = self.size
                script_f4(f18, f17, f23)
            except OSError:
                self.app.notify(
                    f"{Path(f23).name}: no image",
                    severity="error",
                )
            else:
                await self.query(Image).remove()
                await self.mount(f17)

        # a failed effect or restore shows the
        # fallback image instead of nothing
        if not self.query(Image):
            f20 = Image(PATH_3)
            f20.styles.width = "auto"
            f20.styles.height = "100%"
            await self.mount(f20)

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
        f2 = (*FORMATS, ".json")
        return [
            h0
            for h0 in path
            if (
                h0.suffix.lower() in f2
                or self._safe_is_dir(h0)
                or f1
            )
            and not h0.name.startswith(".")
            and not (
                h0.parent.name == "_blank"
                and f0 == "file-1"
            )
        ]

    @work(exclusive=True, group="reveal")
    async def reveal(self, path) -> None:
        # open the tree down to the last used
        # file, using only public reloads
        f0 = Path(path)
        f4 = Path(self.path)
        if not f0.is_file():
            return
        await self.reload()
        f1 = self.root
        # walk down from this tree's own root
        f2 = [
            *(
                h for h in reversed(f0.parents)
                if f4 in h.parents
            ),
            f0,
        ]
        for h0 in f2:
            f3 = next(
                (
                    h1
                    for h1 in f1.children
                    if h1.data.path == h0
                ),
                None,
            )
            if f3 is None:
                break
            f1 = f3
            if h0 != f0:
                await self.reload_node(f1)
        # reading last_line lays out the tree,
        # so the node knows its line
        f5 = f1 is not self.root
        if self.last_line >= 0 and f5:
            self.move_cursor(f1, animate=False)

    @on(DirectoryTree.DirectorySelected)
    def select(
        self,
        event: DirectoryTree.DirectorySelected,
    ):
        f0 = self.app.query_one(MainTab)
        f1 = self.app.stores
        f2 = event.path
        f3 = f1["_blank"]
        f6 = self.file_type
        # only the _blank folders at the top of
        # the 2nd and 3rd picker, not any folder
        # of that name on disk
        f7 = f2.parent == Path(self.path)
        if f2.name != "_blank" or not f7:
            return
        if f6 == "file-0":
            return
        # picker 2: back to the blank canvas,
        # picker 3: no effect on the image shown
        f4 = f3[4] if f6 == "file-2" else ""
        f5 = f4 or str(PATH_3)
        f0.config = [2, 0, 0, "", f5]
        f3[3] = ""
        f3[4] = f5
        script_f9(f1)

        # nothing left of the old effect
        f8 = self.app.query_one("#data-table")
        f9 = self.app.query_one("#label-0")
        f10 = self.app.store["2"]
        f8.clear(columns=False)
        f8.add_rows([[""]] * 10)
        f9.update(f10.get(self.id, ""))
        for h in self.app.query(Input):
            h.value = ""

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
            f11 = f9.suffix.lower()
            if f11 in FORMATS:
                # an active effect is reapplied to
                # the new image unless AS opted out
                f28 = f8[3] in f4["7"] and not f8[0]
                f12 = 1 if f28 else 2
                f13 = [f8[3], str(f9)]
                f14 = script_f6(self, *f13)
                f2.config = [f12, *f14, *f13]

            elif f11 == ".json":
                f15 = str(PATH_3)
                f17 = script_f12(f9)
                if f17 is None:
                    self.app.notify(
                        f"{f10}: no artwing file",
                        severity="error",
                    )
                    return
                self.app.stores = f17
                f18 = script_f5(f15, f17)

                if f18[-1]:
                    f2.config = f18
                if f18[-2]:
                    script_f7(self.app, f18[-2])

            script_f3(self.app, f6, f10)
            f20 = self.app.stores
            script_f9(f20)

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
                f1.update(f26)

            if f23 is not None:
                if len(f23) > 1:
                    f23[0] = f3.row
                    f23[1] = f3.column

            script_f9(f5)
