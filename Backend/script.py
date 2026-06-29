from pathlib import Path

import imagesize

PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Fontend"
PORT_2 = PORT_0.parent / "Formula"
PATH_2 = PORT_2 / "var.json"


def script_f0(h) -> Path:
    f0 = h.stem
    f1 = h.suffix
    f2 = h.parent
    f3 = f"{f0}*{f1}"
    f4 = f2.glob(f3)
    f5 = len(list(f4))
    f6 = (
        h.with_stem(f"{h.stem}_{f5 - 1}")
        if f5 > 0
        else h
    )
    return f6


def script_f1(h, h0, h1) -> None:
    for h2 in h.children:
        if h2.data.path.name == h0:
            h1.move_cursor(h2)
            break


def script_f2(self, h) -> None:
    f0 = self.query_one("#label-0")
    f1 = self.app.store["4"]
    f2 = self.app.textfield
    f0.update(f1.get(h, ""))
    self.app.textfields = self.set_timer(
        3, lambda: f0.update(f2)
    )


def script_f3(self, h, h0) -> None:
    f0 = self.query_one("#label-0")
    f1 = self.app.store["3"]
    f2 = self.app.textfield
    f3 = f1.get(h, "")
    f0.update(f3.format(f3=h0.upper()))
    self.app.textfields = self.set_timer(
        3, lambda: f0.update(f2)
    )


def script_f4(h, h0, h1) -> None:
    f0 = imagesize.get(str(h1))
    f2 = h.height * 18
    f3 = h.width * 9
    f4 = h0.styles
    f5 = f0[0] / f0[1]
    if f5 > (f3 / f2):
        f4.width = "100%"
        f4.height = "auto"
    elif f5 <= (f3 / f2):
        f4.width = "auto"
        f4.height = "100%"


def script_f5(h, h0) -> list:
    f0 = [0, 0, 0, "", ""] or []
    h0.setdefault("_blank", f0)
    f1 = h0.get("_blank")[4]
    f2 = h0.get("_blank")[3]
    f3 = h0.get(f2, None)
    f4 = f1 or h or ""
    h0["_blank"][4] = f4
    if f3 is not None:
        f4 = [*f3, f2, f4]
        f0 = [0, *f4]
    return f0


def script_f6(self, h, h0) -> list:
    f0 = self.app.store
    f1 = self.app.stores
    f2 = f0["7"].get(h, [])
    f3 = sum(1 for row in f2 if row[0] != "")
    f4 = [0, 0, *[""] * f3]
    f5 = f1.get(h, f4)
    f6 = f1["_blank"]
    f6[4] = h0
    f6[3] = h
    f1[h] = f5
    return f5


def script_f7(self, h) -> None:
    f0 = self.query_one("#dir-tree-2")
    f1 = self.query_one("#label-0")
    f2 = self.app.store["6"]
    f3 = f2.get(h, [])
    if f3[1] is not None:
        f4 = self.app
        f1.update(f3[1])
        f4.textfield = f3[1]
    if f3[0] is not None:
        f12 = Path(f0.path).resolve()
        for h0 in f0.root.children:
            f13 = h0.data.path or ""
            f14 = f13.relative_to(f12)
            if f14 == Path(f3[0]):
                h0.expand()
                self.call_after_refresh(
                    script_f1, h0, h, f0
                )
                break
