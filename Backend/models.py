from textual.widgets import (DataTable, Input)
# from textual.coordinate import Coordinate
from pathlib import Path
import shutil
import time


CWD = Path.cwd()
PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
CONFIGS = STATIC_DIR / "model.json"
CONFIGS_ = PATH_FILE.parent / "Formula/za.json"
IMAGES_ = PATH_FILE.parent / "Formula/za.png"



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
    f00 = self.query_one("#cont-switch-1")
    f01 = self.query_one(f"#{f00.current}")
    f2 = self.full_IDs.index(self.app.focused.id)
    f3 = (f2 + prefix) % len(self.full_IDs)
    f4 = self.app.store["4-1"]
    f5 = self.full_IDs[f3]
    f7 = min(prefix,0)

    if self.coord is not None:
        event.prevent_default()
        event.stop()
        f01.focus()

    if self.coord is None:
        if ((f2 + f7) in
                [-1,9]):
            event.prevent_default()
            event.stop()

        if f3 in [0,1,2,4,5,6,7,8,9]:
            self.label.update(f4[f3] or "")
            self.e_third.value = ""
            self.e_fourth.value = ""

        if f3 in [3]:
            f1.current = f5
            table = self.query_one(f"#{f5}")
            coordinates = table.cursor_coordinate
            on_cell_highlighted_(self, coordinates)

        if f3 in [0,1,2]:
            # f0.current = f5
            tree = self.query_one(f"#{f5}")
            tree.reload()

        if (f2 + f7) == 9:
            sr = f"#{f0.current}"
            self.query_one(sr).focus()

        if (f2 + f7) == -1:
            sr = "#button-4"
            self.query_one(sr).focus()


async def on_key_(self, event) -> None:
    f00 = self.query_one("#cont-switch-0")
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f01 = f0.current.split("-")[-1]
    f4 = self.query_one("#third")
    f5 = ["backspace", "space"]
    f2 = f1.cursor_coordinate
    f3 = f1.get_cell_at(f2) or ""
    f6 = event.key

    match f6:
        case "f1":
            self.coord = f2
            on_message(self, f3, "f1")
            self.post_message(Input.Submitted(
                f4, ""))

        case "f2":
            self.coord = f2
            self._clipboard = str(f3)
            on_message(self, f3, "f2")
            self.post_message(Input.Submitted(
                f4, f4.value))

        case "f3":
            self._clipboard = str(f3)
            on_message(self, f3, "f3")

        case "f4":
            self.coord = f2
            clipboard = self._clipboard
            on_message(self, clipboard, "f4")
            self.post_message(Input.Submitted(
                f4, clipboard))

        case "f5":
            self.query_one(
                "#button-0").press()

        case "f6":
            self.query_one(
                "#button-1").press()

        case "f7":
            self.query_one(
                "#button-2").press()

        case "f8":
            self.query_one(
                "#button-6").press()

        case "f9":
            self.query_one(
                "#button-3").press()

        case "f10":
            self.query_one(
                "#button-4").press()

    if not isinstance(self.app.focused, Input):
        if f6 == "shift+tab":
            action_next_table(self, event, -1)
            self.coord = None
        elif f6 == "tab":
            action_next_table(self, event, 1)
            self.coord = None

    if isinstance(self.app.focused, Input):
        if f6 == "tab":
            event.stop()
            event.prevent_default()
            f01 = self.query_one("#third")
            self.post_message(Input.Submitted(
                f01, f01.value))
        if event.key == "escape":
            self.coord = None
            f4.value = ""
            f1.focus()

    if isinstance(self.app.focused, DataTable):
        if (len(f6) == 1 or f6 in f5):
            self.coord = f2

            if (int(f01) in [4,5]
                    and f2.column == 12):
                sarin = int(f01) - 3
                sar = f"dir-tree-{sarin}"
                self.query_one(f"#{sar}").focus()
                f00.current = sar
                event.stop()

            else:
                f4.focus()
                event.stop()

                if f6 in f5:
                    f4.value = str(f3)

                elif len(f6) == 1:
                    f4.value = f6

                    def after_focus():
                        f4.cursor_position = len(f6)

                    self.call_after_refresh(after_focus)


def on_cell_highlighted_(self, coordinate) -> None:
    f0 = self.query_one("#cont-switch-1")
    f3 = self.query_one("#fourth")
    f4 = self.query_one("#third")
    f5 = f0.current.split("-")[-1]
    f00 = self.app.now
    f7 = self.app.store["0"].get(f00)
    row, col = coordinate
    f4.value = ""
    f3.value = ""

    def safe(obj, *keys):
        for key in keys:
            try:
                obj = obj[key]
            except (IndexError, KeyError, TypeError):
                return None
        return obj

    try:
            value = safe(f7, row) or ""
            if value is not None:
                f3.value = value[1]
                f4.value = value[2]


    except IndexError:
        return


def on_pressed(self, event) -> None:
    f0 = self.app.store
    f1 = self.app.stores
    f2 = event.button.id
    f3 = f2.split("-")[-1]
    f5 = f1.setdefault("0", {})
    f6 = f5.setdefault("38", {})
    f7 = f5.setdefault("39", {})
    f8 =  f0["4-0"].index(f2) \
        if f2 in f0["4-0"] else -1
    f10 = f0["4-1"][f8]
    self.label.update(f10)
    f11 = {"6": 2, "3": 1}
    f12 = {"6": 1, "3": 2}
    f9 = self.turi

    if f2 == "button-6":
        self.app.stores = {}
        on_message(self,  "", "f5")

    elif f2 == "button-0":
        f6[0] = 1 - f6.get(0,0)
        on_message(self,f9[f6[0]],"f6")

    elif f2 == "button-1":
        f6[1] = 1 - f6.get(1,0)
        on_message(self,f9[f6[1]],"f7")

    elif f2 == "button-2":
        f6[2] = 1 - f6.get(2,0)
        on_message(self,f9[f6[2]],"f8")

    elif f2 == "button-3":
        f13 = f5.get('38', {})
        f14 = int(time.time())
        for k in ['0', '1', '2']:
            if f13.get(k, 0) == 0:
                f7[k] = f14
        on_message(self, "", "f9")

    elif f2 == "button-4":
        on_message(self, "", "f10")

    if f3 == "6" or f3 == "3":
        # self.e_images.config = f19
        pass

    if f3 == "4":
        f15 = str(int(time.time()))
        image_outs_ = CWD / f"{f15}.png"
        image_outs = CWD / f"{f15[1:]}.json"
        shutil.copy2(CONFIGS_, image_outs)
        shutil.copy2(IMAGES_, image_outs_)



def on_submitted(self, event) -> None:
    f1 = self.query_one("#cont-switch-1")
    f2 = self.query_one(f"#{f1.current}")
    f3 = f1.current.split("-")[-1]
    f80 = self.app.stores or {}
    f70 = self.app.store["0"]
    f05 = f70[self.app.now] or []
    f71 = f05[self.coord.row] or []
    # f72 = f71.get(self.coord.column)
    f00 = event.value
    f0 = self.coord



    if f71[0] and self.coord.column == 1:
        f2.update_cell_at(f0,f00)
        f6 = self.get_all_data(f2)
        test = sum(1 for row in f05
                   if row[0] != "")
        f06 = [""] * test

        for var,val in f6.items():
            test = val.get('0','')
            if len(f06) > int(var):
                f06[int(var)] = test

        new = [self.coord.row,self.coord.column,*f06]
        # news = [self.coord.row,self.coord.column,f00,s]
        self.app.stores[self.app.now] = new
        news = [*new,self.app.now]
        self.e_images.config = [0,0,news]



    #         f8 = f0.row in range(0, 10)
    #         f7 = f0.row in range(24, 31)
    #         f9 = 2 if f8 else (0 if f7 else 1)
    #         f10 = f9 if int(f3) == 0 else 1
    #
    #         self.app.stores[f3] = f6
    #         f11 = {**self.app.stores}
    #         f11.update({'_': [0,f10]})
    #         self.e_images.config = f11
    #
    #     self.coord = None
    #     event.input.value = ""
    #     f2.focus()

