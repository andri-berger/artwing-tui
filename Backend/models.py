from textual.widgets import (
    DataTable, Input)
from .script import (script_f1,
                     script_f0,
                     script_f2,
                     script_f9)
from .model import MainTab
from pathlib import Path
import shutil
import time
import json


PORT = Path.cwd()
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Fontend"
PORT_2 = PORT_0.parent / "Formula"
PATH_3 = PORT_2 / "za.json"
PATH_4 = PORT_2 / "za.png"


# OK !!!
def on_submitted(self, event) -> None:
    f0 = self.app.query_one(MainTab)
    f1 = self.query_one("#data-table")
    f2 = f1.cursor_coordinate
    f3 = self.app.stores
    f4 = self.app.store
    f5 = event.input
    f6 = event.value
    f7 = f4["2"]
    f5.value = ""
    f1.focus()

    f8 = f3['_blank']
    f9 = f7.get(f8[3])
    if f9 is not None:
        f11 = f2.row
        f12 = f2.column
        f13 = len(f9) > f11
        f14 = f9[f11] if f13 else []
        if len(f14) > 1 and f12 == 1:
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

# OK !!!
def on_pressed(self, event) -> None:
    f0 = self.query_one(MainTab)
    f1 = self.query_one("#data-table")
    f2 = self.query_one("#dir-tree-1")
    f3 = self.query_one("#label-0")
    f4 = self.app.store["1"]
    f5 = self.app.store["3"]
    f6 = self.app.store["4"]
    f7 = self.app.store["5"]
    f8 = f1.cursor_coordinate
    f9 = self.app.stores
    f10 = event.button.id
    f11 = f9["_blank"]
    f12 = "textual-dark"
    f13 =  f6.index(f10) \
        if f10 in f6 else -1
    f14 = f10.split("-")[-1]
    f3.update(f5[f13] or "")
    self.app.textfield = f5[f13]

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
        f23 = f22 % len(f7)
        f24 = f7[f23] or f12
        self.app.theme = f24
        script_f1(
            self, f10, f24)
        f11[2] = f23 or 0

    elif int(f14) == 4:
        f25 = f4.get(f11[3])
        if f25 is not None:
            f26 = f"{f11[3]}.png"
            f27 = PORT_1 / f25[0]
            f28 = script_f2(f27 / f26)
            shutil.copy2(PATH_4, f28)
            f29 = Path(f2.path).resolve()

            for f30 in f2.root.children:
                f31 = f30.data.path or ""
                f32 = f31.relative_to(f29)
                if f32 == Path(f25[0]):
                    f30.expand()
                    self.set_timer(
                        0.1, lambda:
                        f2.move_cursor(f30))
                    break
            f2.reload()

    elif int(f14) == 5:
        f33 = time.time()
        f34 = str(int(f33))
        f35 = f34[1:] or []
        f36 = PORT / f"{f34}.png"
        f37 = PORT / f"{f35}.json"
        shutil.copy2(PATH_3, f37)
        shutil.copy2(PATH_4, f36)

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
    f3 = self.query_one("#button-0")
    f4 = self.query_one("#button-1")
    f5 = self.query_one("#button-2")
    f6 = self.query_one("#button-3")
    f7 = self.query_one("#button-4")
    f8 = self.query_one("#button-5")
    f9 = self.query_one("#input-1")
    f10 = f2.cursor_coordinate
    f11 = f2.get_cell_at(f10)
    f12 = self.app.clipboards
    f13 = self.app.focused
    f14 = str(f11) or ""
    f15 = event.key

    if f15 in f0:
        script_f0(
            self, f15)

    match f15:
        case "delete":
            self.post_message(
                Input.Submitted(
                f9, ""))

        case "f1":
            f16 = self.app
            self.post_message(
                Input.Submitted(
                f9, f9.value))
            f16.clipboards = f14

        case "f2":
            f17 = self.app
            f17.clipboards = f14

        case "f3":
            self.post_message(
                Input.Submitted(
                f9, f12))

        case "f4": f3.press()
        case "f5": f4.press()
        case "f6": f5.press()
        case "f7": f6.press()
        case "f8": f7.press()
        case "f9": f8.press()

    # OK !!!
    if not isinstance(f13, Input):
        if f15 == "shift+tab":
            script_f9(
                self, event, -1)
        elif f15 == "tab":
            script_f9(
                self, event, 1)

    # OK !!!
    if isinstance(f13, Input):
        if f15 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(
                f9, f9.value))
        if event.key == "escape":
            f9.value = ""
            f2.focus()

    if isinstance(f13, DataTable):
        if (len(f15) == 1
                or f15 in f1):
            f9.focus()
            event.stop()

            if f15 in f1:
                f9.value = str(f14)

            elif len(f15) == 1:
                f9.value = f15
                f16 = 'cursor_position'
                self.call_after_refresh(
                    lambda: setattr(
                        f9, f16, len(f15)))
