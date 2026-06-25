from textual import events, on
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import (
    Button,
    ContentSwitcher,
    DataTable,
    DirectoryTree,
    Input,
    Label,
)

from .model import FileTree, MainTab
from .models import (
    on_highlighted,
    on_key,
    on_pressed,
    on_shift_tab,
    on_submitted,
)


class MainApp(Widget):
    def __init__(self) -> None:
        super().__init__()

    def on_mount(self) -> None:
        f0 = self.query_one("#data-table")

        f0.cursor_type = "cell"
        f0.zebra_stripes = True
        f0.fixed_columns = 1
        f0.fixed_rows = 0
        f1 = [[""]] * 10

        f0.add_column("", width=20)
        for h in range(2):
            f0.add_column("", width=10)
        f0.add_rows(f1)

    def compose(self) -> ComposeResult:
        with Horizontal(id="layer-0"):
            yield MainTab(name="")

        with Horizontal(id="layer-1"):
            with ContentSwitcher(
                id="cont-switch-0",
                initial="dir-tree-0",
            ):
                yield FileTree(
                    "/",
                    file_type="file-0",
                    id="dir-tree-0",
                )

            with ContentSwitcher(
                id="cont-switch-1",
                initial="dir-tree-1",
            ):
                yield FileTree(
                    "Fontend",
                    file_type="file-1",
                    id="dir-tree-1",
                )

            with ContentSwitcher(
                id="cont-switch-2",
                initial="dir-tree-2",
            ):
                yield FileTree(
                    "Fontend/_blank",
                    file_type="file-2",
                    id="dir-tree-2",
                )

            with ContentSwitcher(
                id="cont-switch-3",
                initial="data-table",
            ):
                yield DataTable(
                    show_header=False,
                    id="data-table",
                )

        with Horizontal(id="layer-2"):
            yield Button("X", id="button-0")
            yield Button("AS", id="button-1")
            yield Button("BSS", id="button-2")
            yield Button("CSS", id="button-3")
            yield Button("CREATE", id="button-4")
            yield Button("EXPORT", id="button-5")
            yield Input(
                disabled=False, id="input-0"
            )
            yield Input(
                disabled=False, id="input-1"
            )

        with Horizontal(id="layer-3"):
            yield Label(id="label-0")

    def get_data(self, event) -> dict:
        f0 = self.app.horizontal
        f1 = self.app.vertical

        def data(h) -> int | float | str:
            if not isinstance(h, str):
                return h
            for cast in (int, float):
                try:
                    return cast(h)
                except ValueError, TypeError:
                    pass
            return h

        return {
            str(h0): d
            for h0, h1 in enumerate(
                range(f0, len(event.rows))
            )
            if (
                d := {
                    str(h2): data(h3)
                    for h2, h3 in enumerate(
                        event.get_row_at(h1)[f1:]
                    )
                    if h3 is not None and h3 != ""
                }
            )
        }

    @on(DataTable.CellHighlighted)
    def highlighted(
        self, event: DataTable.CellHighlighted
    ):
        on_highlighted(self, event.coordinate)

    @on(Input.Submitted)  # Enter only
    def submitted(self, event: Input.Submitted):
        on_submitted(self, event)

    @on(Button.Pressed)
    def pressed(self, event: Button.Pressed):
        on_pressed(self, event)

    @on(events.Key)
    async def key(self, event: events.Key):
        await on_key(self, event)

    @on(events.Click)
    def clicked(self):
        f0 = self.app
        f1 = f0.focused
        f2 = f0.textfields
        f3 = DirectoryTree
        f4 = DataTable
        if f2 is not None:
            f0.textfields.stop()
            f0.textfields = None
        f5 = isinstance(f1, f3)
        f6 = isinstance(f1, f4)
        if f5 or f6:
            on_shift_tab(self, None, 0)
