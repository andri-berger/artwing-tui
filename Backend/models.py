from textual.widgets import (
    DataTable, Input)
from .script import (script_f1,
                     script_f0,
                     script_f2,
                     script_f9)
from .model import MainTab, FileTree
from pathlib import Path
import shutil
import time
import json

PORT = Path.cwd()
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Fontend"
PORT_2 = PORT_0.parent / "Formula"
PORT_3 = PORT_1 / "zarpings"
PATH_3 = PORT_2 / "za.json"
PATH_4 = PORT_2 / "za.png"

def on_submitted(self, event) -> None:
    f0 = self.app.query_one(MainTab)
    f1 = self.query_one("#data-table")
    f2 = f1.cursor_coordinate
    f3 = self.app.stores
    f4 = self.app.store
    f5 = event.input
    f6 = event.value
    f5.value = ""
    f1.focus()

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
            f1.update_cell_at(f2,f6)
            f15 = self.get_data(f1)
            f16 = sum(1 for row in f9
                       if row[0] != "")
            f17 = f16 * [""]

            for var,val in f15.items():
                f18 = val.get('0','')
                if len(f17) > int(var):
                    f17[int(var)] = f18

            f19 = [f11,f12,*f17]
            f20 = [1,*f19,*f8[3:]]
            f3[f8[3]] = f19 or []

            f0.config = f20
            PATH_3.write_text(
                json.dumps(f3))

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
    self.app.textfield = f6[f13]

    if self.app.textfields is not None:
        self.app.textfields.stop()
        self.app.textfields = None

    if int(f14) == 0:
        f17 = [f8.row,f8.column]
        script_f1(self, f10, f11[3])
        f0.config = [0, *f17, *f11[3:]]
        f9[f11[3]] = f17

    elif int(f14) == 1:
        f18 = ["", "de"]
        f19 = f18[f11[0]]
        script_f1(
            self, f10, f19)
        f11[0] = 1 - f11[0]

    elif int(f14) in (2,3):
        f20 = 3 - int(f14)
        f21 = 1 - f20 * 2
        self.app.initial += f21
        f22 = self.app.initial
        f23 = f22 % len(f4)
        f24 = f4[f23] or f12
        self.app.theme = f24
        script_f1(
            self, f10, f24)
        f11[2] = f23 or 0

    elif int(f14) == 4:
        f25 = f7.get(f11[3])
        if f25 is not None:
            f26 = time.time()
            f27 = str(int(f26))
            f28 = f27[1:] or []
            f29 = f"{f28}.json"
            f30 = f"{f11[3]}.png"
            f31 = PORT_1 / f25[0]
            f32 = PORT_3 / f29 / ""
            f33 = script_f2(f31/f30)
            shutil.copy2(PATH_4, f33)
            shutil.copy2(PATH_3, f32)
            f34 = Path(f2.path).resolve()

            for f30 in f2.root.children:
                f35 = f30.data.path or ""
                f36 = f35.relative_to(f34)
                if f36 == Path(f25[0]):
                    f30.expand()
                    self.set_timer(
                        0.1, lambda:
                        f2.move_cursor(f30))
                    break
            f2.reload()

    elif int(f14) == 5:
        f37 = time.time()
        f38 = str(int(f37))
        f39 = f38[1:] or []
        f40 = PORT / f"{f38}.png"
        f41 = PORT / f"{f39}.json"
        shutil.copy2(PATH_3, f41)
        shutil.copy2(PATH_4, f40)

    if int(f14) in (4,5):
        script_f1(self, f10, "")

    if int(f14) in (0,1,2,3):
        PATH_3.write_text(
            json.dumps(f9))

async def on_key_(self, event) -> None:
    f0 = ("delete","f1","f2","f3","f4","f5","f6",
           "f7","f8","f9","f10","f11","f12")
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
    f15 = str(f12) or ""
    f16 = event.key
    if f16 in f0:
        script_f0(
            self, f16)

    if not isinstance(f14, Input):
        if f16 == "shift+tab":
            script_f9(
                self, event, -1)
        elif f16 == "tab":
            script_f9(
                self, event, 1)

    if isinstance(f14, Input):
        if f16 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(
                f10, f10.value))
        if event.key == "escape":
            self.post_message(
                Input.Submitted(
                f10, ""))

    if isinstance(f14, DataTable):
        if (len(f16) == 1
                or f16 in f1):
            f10.focus()
            event.stop()

            if f16 in f1:
                f10.value = str(f15)

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
            self.post_message(
                Input.Submitted(
                f10, f10.value))
            f17.clipboards = f15

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
