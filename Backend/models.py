from textual.widgets import (
    DataTable, Input)
from .script import on_message, safe_rename, action_next_table
from .model import ImageTab
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
    f0 = self.app.query_one(ImageTab)
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
            f15 = self.get_all_data(f1)
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
    f0 = self.query_one(ImageTab)
    f1 = self.query_one("#data-table")
    f2 = self.query_one("#dir-tree-2")
    f3 = self.query_one("#label-0")
    f4 = self.app.store["1"]
    f5 = self.app.store["3"]
    f6 = self.app.store["4"]
    f7 = self.app.store["5"]
    f8 = self.app.stores
    f9 = event.button.id
    f10 = f8["_blank"]
    f12 = "textual-dark"
    f13 =  f6.index(f9) \
        if f9 in f6 else -1
    f14 = f9.split("-")[-1]
    f3.update(f5[f13] or "")
    self.app.textfield = f5[f13]

    if self.app.textfields is not None:
        self.app.textfields.stop()
        self.app.textfields = None

    if int(f14) == 0:
        f16 = f1.cursor_coordinate
        f17 = [f16.row,f16.column]
        on_message(self, f9, f10[3])
        f0.config = [0, *f17, *f10[3:]]
        f8[f10[3]] = f17

    elif int(f14) == 1:
        f18 = ["", "de"]
        f19 = f18[f10[0]]
        on_message(
            self, f9, f19)
        f10[0] = 1 - f10[0]

    elif int(f14) in (2,3):
        f20 = 3 - int(f14)
        f21 = 1 - f20 * 2
        self.app.initial += f21
        f22 = self.app.initial
        f23 = f22 % len(f7)
        f24 = f7[f23] or f12
        self.app.theme = f24
        on_message(
            self, f9, f24)
        f10[2] = f23 or 0

    elif int(f14) == 4:
        f25 = f4.get(f10[3],[])
        if f25[0] is not None:
            f26 = f"{f10[3]}.png"
            f27 = PORT_1 / f25[0]
            f28 = safe_rename(f27/f26)
            self.notify(f"ooo {f28}")
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
        on_message(self, f9, "")

    if int(f14) in (0,1,2,3):
        PATH_3.write_text(
            json.dumps(f8))


async def on_key_(self, event) -> None:
    f0 = ["backspace", "space", "enter"]
    f1 = self.query_one("#data-table")
    f2 = self.query_one("#input-1")
    f3 = f1.cursor_coordinate
    f4 = f1.get_cell_at(f3)
    f04 = self.app.focused
    f5 = event.key
    f6 = f4 or ""

    match f5:
        case "delete":
            # self.coord = f3
            on_message(self, f6, "f1")
            self.post_message(
                Input.Submitted(
                f2, ""))

        case "f1":
            # self.coord = f3
            self._clipboard = str(f6)
            on_message(self, f6, "f2")
            self.post_message(
                Input.Submitted(
                f2, f2.value))

        case "f2":
            self._clipboard = str(f6)
            on_message(self, f6, "f3")

        case "f3":
            # self.coord = f3
            clipboard = self._clipboard
            on_message(self, clipboard, "f4")
            self.post_message(
                Input.Submitted(
                f2, clipboard))

        case "f4":
            self.query_one(
                "#button-0").press()

        case "f5":
            self.query_one(
                "#button-1").press()

        case "f6":
            self.query_one(
                "#button-2").press()

        case "f7":
            self.query_one(
                "#button-3").press()

        case "f8":
            self.query_one(
                "#button-4").press()

        case "f9":
            self.query_one(
                "#button-5").press()

        case "f10":
            self.notify("fullscreen coming soon, stay tuned")

        case "f11":
            self.notify("fullscreen coming soon, stay tuned")

        case "f12":
            self.notify("fullscreen coming soon, stay tuned")

    # if isinstance(self.app.focused, DirectoryTree):
    #     if f8 == "space":
    #         h0.stop()
    #         tree = self.query_one(DirectoryTree)
    #         node = tree.cursor_node
    #         if (node and node.data
    #                 and node.data.path.is_file()):
    #             self.notify("space pressed")
    #             self.post_message(
    #                 DirectoryTree.FileSelected(tree, node))

    if not isinstance(f04, Input):
        if f5 == "shift+tab":
            action_next_table(self, event, -1)
            # self.coord = None
        elif f5 == "tab":
            action_next_table(self, event, 1)

    # OK !!!
    if isinstance(f04, Input):
        if f5 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(
                f2, f2.value))
        if event.key == "escape":
            f2.value = ""
            f1.focus()

    # OK !!!
    if isinstance(f04, DataTable):
        if (len(f5) == 1
                or f5 in f0):
            f2.focus()
            event.stop()

            if f5 in f0:
                f2.value = str(f6)

            elif len(f5) == 1:
                f2.value = f5

                def after_focus():
                    f2.cursor_position = len(f5)
                self.call_after_refresh(after_focus)
