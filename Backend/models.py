from textual.widgets import (
    DataTable, Input)
# from textual.coordinate import Coordinate
from pathlib import Path
from .script import on_message, safe_rename
from .model import ImageTab
import shutil
import time
import json


PATH = Path.cwd()
PATH_0 = Path(__file__).parent
PATH_1 = PATH_0.parent / "Fontend"
PATH_2 = PATH_0.parent / "Formula"
PATH_3 = PATH_2 / "za.json"
PATH_4 = PATH_2 / "za.png"


# tree = self.query_one(DirectoryTree)
# node = tree.cursor_node
#
# if node and node.data:
#     path = node.data.path
#     current_dir = path if path.is_dir() else path.parent

# def on_key(self, event: events.Key) -> None:
#     if event.key in ("up", "down"):
#         self.call_after_refresh(self._on_cursor_move)
#
# def _on_cursor_move(self) -> None:
#     tree = self.query_one(DirectoryTree)
#     node = tree.cursor_node
#     if node and node.data:
#         path = node.data.path
#         # do something with path







def action_next_table(self, event, prefix) -> None:
    f0 = self.query_one("#cont-switch-0")
    f1 = self.query_one("#cont-switch-1")
    f2 = self.query_one(f"#{f1.current}")
    f3 = self.query_one("#data-table")
    f4 = self.query_one("#label-0")
    f5 = self.query_one("#input-0")
    f6 = self.query_one("#input-1")
    f7 = self.app.store["3"]
    f8 = self.app.store["4"]
    f9 = self.app.store["1"]
    f10 = self.app.focused.id
    f11 = self.app.stores
    f12 = f11['_blank']
    f13 = f8.index(f10)
    f14 = f13 + prefix
    f15 = f14 % len(f8)
    f17 = min(prefix,0)
    f12[1] = f15 or 0
    PATH_3.write_text(
        json.dumps(f11))
    self.notify(f"... {self.coord} {f15}")

    # if self.coord is not None:
    #     event.prevent_default()
    #     event.stop()
    #     f2.focus()

    if self.coord is None:
        if ((f13 + f17) in [-1,9]):
            event.prevent_default()
            event.stop()

        if f15 in [0,1,2,3,4,5,6,7,8,9]:
            self.app.clear_notifications()
            self.app.textfield = f7[f15] or ""
            f4.update(f7[f15] or "")
            f6.value = ""
            f5.value = ""

        if f15 in [3]:
            coordinates = f3.cursor_coordinate
            on_highlighted_(self,coordinates)
            yes = f9.get(f12[2],[])
            yes0 = yes[2] if len(yes) > 2 else ""
            self.app.textfield = yes0
            f4.update(yes0)

        if (f13 + f17) == 9:
            sr = f"#{f0.current}"
            self.query_one(sr).focus()

        if (f13 + f17) == -1:
            sr = "#button-5"
            self.query_one(sr).focus()


async def on_key_(self, event) -> None:
    f0 = ["backspace", "space", "enter"]
    f1 = self.query_one("#cont-switch-0")
    f2 = self.query_one("#cont-switch-1")
    f3 = self.query_one(f"#{f2.current}")
    f4 = f2.current.split("-")[-1]
    f5 = self.query_one("#input-1")
    f6 = f3.cursor_coordinate
    f7 = f3.get_cell_at(f6) or ""
    f8 = event.key

    match f8:
        case "delete":
            self.coord = f6
            on_message(self, f7, "f1")
            self.post_message(Input.Submitted(
                f5, ""))

        case "f1":
            self.coord = f6
            self._clipboard = str(f7)
            on_message(self, f7, "f2")
            self.post_message(Input.Submitted(
                f5, f5.value))

        case "f2":
            self._clipboard = str(f7)
            on_message(self, f7, "f3")

        case "f3":
            self.coord = f6
            clipboard = self._clipboard
            on_message(self, clipboard, "f4")
            self.post_message(Input.Submitted(
                f5, clipboard))

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
                "#button-6").press()

        case "f8":
            self.query_one(
                "#button-3").press()

        case "f9":
            self.query_one(
                "#button-4").press()

        case "f10":
            self.notify("fullscreen coming soon, stay tuned")

        case "f11":
            self.notify("fullscreen coming soon, stay tuned")

        case "f12":
            self.notify("fullscreen coming soon, stay tuned")

    # if isinstance(self.app.focused, DirectoryTree):
    #     if f8 == "space":
    #         event.stop()
    #         tree = self.query_one(DirectoryTree)
    #         node = tree.cursor_node
    #         if (node and node.data
    #                 and node.data.path.is_file()):
    #             self.notify("space pressed")
    #             self.post_message(
    #                 DirectoryTree.FileSelected(tree, node))

    if not isinstance(self.app.focused, Input):
        if f8 == "shift+tab":
            action_next_table(self, event, -1)
            self.coord = None
        elif f8 == "tab":
            action_next_table(self, event, 1)
            self.coord = None

    if isinstance(self.app.focused, Input):
        if f8 == "tab":
            event.stop()
            event.prevent_default()
            f4 = self.query_one("#input-1")
            self.post_message(Input.Submitted(
                f4, f4.value))
        if event.key == "escape":
            self.coord = None
            f5.value = ""
            f3.focus()

    if isinstance(self.app.focused, DataTable):
        if (len(f8) == 1 or f8 in f0):
            self.coord = f6
            f5.focus()
            event.stop()

            if f8 in f0:
                f5.value = str(f7)

            elif len(f8) == 1:
                f5.value = f8

                def after_focus():
                    f5.cursor_position = len(f8)
                self.call_after_refresh(after_focus)

def on_highlighted_(self, coordinate) -> None:
    f0 = self.query_one("#input-0")
    f1 = self.query_one("#input-1")
    f2 = self.app.store["2"]
    f3 = self.app.stores
    f4 = f3['_blank'][3]
    f5 = [""] * 10
    f6,f7 = coordinate
    f8 = f2.get(f4,f5)
    f1.value = ""
    f0.value = ""

    try:
        value = f8[f6] if len(f8) > f6 else f5
        if value is not None and f7 <= 1:
            f0.value = value[1]
            f1.value = value[2]

    except IndexError:
        pass


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
        f15 = [f10[3], f10[4]]
        f16 = f1.cursor_coordinate
        f17 = [f16.row,f16.column]
        on_message(self, f9, f10[3])
        f0.config = [0, *f17, *f15]
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
            f27 = PATH_1 / f25[0]
            f28 = safe_rename(f27/f26)
            self.notify(f"ooo {f28}")
            shutil.copy2(PATH_4, f28)
            f29 = Path(f2.path).resolve()

            for f30 in f2.root.children:
                f31 = f30.data.path or ""
                f32 = f31.relative_to(f29)
                if f32 == Path(f25[0]):
                    f30.expand()
                    break
            f2.reload()

    elif int(f14) == 5:
        fx66 = time.time()
        fx12 = str(int(fx66))
        fx13 = PATH / f"{fx12}.png"
        fx14 = PATH / f"{fx12[1:]}.json"
        shutil.copy2(PATH_3, fx14)
        shutil.copy2(PATH_4, fx13)
        on_message(self, "", "f10")

    if int(f14) in (0,1,2,3):
        PATH_3.write_text(
            json.dumps(f8))



def on_submitted(self, event) -> None:
    f93 = self.app.query_one(ImageTab)
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.app.store["2"]
    f03 = self.app.store["0"]
    f3 = self.app.stores
    f4 = f3['_blank'][4]
    f05 = f3['_blank'][3]
    f5 = f03.get(f05, f05)

    f6 = f2[f5] or []
    f7 = event.value
    f8 = self.coord
    f08 = f8.column
    f09 = f8.row

    f9 = f6[f8.row] or []
    if f9[0] and f8.column == 1:
        f1.update_cell_at(f8,f7)
        f10 = self.get_all_data(f1)
        test = sum(1 for row in f6
                   if row[0] != "")
        f11 = [""] * test

        for var,val in f10.items():
            test = val.get('0','')
            if len(f11) > int(var):
                f11[int(var)] = test

        f12 = [f09,f08,*f11]
        f3[f05] = f12 or []
        f13 = [1,*f12,f05,f4]
        f93.config = f13
        event.input.value = ""
        self.coord = None
        f1.focus()

        PATH_3.write_text(
            json.dumps(f3))

