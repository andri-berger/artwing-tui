from .models import (
    on_key_, on_pressed, on_submitted)
from textual.widgets import (
    DataTable, Input, Button,
    ContentSwitcher, Label)
from .script import script_f8
from .model import FileTree, MainTab
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widget import Widget
from textual.events import Key, Click
from textual import on, events

class MainApp(Widget):
    def __init__(self) -> None:
        super().__init__()

    def on_mount(self) -> None:
        f0 = self.query_one(
            "#data-table")

        f0.cursor_type = "cell"
        f0.zebra_stripes = True
        f0.fixed_columns = 1
        f0.fixed_rows = 0
        f1 = [[""]] * 10

        f0.add_column(
            "", width=20)
        for _ in range(2):
                f0.add_column(
                    "", width=10)
        f0.add_rows(f1)

    def compose(self) -> ComposeResult:
        with Horizontal(id="layer-0"):
            yield MainTab(name="")

        with Horizontal(id="layer-1"):
            with ContentSwitcher(
                    id="cont-switch-0",
                    initial="dir-tree-0"):
                yield FileTree(
                    "/",
                    file_type="file-0",
                    id="dir-tree-0")

            with ContentSwitcher(
                    id="cont-switch-1",
                    initial="dir-tree-1"):
                yield FileTree(
                    "Fontend",
                    file_type="file-1",
                    id="dir-tree-1")

            with ContentSwitcher(
                    id="cont-switch-2",
                    initial="dir-tree-2"):
                yield FileTree(
                    "Fontend/_blank",
                    file_type="file-2",
                    id="dir-tree-2")

            with ContentSwitcher(
                    id="cont-switch-3",
                    initial="data-table"):
                yield DataTable(
                    show_header=False,
                    id="data-table")

        with Horizontal(id="layer-2"):
            yield Button("X", id="button-0")
            yield Button("AS", id="button-1")
            yield Button("BSS", id="button-2")
            yield Button("CSS", id="button-3")
            yield Button("CREATE", id="button-4")
            yield Button("EXPORT", id="button-5")
            yield Input(disabled=False, id="input-0")
            yield Input(disabled=False, id="input-1")

        with Horizontal(id="layer-3"):
            yield Label(id="label-0")

    def get_data(self, h0) -> dict:
        f0 = self.app.horizontal
        f1 = self.app.vertical

        def data(h1) -> int | float | str:
            if not isinstance(h1, str):
                return h1
            for cast in (int,float):
                try:
                    return cast(h1)
                except (ValueError,
                        TypeError):
                    pass
            return h1

        f2 = {
            str(row_i): d
            for row_i, r in enumerate(
                range(f0, len(h0.rows)))
            if (d := {
                str(i): data(v)
                for i, v in enumerate(
                    h0.get_row_at(r)[f1:])
                if v is not None and v != ''})}
        return f2

    @on(DataTable.CellHighlighted)
    def highlighted(self, event: DataTable.CellHighlighted):
        script_f8(self, event.coordinate)

    @on(Input.Submitted) # Enter only
    def submitted(self, event: Input.Submitted):
        on_submitted(self, event)

    @on(Button.Pressed)
    def pressed(self, event: Button.Pressed):
        on_pressed(self, event)

    @on(Key)
    async def key(self, event: events.Key):
        await on_key_(self, event)

    @on(Click)
    def clicked(self):
        f0 = self.app
        f1 = f0.textfields
        if f1 is not None:
            f0.textfields.stop()
            f0.textfields = None
