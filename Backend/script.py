from pathlib import Path
import imagesize
import json

PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Fontend"
PORT_2 = PORT_0.parent / "Formula"
PATH_3 = PORT_2 / "za.json"


def on_message(self, h0, h1) -> None:
    self.app.clear_notifications()
    f0 = self.query_one("#label-0")
    f1 = self.app.textfield
    f2 = {
        "f0": f"Image on path {h1} has been chosen for canvas, congrats, good choice!",
        "f1": f"(f1) {h1} deleted from table",
        "f2": f"(f2) {h1} cut to clipboard",
        "f3": f"(f3) {h1} copied to clipboard",
        "f4": f"(f4) {h1} pasted from clipboard",
        "f5": f"(f5) {h1} Clear Canvas",
        "f6": f"(f6) {h1} B00 Seed",
        "f7": f"(f7) {h1} C0 Seed",
        "f8": f"(f8) {h1} C0 Seed",
        "f9": f"(f9) {h1} Regenerate Art",
        "f10": f"(f10) {h1} Export to Disk",
        "button-0": f"FX {h1.upper()} PARAMS have been erased!",
        "button-1": f"FX REALTIME APPLICATION has been {h1}activated!",
        "button-2": f"THEME {h1.upper()} has been chosen!",
        "button-3": f"THEME {h1.upper()} has been chosen!",
        "button-4": f"PNG FILE has been saved to local file directory!",
        "button-5": f"PNG AND JSON FILES have been saved to disk!"}

    f0.update(f2.get(h0, ""))
    self.app.textfields = self.set_timer(
        3, lambda: f0.update(f1))

def safe_rename(dst: Path) -> Path:
    f0 = len(list(dst.parent.glob(f"{dst.stem}*{dst.suffix}")))
    f1 = dst.with_stem(f"{dst.stem}_{f0-1}") if f0 > 0 else dst
    return f1

def script(parent_node, f8, tree) -> None:
    for child in parent_node.children:
        if child.data.path.name == f8:
            tree.move_cursor(child)
            break

def script_f1(self, h0) -> list:
    f0 = [0,0,0,"",""]
    self.setdefault("_blank",f0)
    f1 = self.get("_blank")[4]
    f2 = self.get("_blank")[3]
    f3 = self.get(f2,None)
    f4 = f1 or h0 or ""
    self['_blank'][4] = f4
    if f3 is not None:
        f4 = [*f3,f2,f4]
        f0 = [0,*f4]
    return f0

def script_f2(self, h0, h1) -> list:
    f0 = self.app.store["2"]
    f1 = self.app.stores
    f2 = f0.get(h0, [])
    f3 = sum(1 for row in f2
             if row[0] != "")
    f4 = [0, 0, *[""] * f3]
    f5 = f1.get(h0, f4)
    f6 = f1["_blank"]
    f6[4] = h1
    f6[3] = h0
    f1[h0] = f5
    return f5

def script_f3(h0, h1, h2):
    f5, f6 = imagesize.get(str(h2))
    f3 = h1.height * 18
    f2 = h1.width * 9
    f7 = f5 / f6
    f8 = f2 / f3

    if f7 > f8:
        h0.styles.width = "100%"
        h0.styles.height = "auto"
    elif f7 <= f8:
        h0.styles.width = "auto"
        h0.styles.height = "100%"


def script_f0(self, h0) -> None:
    f0 = self.query_one("#dir-tree-1")
    f1 = self.query_one("#label-0")
    f2 = self.app.store["1"]
    f3 = f2.get(h0, [])
    if f3[1] is not None:
        self.app.textfield = f3[1]
        f1.update(f3[1])
    if f3[0] is not None:
        f12 = Path(f0.path).resolve()
        for node in f0.root.children:
            f13 = node.data.path or ""
            f14 = f13.relative_to(f12)
            if f14 == Path(f3[0]):
                node.expand()
                self.call_after_refresh(
                    script, node, h0, f0)
                break

# OK !!!
def on_highlighted(self, h0) -> None:
    f0 = self.query_one("#input-0")
    f1 = self.query_one("#input-1")
    f2 = self.app.store["2"]
    f3 = self.app.stores
    f1.value = ""
    f0.value = ""

    f4 = f3['_blank']
    f5 = f2.get(f4[3])
    if f5 is not None:
        f6 = h0.row
        f7 = h0.column
        f8 = len(f5) > f6
        f9 = f5[f6] if f8 else []
        if (len(f9) > 2
                and f7 <= 1):
            f0.value = f9[1]
            f1.value = f9[2]

# OK !!!
def action_next_table(self, h0, h1) -> None:
    f0 = self.query_one("#data-table")
    f1 = self.query_one("#dir-tree-0")
    f2 = self.query_one("#button-5")
    f3 = self.query_one("#input-1")
    f4 = self.query_one("#input-0")
    f5 = self.query_one("#label-0")
    f6 = self.app.store["3"]
    f7 = self.app.store["4"]
    f8 = self.app.store["1"]
    f9 = f0.cursor_coordinate
    f10 = self.app.focused.id
    f11 = self.app.stores
    f12 = f11['_blank']
    f13 = f7.index(f10)
    f14 = f13 + h1 + 0
    f15 = f14 % len(f7)
    f16 = min(h1, 0)
    f17 = f13 + f16

    if f15 != 3:
        f40 = self.app
        f18 = f6[f15] or ""
        f40.textfield = f18
        f5.update(f18)
        f3.value = ""
        f4.value = ""

    if f15 == 3:
        f19 = f12[3]
        f20 = f8.get(f19)
        if f20 is not None:
            f21 = len(f20) > 1
            f22 = f20[1] if f21 else ""
            on_highlighted(self, f9)
            self.app.textfield = f22
            f5.update(f22)

    if f17 == -1 or f17 == 9:
        h0.prevent_default()
        h0.stop()

    if f17 == 9:
        f1.focus()
    if f17 == -1:
        f2.focus()

    f12[1] = f15 or 0
    PATH_3.write_text(
        json.dumps(f11))
