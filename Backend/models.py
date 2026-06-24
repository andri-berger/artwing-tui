from textual.widgets import (
    DataTable, Input)
from .script import (script_f3,
                     script_f2,
                     script_f0)
from .model import MainTab, FileTree
from pathlib import Path
import shutil
import time
import json

PORT = Path.cwd()
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Fontend"
PORT_2 = PORT_0.parent / "Formula"
PORT_3 = PORT_1 / "yamljson"
PATH_3 = PORT_2 / "var.json"
PATH_4 = PORT_2 / "var.png"

def on_highlighted(self, event) -> None:
    f0 = self.query_one("#input-0")
    f1 = self.query_one("#input-1")
    f2 = self.app.store["7"]
    f3 = self.app.stores
    f1.value = ""
    f0.value = ""

    f4 = f3['_blank']
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
            f1.value = (str(f13)
                        or f12[2])

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
    f8 = f3['_blank']
    f9 = f7.get(f8[3])
    if f9 is not None:
        f11 = f2.row
        f12 = f2.column
        f13 = len(f9) > f11
        f14 = f9[f11] if f13 else []
        if len(f14) > 2 and f12 == 1:
            f5.value = f6 or f14[2]
            f0.update_cell_at(f2,f6)
            f15 = self.get_data(f0)
            f16 = sum(1 for h in f9
                       if h[0] != "")
            f17 = f16 * [""]

            for h0,h1 in f15.items():
                f18 = h1.get('0','')
                if len(f17) > int(h0):
                    f17[int(h0)] = f18

            f19 = [f11,f12,*f17]
            f20 = [1,*f19,*f8[3:]]
            f3[f8[3]] = f19 or []

            f1.config = f20
            PATH_3.write_text(
                json.dumps(f3))

def on_shift_tab(self, event, prefix) -> None:
    f0 = self.query_one("#data-table")
    f1 = self.query_one("#dir-tree-0")
    f2 = self.query_one("#button-5")
    f3 = self.query_one("#input-1")
    f4 = self.query_one("#input-0")
    f5 = self.query_one("#label-0")
    f6 = self.app.store["2"]
    f7 = self.app.store["1"]
    f8 = self.app.store["6"]
    f9 = f0.cursor_coordinate
    f10 = self.app.focused.id
    f11 = self.app.stores
    f12 = f11['_blank']
    f13 = f7.index(f10)
    f14 = f13 + prefix
    f15 = f14 % len(f7)
    f16 = min(prefix, 0)
    f17 = f13 + f16

    if f17 in (-1, 9):
        event.prevent_default()
        event.stop()

    if f15 not in (2, 3):
        f40 = self.app
        f18 = f6[f15] or ""
        f40.textfield = f18
        f5.update(f18)
        f3.value = ""
        f4.value = ""

    if f15 in (2, 3):
        f19 = f12[3]
        f20 = f8.get(f19)
        if f20 is not None:
            f21 = len(f20) > 1
            f22 = f20[1] if f21 else ""
            self.app.textfield = f22
            on_highlighted(self, f9)
            f5.update(f22)

    if f17 == 9:
        f1.focus()
    if f17 == -1:
        f2.focus()

    f12[1] = f15 or 0
    PATH_3.write_text(
        json.dumps(f11))

def on_pressed(self, event) -> None:
    f0 = self.query_one(MainTab)
    f1 = self.query_one("#data-table")
    f2 = self.query_one("#dir-tree-1")
    f3 = self.query_one("#label-0")
    f4 = self.app.store["0"]
    f5 = self.app.store["1"]
    f6 = self.app.store["2"]
    f7 = self.app.store["6"]
    f8 = f1.cursor_coordinate
    f9 = self.app.stores
    f10 = event.button.id
    f11 = f9["_blank"]
    f12 = "textual-dark"
    f13 =  f5.index(f10) \
        if f10 in f5 else -1
    f14 = f10.split("-")[-1]
    f3.update(f6[f13] or "")
    f15 = self.app

    f15.textfield = f6[f13]
    if f15.textfields is not None:
        f15.textfields.stop()
        f15.textfields = None

    if int(f14) == 0:
        f16 = [f8.row,f8.column]
        script_f3(self, f10, f11[3])
        f0.config = [0, *f16, *f11[3:]]
        f9[f11[3]] = f16

    elif int(f14) == 1:
        f17 = ["", "de"]
        f18 = f17[f11[0]]
        script_f3(
            self, f10, f18)
        f11[0] = 1 - f11[0]

    elif int(f14) in (2,3):
        f19 = 3 - int(f14)
        f20 = 1 - f19 * 2
        self.app.initial += f20
        f21 = self.app.initial
        f22 = f21 % len(f4)
        f23 = f4[f22] or f12
        self.app.theme = f23
        script_f3(
            self, f10, f23)
        f11[2] = f22 or 0

    elif int(f14) == 4:
        f24 = f7.get(f11[3])
        if f24 is not None:
            f25 = time.time()
            f26 = str(int(f25))
            f27 = f26[1:] or []
            f28 = f"{f27}.json"
            f29 = f"{f11[3]}.png"
            f30 = PORT_1 / f24[0]
            f31 = PORT_3 / f28 / ""
            f32 = script_f0(f30 / f29)
            shutil.copy2(PATH_4, f32)
            shutil.copy2(PATH_3, f31)
            f33 = Path(f2.path).resolve()

            for h in f2.root.children:
                f34 = h.data.path or ""
                f35 = f34.relative_to(f33)
                if f35 == Path(f24[0]):
                    h.expand()
                    self.set_timer(
                        0.1, lambda:
                        f2.move_cursor(h))
                    break
            f2.reload()

    elif int(f14) == 5:
        f36 = time.time()
        f37 = str(int(f36))
        f38 = f37[1:] or []
        f39 = PORT / f"{f37}.png"
        f40 = PORT / f"{f38}.json"
        shutil.copy2(PATH_3, f40)
        shutil.copy2(PATH_4, f39)

    if int(f14) in (4,5):
        script_f3(self, f10, "")

    if int(f14) in (0,1,2,3):
        PATH_3.write_text(
            json.dumps(f9))

async def on_key(self, event) -> None:
    f0 = ("delete","f1","f2","f3",
          "f4","f5","f6","f7","f8","f9")
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
    if f16 in f0:
        script_f2(
            self, f16)

    if not isinstance(f14, Input):
        if f16 == "shift+tab":
            on_shift_tab(
                self, event, -1)
        elif f16 == "tab":
            on_shift_tab(
                self, event, 1)

    if isinstance(f14, Input):
        if f16 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(
                f10, f10.value))
        if event.key == "escape":
            on_highlighted(self, f11)
            f2.focus()

    if isinstance(f14, DataTable):
        if (len(f16) == 1
                or f16 in f1):
            f10.focus()
            event.stop()

            if f16 in f1:
                f10.value = f15

            elif len(f16) == 1:
                f10.value = f16
                f17 = 'cursor_position'
                self.call_after_refresh(
                    lambda: setattr(
                        f10, f17, len(f16)))

    match f16:
        case "delete":
            if not isinstance(
                    f14, FileTree):
                self.post_message(
                    Input.Submitted(f10, ""))
            if isinstance(f14, FileTree):
                node = f3.cursor_node
                if node is not None:
                    path = node.data.path
                    paths = node.parent
                    if path.is_file():
                        self.set_timer(
                            0.1, lambda:
                            f3.move_cursor(
                                paths))
                        path.unlink()
                        f3.reload()

        case "f1":
            f17 = self.app
            f17.clipboards = f15
            self.post_message(
                Input.Submitted(
                    f10, ""))

        case "f2":
            f19 = self.app
            f19.clipboards = f15

        case "f3":
            self.post_message(
                Input.Submitted(
                f10, f13))

        case "f4": f4.press()
        case "f5": f5.press()
        case "f6": f6.press()
        case "f7": f7.press()
        case "f8": f8.press()
        case "f9": f9.press()
