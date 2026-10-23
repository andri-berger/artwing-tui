import json
import shutil
import time
from pathlib import Path

from textual.widgets import DataTable, Input

from .model import FileTree, MainTab
from .script import (
    PATH_01,
    PORT_00,
    script_f0,
    script_f01,
    script_f2,
    script_f3,
    script_f9,
)

PORT_0 = script_f01()
PORT_3 = PORT_0 / "yamljson"



def on_highlighted(self, event) -> None:
    f0 = self.query_one("#input-0")
    f1 = self.query_one("#input-1")
    f2 = self.app.store["7"]
    f3 = self.app.stores
    f1.value = ""
    f0.value = ""

    f4 = f3["_blank"]
    f5 = f3.get(f4[3])
    f6 = f2.get(f4[3])
    if f6 is not None:
        f7 = f5 or []
        f8 = event.row
        f9 = event.column
        f10 = len(f6) > f8
        f11 = len(f7[2:]) > f8
        f12 = f6[f8] if f10 else []
        f13 = f7[2:][f8] if f11 else ""
        if len(f12) > 2 and f9 <= 1:
            f0.value = f12[1] or ""
            f1.value = str(f13) or f12[2]


def on_submitted(self, event) -> None:
    f0 = self.query_one("#data-table")
    f1 = self.query_one(MainTab)
    f2 = f0.cursor_coordinate
    f3 = self.app.stores
    f4 = self.app.store
    f6 = event.value
    f5 = event.input
    f5.value = ""
    f0.focus()

    f7 = f4["7"]
    f8 = f3["_blank"]
    f9 = f7.get(f8[3])
    if f9 is not None:
        f11 = f2.row
        f12 = f2.column
        f13 = len(f9) > f11
        f14 = f9[f11] if f13 else []
        if len(f14) > 2 and f12 == 1:
            f5.value = f6 or f14[2]
            f0.update_cell_at(f2, f6)
            f15 = self.get_data(f0)
            f16 = sum(1 for h in f9 if h[0] != "")
            f17 = f16 * [""]

            for h0, h1 in f15.items():
                f18 = h1.get("0", "")
                if len(f17) > int(h0):
                    f17[int(h0)] = f18

            f19 = [f11, f12, *f17]
            f20 = [1, *f19, *f8[3:]]
            f3[f8[3]] = f19 or []

            f1.config = f20
            script_f9(f3)


def on_shift_tab(self, event, prefix) -> None:
    f0 = self.query_one("#data-table")
    f1 = self.query_one("#dir-tree-0")
    f2 = self.query_one("#button-5")
    f3 = self.query_one("#input-1")
    f4 = self.query_one("#input-0")
    f5 = self.query_one("#label-0")
    f6 = self.app.store["0"]
    f7 = self.app.store["2"]
    f8 = self.app.store["6"]
    f9 = f0.cursor_coordinate
    f10 = self.app.focused.id
    f11 = self.app.stores
    f12 = f11["_blank"]
    f13 = f6.index(f10)
    f14 = f13 + prefix
    f15 = f14 % len(f6)
    f16 = min(prefix, 0)
    f17 = f13 + f16

    if f17 in (-1, 9):
        event.prevent_default()
        event.stop()

    if f15 not in (2, 3):
        f20 = f6[f15] or ""
        f21 = f7.get(f20, "")
        f5.update(f21)
        f3.value = ""
        f4.value = ""

    if f15 in (2, 3):
        f22 = f12[3]
        f23 = f8.get(f22)
        if f23 is not None:
            f21 = len(f23) > 1
            f22 = f23[1] if f21 else ""
            on_highlighted(self, f9)
            f5.update(f22)

    if f17 == 9:
        f1.focus()
    if f17 == -1:
        f2.focus()

    f12[1] = f15 + 1
    script_f9(f11)


def on_pressed(self, event) -> None:
    f0 = self.query_one(MainTab)
    f1 = self.query_one("#data-table")
    f2 = self.query_one("#dir-tree-1")
    f3 = self.query_one("#label-0")
    f4 = self.app.store["1"]
    f5 = self.app.store["2"]
    f6 = self.app.store["6"]
    f7 = f1.cursor_coordinate
    f8 = event.button.id
    f9 = self.app.stores
    f11 = f9["_blank"]
    f12 = f5.get(f8, "")
    f13 = f8.split("-")
    f14 = f13[-1] or 0
    f15 = str(event.button.label)

    f3.update(f12)

    # only a finished render is saved, never
    # an older one while gmic runs or failed
    f34 = f0.rendered
    if int(f14) in (4, 5) and f34 is None:
        self.app.notify(
            "NOTHING SAVED, the image is still"
            " rendering or its effect failed",
            severity="warning",
        )

    # X: nothing to clear without an effect
    if int(f14) == 0 and f11[3]:
        f16 = [f7.row, f7.column]
        script_f3(self, f8, f11[3], f15)
        f0.config = [0, *f16, *f11[3:]]
        f9[f11[3]] = f16

    elif int(f14) == 1:
        # AS on (1) opts out of reapplying
        f17 = ["de", ""]
        f18 = f17[f11[0]]
        script_f3(self, f8, f18, f15)
        f11[0] = 1 - f11[0]

    elif int(f14) in (2, 3) and f4:
        # BSS steps back, CSS forward
        f20 = -1 if int(f14) == 2 else 1
        f22 = (self.app.initial + f20) % len(f4)
        f23 = f4[f22]
        self.app.initial = f22
        self.app.theme = f23
        script_f3(self, f8, f23, f15)
        # by name, a reordered theme list
        # still restores the same theme
        f11[2] = f23

    elif int(f14) == 4 and f34:
        # an effect goes to its category, a raw
        # image to the root, named after it;
        # the json is named after the png
        f24 = f6.get(f34[0])
        f25 = f34[0] or Path(f34[1]).stem
        f30 = PORT_0 / f24[0] if f24 else PORT_0
        f32, f31 = script_f0(
            f30 / f"{f25}.png",
            PORT_3 / f"{f25}.json",
        )
        f32.parent.mkdir(exist_ok=True)
        f31.parent.mkdir(exist_ok=True)
        shutil.copy2(PATH_01, f32)
        f31.write_text(json.dumps(f9))
        # cursor on the new png, so it can be
        # picked as the next source right away
        f2.reveal(f32)
        script_f3(self, f8, "", f15)

    elif int(f14) == 5 and f34:
        # png and json share one timestamp,
        # the next free one
        f36 = int(time.time())
        while any(
            h.exists()
            for h in (
                PORT_00 / f"{f36}.png",
                PORT_00 / f"{str(f36)[1:]}.json",
            )
        ):
            f36 += 1
        f37 = str(f36)
        f39 = PORT_00 / f"{f37}.png"
        f40 = PORT_00 / f"{f37[1:]}.json"
        f40.write_text(json.dumps(f9))
        shutil.copy2(PATH_01, f39)
        script_f3(self, f8, "", f15)

    if int(f14) in (0, 1, 2, 3):
        script_f9(f9)


def on_files(self, h, h0) -> None:
    # F1 cuts, F2 copies a file of the left
    # or middle tree, F3 pastes it into the
    # middle tree next to the cursor
    f0 = self.query_one("#dir-tree-1")
    f1 = h0.cursor_node
    f2 = f1.data.path if f1 and f1.data else None
    f7 = self.app.notify

    if h in ("f1", "f2"):
        if h0.id == "dir-tree-2":
            return
        if f2 is None or not f2.is_file():
            return
        self.app.files = [f2, h == "f1"]
        f8 = "CUT" if h == "f1" else "COPIED"
        f7(f"FILE {f2.name.upper()} {f8}!")
        return

    if h0 is not f0 or not self.app.files:
        return
    f3, f4 = self.app.files
    f5 = Path(f0.path)
    if f2 is not None:
        f5 = f2 if f2.is_dir() else f2.parent
    # _blank is wiped at every start
    if f5.name == "_blank":
        f5 = Path(f0.path)
    if not f3.is_file():
        self.app.files = []
        f7(
            f"{f3.name}: no longer there",
            severity="warning",
        )
        return
    if f4 and f3.parent == f5:
        return
    (f6,) = script_f0(f5 / f3.name)
    if f4:
        shutil.move(f3, f6)
        self.app.files = []
    else:
        shutil.copy2(f3, f6)
    f7(f"FILE {f6.name.upper()} PASTED!")
    f0.reveal(f6)
    # a cut from the left tree leaves a gap
    if f4:
        self.query_one("#dir-tree-0").reload()


async def on_key(self, event) -> None:
    f0 = (
        "delete",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
    )
    f1 = ("backspace", "space", "enter")
    f2 = self.query_one("#data-table")
    f3 = self.query_one("#dir-tree-1")
    f4 = self.query_one("#button-0")
    f5 = self.query_one("#button-1")
    f6 = self.query_one("#button-2")
    f7 = self.query_one("#button-3")
    f8 = self.query_one("#button-4")
    f9 = self.query_one("#button-5")
    f10 = self.query_one("#input-1")
    f11 = f2.cursor_coordinate
    f12 = f2.get_cell_at(f11)
    f13 = self.app.clipboards
    f14 = self.app.focused
    f15 = str(f12 or "")
    f16 = event.key
    # in a file tree F1-F3 act on files,
    # never on the table
    if isinstance(f14, FileTree):
        if f16 in ("f1", "f2", "f3"):
            on_files(self, f16, f14)
            return

    if f16 in f0:
        script_f2(self, f16)

    if not isinstance(f14, Input):
        if f16 == "shift+tab":
            on_shift_tab(self, event, -1)
        elif f16 == "tab":
            on_shift_tab(self, event, 1)

    if isinstance(f14, Input):
        if f16 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(f10, f10.value)
            )
        if event.key == "escape":
            on_highlighted(self, f11)
            f2.focus()

    if isinstance(f14, DataTable):
        if len(f16) == 1 or f16 in f1:
            f10.focus()
            event.stop()

            if f16 in f1:
                f10.value = f15

            elif len(f16) == 1:
                f10.value = f16
                f17 = "cursor_position"
                self.call_after_refresh(
                    lambda: setattr(
                        f10, f17, len(f16)
                    )
                )

    match f16:
        case "delete":
            if not isinstance(f14, FileTree):
                self.post_message(
                    Input.Submitted(f10, "")
                )
            if f14 is f3:
                node = f3.cursor_node
                if node is not None:
                    path = node.data.path
                    paths = node.parent
                    if path.is_file():
                        self.set_timer(
                            0.1,
                            lambda: (
                                f3.move_cursor(
                                    paths
                                )
                            ),
                        )
                        path.unlink()
                        f3.reload()

        # F1 cuts (clears the cell), F2 copies,
        # in the order of the button row
        case "f1":
            f17 = self.app
            f17.clipboards = f15
            self.post_message(
                Input.Submitted(f10, "")
            )

        case "f2":
            f19 = self.app
            f19.clipboards = f15

        case "f3":
            self.post_message(
                Input.Submitted(f10, f13)
            )

        case "f4":
            f4.press()
        case "f5":
            f5.press()
        case "f6":
            f6.press()
        case "f7":
            f7.press()
        case "f8":
            f8.press()
        case "f9":
            f9.press()
