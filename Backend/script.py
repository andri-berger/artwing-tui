from pathlib import Path
import imagesize
import json

PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Fontend"
PORT_2 = PORT_0.parent / "Formula"
PATH_2 = PORT_2 / "za.json"

def script_f0(self, h0) -> None:
    f0 = self.query_one("#label-0")
    f1 = self.app.store["4"]
    f2 = self.app.textfield
    f0.update(f1.get(h0, ""))
    self.app.textfields = (
        self.set_timer(
            3, lambda:
            f0.update(f2)))

def script_f1(self, h0, h1) -> None:
    f0 = self.query_one("#label-0")
    f1 = self.app.store["3"]
    f2 = self.app.textfield
    f3 = f1.get(h0, "")
    f0.update(f3.format(
        f3=h1.upper()))
    self.app.textfields = (
        self.set_timer(
            3, lambda:
            f0.update(f2)))

def script_f2(h0) -> Path:
    f0 = h0.stem
    f1 = h0.suffix
    f2 = h0.parent
    f3 = f"{f0}*{f1}"
    f4 = f2.glob(f3)
    f5 = len(list(f4))
    f6 = h0.with_stem(
        f"{h0.stem}_{f5-1}") \
        if f5 > 0 else h0
    return f6

def script_f3(h0, h1, h2) -> None:
    for child in h0.children:
        if child.data.path.name == h1:
            h2.move_cursor(child)
            break

def script_f4(h0, h1) -> list:
    f0 = [0,0,0,"",""] or []
    h1.setdefault("_blank",f0)
    f1 = h1.get("_blank")[4]
    f2 = h1.get("_blank")[3]
    f3 = h1.get(f2,None)
    f4 = f1 or h0 or ""
    h1['_blank'][4] = f4
    if f3 is not None:
        f4 = [*f3,f2,f4]
        f0 = [0,*f4]
    return f0

def script_f5(self, h0, h1) -> list:
    f0 = self.app.store
    f1 = self.app.stores
    f2 = f0["7"].get(h0, [])
    f3 = sum(1 for row in f2
             if row[0] != "")
    f4 = [0, 0, *[""] * f3]
    f5 = f1.get(h0, f4)
    f6 = f1["_blank"]
    f6[4] = h1
    f6[3] = h0
    f1[h0] = f5
    return f5

def script_f6(h0, h1, h2) -> None:
    f0 = imagesize.get(str(h2))
    f2 = h1.height * 18
    f3 = h1.width * 9
    f4 = f0[0] / f0[1]
    if f4 > (f3 / f2):
        h0.styles.width = "100%"
        h0.styles.height = "auto"
    elif f4 <= (f3 / f2):
        h0.styles.width = "auto"
        h0.styles.height = "100%"

def script_f7(self, h0) -> None:
    f0 = self.query_one("#dir-tree-2")
    f1 = self.query_one("#label-0")
    f2 = self.app.store["6"]
    f3 = f2.get(h0, [])
    if f3[1] is not None:
        f4 = self.app
        f1.update(f3[1])
        f4.textfield = f3[1]
    if f3[0] is not None:
        f12 = Path(f0.path).resolve()
        for node in f0.root.children:
            f13 = node.data.path or ""
            f14 = f13.relative_to(f12)
            if f14 == Path(f3[0]):
                node.expand()
                self.call_after_refresh(
                    script_f3, node, h0, f0)
                break

def script_f8(self, h0) -> None:
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
        f8 = h0.row
        f9 = h0.column
        f10 = len(f6) > f8
        f11 = len(f7[2:]) > f8
        f12 = f6[f8] if f10 else []
        f13 = f7[2:][f8] if f11 else ""
        if len(f12) > 2 and f9 <= 1:
            f0.value = f12[1] or ""
            f1.value = (str(f13)
                        or f12[2])

def script_f9(self, h0, h1) -> None:
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
    f14 = f13 + h1 + 0
    f15 = f14 % len(f7)
    f16 = min(h1, 0)
    f17 = f13 + f16

    if f15 not in (2,3):
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
            script_f8(self, f9)
            f5.update(f22)

    if f17 in (-1,9):
        h0.prevent_default()
        h0.stop()

    if f17 == 9:
        f1.focus()
    if f17 == -1:
        f2.focus()

    f12[1] = f15 or 0
    PATH_2.write_text(
        json.dumps(f11))
