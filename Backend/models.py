from textual.widgets import (
    DataTable, Input, DirectoryTree)
# from textual.coordinate import Coordinate
from pathlib import Path
import imagesize
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

def tester(self, param, params) -> list:
    f0 = self.app.store["2"]
    f1 = self.app.stores
    f2 = f0.get(param,[])
    f3 = sum(1 for row in f2
             if row[0] != "")
    f4 = [0, 0, *[""] * f3]
    f5 = f1.get(param,f4)
    f6 = f1["_blank"]
    f6[4] = params
    f6[3] = param
    f1[param] = f5
    return f5



def testlauf(yes, size, IMAGES):
    cell_w, cell_h = 9, 18
    target_w = size.width * cell_w
    target_h = size.height * cell_h
    container_ratio = target_w / target_h
    width, height = imagesize.get(str(IMAGES))
    img_ratio = width / height

    if img_ratio > container_ratio:
        yes.styles.width = "100%"
        yes.styles.height = "auto"
    else:
        yes.styles.width = "auto"
        yes.styles.height = "100%"

def safe_rename(dst: Path) -> Path:
    count = len(list(dst.parent.glob(f"{dst.stem}*{dst.suffix}")))
    new_dst = dst.with_stem(f"{dst.stem}_{count-1}") if count > 0 else dst
    return new_dst

def on_message(self,value,hash) -> None:
    self.app.clear_notifications()
    test = {
        "f0": f"Image on path {value} has been chosen for canvas, congrats, good choice!",
        "f1": f"(f1) {value} deleted from table",
        "f2": f"(f2) {value} cut to clipboard",
        "f3": f"(f3) {value} copied to clipboard",
        "f4": f"(f4) {value} pasted from clipboard",
        "f5": f"(f5) {value} Clear Canvas",
        "f6": f"(f6) {value} B00 Seed",
        "f7": f"(f7) {value} C0 Seed",
        "f8": f"(f8) {value} C0 Seed",
        "f9": f"(f9) {value} Regenerate Art",
        "f10": f"(f10) {value} Export to Disk"}
    self.notify(
        test.get(
            hash, ""))

def action_next_table(self, event, prefix) -> None:
    f0 = self.query_one("#cont-switch-0")
    f1 = self.query_one("#cont-switch-1")
    f2 = self.query_one(f"#{f1.current}")
    f3 = self.query_one(DataTable)
    f4 = self.query_one("#label-0")
    f5 = self.query_one("#fourth")
    f6 = self.query_one("#third")
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
    f16 = f8[f15]

    if self.coord is not None:
        event.prevent_default()
        event.stop()
        f2.focus()

    if self.coord is None:
        if ((f13 + f17) in [-1,9]):
            event.prevent_default()
            event.stop()

        if f15 in [0,1,2,3,4,5,6,7,8,9]:
            self.app.clear_notifications()
            f4.update(f7[f15] or "")
            f6.value = ""
            f5.value = ""

        if f15 in [3]:
            coordinates = f3.cursor_coordinate
            on_highlighted_(self,coordinates)
            yes = f9.get(f12[2],[])
            yes0 = yes[2] if len(yes) > 2 else ""
            f4.update(yes0)

        if f15 in [0,1,2]:
            tree = self.query_one(f"#{f16}")
            tree.reload()

        if (f13 + f17) == 9:
            sr = f"#{f0.current}"
            self.query_one(sr).focus()

        if (f13 + f17) == -1:
            sr = "#button-4"
            self.query_one(sr).focus()


async def on_key_(self, event) -> None:
    f0 = ["backspace", "space", "enter"]
    f1 = self.query_one("#cont-switch-0")
    f2 = self.query_one("#cont-switch-1")
    f3 = self.query_one(f"#{f2.current}")
    f4 = f2.current.split("-")[-1]
    f5 = self.query_one("#third")
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
            f4 = self.query_one("#third")
            self.post_message(Input.Submitted(
                f4, f4.value))
        if event.key == "escape":
            self.coord = None
            f5.value = ""
            f3.focus()

    if isinstance(self.app.focused, DataTable):
        if (len(f8) == 1 or f8 in f0):
            self.coord = f6

            if (int(f4) in [4,5]
                    and f6.column == 12):
                sarin = int(f4) - 3
                sar = f"dir-tree-{sarin}"
                self.query_one(f"#{sar}").focus()
                f1.current = sar
                event.stop()

            else:
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
    f0 = self.query_one("#fourth")
    f1 = self.query_one("#third")
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
    f01 = ['activated', 'deactivated']
    f00 = self.query_one("#dir-tree-2")
    f02 = self.query_one("#label-0")
    f0 = self.app.store
    f1 = self.app.stores
    f2 = event.button.id
    f03 = f1['_blank']
    f3 = f1['_blank'][3]
    f09 = f1['_blank'][4]
    f4 = f2.split("-")[-1]
    f5 =  f0["4"].index(f2) \
        if f2 in f0["4"] else -1
    f6 = f0["3"][f5]
    f02.update(f6)


    if f2 == "button-6":
        f1.pop(f3, None)
        f16 = tester(self, f3, f09)
        f06 = [0, *f16, f3, f09]
        self.e_images.config = f06
        on_message(self,"", "f5")

    elif f2 == "button-0":
        f03[0] = 1 - f03[0]
        on_message(self,f2,"f6")

    elif f2 == "button-1":
        f03[1] = 1 - f03[1]
        on_message(self,f2,"f7")

    elif f2 == "button-2":
        f03[2] = 1 - f03[2]
        on_message(self,f2,"f8")

    elif f2 == "button-3":
        toast = f0["1"].get(
            f3,["",""])
        node = f02.cursor_node
        news = node.data.path
        if toast[1]:
            f07 = PATH_1
            f08 = f07 / toast[1]
            f7 = f08 / news.name
            f8 = safe_rename(f7)
            shutil.copy2(PATH_4, f8)
            f9 = Path(f00.path).resolve()

            for node in f00.root.children:
                f10 = node.data.path
                f11 = f10.relative_to(f9)
                if f11 == Path(toast[1]):
                    node.expand()
                    break
            f00.reload()

    elif f2 == "button-4":
        f12 = str(int(time.time()))
        f13 = PATH / f"{f12}.png"
        f14 = PATH / f"{f12[1:]}.json"
        shutil.copy2(PATH_3, f14)
        shutil.copy2(PATH_4, f13)
        on_message(self, "", "f10")

    if f4 in (6,0,1,2):
        PATH_3.write_text(
            json.dumps(f1))



def on_submitted(self, event) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.app.store["2"]
    f3 = self.app.stores
    f4 = f3['_blank'][4]
    f5 = f3['_blank'][3]
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
        f3[f5] = f12
        f13 = [1,*f12,f5,f4]
        self.e_images.config = f13
        event.input.value = ""
        self.coord = None
        f1.focus()

        PATH_3.write_text(
            json.dumps(f3))

