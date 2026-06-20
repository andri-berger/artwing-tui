from .models import (
    on_highlighted_,
    on_key_, on_pressed,
    on_submitted)
from textual.widgets import (
    DataTable, Input, Button,
    ContentSwitcher, Label)

from .model import FileTypeTree, ImageTab
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widget import Widget
from textual.events import Key
from textual import on
from itertools import cycle
cursors = cycle(["cell"])


class NoSelectInput(Input):
    def on_focus(self):
        self.cursor_position = len(self.value)

class TableApp(Widget):
    def __init__(self) -> None:
        super().__init__()
        self.glob = 0
        self.coord = (0,0)      # braucht es das??
        self._cursor = None
        self._clipboard = None

    def on_mount(self) -> None:
        table = self.query_one("#data-table")
        rows = [[""]] * 9

        table.cursor_type = "cell"
        table.zebra_stripes = True
        table.fixed_columns = 1
        table.fixed_rows = 0
        table.add_column(
            "", width=20)
        for _ in range(9):
                table.add_column(
                    "",
                    width=9)
        table.add_rows(rows[0:])

    def compose(self) -> ComposeResult:
        with Horizontal(id="top"):
            yield ImageTab(name="")

        with Horizontal(id="bottom"):
            with ContentSwitcher(
                    initial="dir-tree-0",
                    id="cont-switch-0"):
                yield FileTypeTree(
                    "/",
                    file_type="multi",
                    id="dir-tree-0")

            with ContentSwitcher(
                    initial="dir-tree-2",
                    id="cont-switch-3"):
                yield FileTypeTree(
                    "Fontend",
                    file_type="multi",
                    id="dir-tree-2")

            with ContentSwitcher(
                    initial="dir-tree-1",
                    id="cont-switch-2"):
                yield FileTypeTree(
                    "Fontend/_blank",
                    file_type="naked",
                    id="dir-tree-1")

            with ContentSwitcher(
                    initial="data-table",
                    id="cont-switch-1"):
                yield DataTable(
                    show_header=False,
                    id="data-table")

        with Horizontal(id="status"):
            yield Button("X", id="button-0")
            yield Button("AS", id="button-1")
            yield Button("BSS", id="button-2")
            yield Button("CSS", id="button-3")
            yield Button("CREATE", id="button-4")
            yield Button("EXPORT", id="button-5")
            yield Input(disabled=False, id="input-0")
            yield Input(disabled=False, id="input-1")

        with Horizontal(id="bottoms"):
            yield Label(id="label-0")

    def get_all_data(self, table: DataTable):
        skip_rows = 0
        skip_cols = 1

        def coerce(v):
            if not isinstance(v, str):  # only convert actual strings
                return v
            for cast in (int, float):
                try:
                    return cast(v)
                except (ValueError, TypeError):
                    pass
            return v

        return {
            str(row_i): d
            for row_i, r in enumerate(range(skip_rows, len(table.rows)))
            if (d := {
                str(i): coerce(v)
                for i, v in enumerate(table.get_row_at(r)[skip_cols:])
                if v is not None and v != ''
            })
        }

    def _position_digits(self):
        x_offset = self.c_cont.region.x - self.c_digits.region.x
        y_offset = self.c_cont.region.y - self.c_digits.region.y - 3
        self.c_digits.styles.offset = (x_offset, y_offset)

    @on(DataTable.CellHighlighted)
    def highlighted(self, event: DataTable.CellHighlighted) -> None:
        on_highlighted_(self, event.coordinate)

    @on(Input.Submitted) # Enter only
    def submitted(self, event: Input.Submitted) -> None:
        on_submitted(self,event)

    @on(Button.Pressed)
    def pressed(self, event: Button.Pressed) -> None:
        on_pressed(self, event)

    @on(Key)
    async def key(self, event) -> None:
        await on_key_(self, event)
