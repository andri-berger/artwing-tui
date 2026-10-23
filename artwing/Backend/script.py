import json
import re
from pathlib import Path

from PIL import Image
from platformdirs import (
    user_data_dir,
    user_state_dir,
)



def script_f01() -> Path:
    f0 = user_state_dir("artwing-tui")
    Path(f0).mkdir(parents=True, exist_ok=True)
    return Path(f0)


def script_f00() -> Path:
    f0 = user_data_dir("artwing-tui")
    Path(f0).mkdir(parents=True, exist_ok=True)
    return Path(f0)


PORT_00 = script_f00()
PATH_00 = PORT_00 / "700000000.json"
PATH_01 = PORT_00 / "1700000000.png"
PATH_02 = PORT_00 / "1700000001"
# raster formats both gmic and pillow read
FORMATS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".gif",
    ".tif",
    ".tiff",
    ".webp",
    ".ppm",
    ".pgm",
    ".pnm",
    ".tga",
)


def _ignore(dirpath, names):
    skip = {n for n in names if n.startswith(".")}
    if Path(dirpath).name == "_blank":
        skip = set(names)
    return skip


def script_f0(h) -> Path:
    f0 = 0
    f1 = h
    while f1.exists():
        f1 = h.with_stem(f"{h.stem}_{f0}")
        f0 += 1
    return f1


def script_f1(h, h0, h1) -> None:
    for h2 in h.children:
        if h2.data.path.name == h0:
            h1.move_cursor(h2)
            break


def script_f2(self, h) -> None:
    f0 = self.app.store["4"]
    script_f10(self, f0.get(h, ""))


def script_f3(self, h, h0) -> None:
    f0 = self.app.store["3"]
    f1 = f0.get(h, "")
    script_f10(self, f1.format(f3=h0.upper()))


def script_f4(h, h0, h1) -> None:
    with Image.open(h1) as f1:
        f0 = f1.size
    f2 = h.height * 18
    f3 = h.width * 9
    f4 = h0.styles
    f5 = f0[0] / f0[1]
    if f5 > (f3 / f2):
        f4.width = "100%"
        f4.height = "auto"
    else:
        f4.width = "auto"
        f4.height = "100%"


def script_f5(h, h0) -> list:
    f0 = [0, 0, 0, "", ""]
    # a copy, the returned list must not be
    # the stored one
    h0.setdefault("_blank", [*f0])
    f1 = h0.get("_blank")[4]
    f2 = h0.get("_blank")[3]
    f3 = h0.get(f2) if f2 else None
    f4 = f1 or h or ""
    h0["_blank"][4] = f4
    if f3 is not None:
        f4 = [*f3, f2, f4]
        f0 = [0, *f4]
    # an image without effect comes back raw
    elif f1 and Path(f1).is_file():
        f0 = [2, 0, 0, f2, f4]
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
    f3 = f2.get(h, [None, None])
    if f3[1] is not None:
        f4 = self.app
        f1.update(f3[1])
        f4.textfield = f3[1]
    if f3[0] is not None:
        f5 = script_f11(f0, f3[0])
        if f5 is not None:
            self.call_after_refresh(
                script_f1, f5, h, f0
            )


def script_f8(h) -> str:
    f0 = h.decode("latin-1")
    f1 = re.sub(r"\x1b\[[\d;]*m", "", f0)
    f2 = f1.strip().split("\n")[-1]
    return f2.split("***")[-1].strip()


def script_f9(h) -> None:
    # write to a temp file first, so a crash
    # never leaves a half written state file
    f0 = PATH_00.with_suffix(".tmp")
    f0.write_text(json.dumps(h))
    f0.replace(PATH_00)


def script_f10(self, h) -> None:
    f0 = self.app.query_one("#label-0")
    f1 = self.app.textfield
    f2 = self.app.textfields
    if f2 is not None:
        f2.stop()
    f0.update(h)
    self.app.textfields = self.set_timer(
        3, lambda: f0.update(f1)
    )


def script_f11(h, h0):
    for h1 in h.root.children:
        if h1.data.path.name == h0:
            h1.expand()
            return h1
    return None


def script_f12(h) -> dict | None:
    # only accept artwing state files, any
    # other json on disk is ignored
    try:
        f0 = json.loads(Path(h).read_text())
    except OSError, ValueError:
        return None
    f1 = isinstance(f0, dict)
    f2 = f0.get("_blank") if f1 else None
    f3 = isinstance(f2, list) and len(f2) == 5
    return f0 if f3 else None


def script_f13(h) -> Path:
    # gmic parses "," and "$" in file names,
    # so hand it a link with a plain name
    f0 = Path(h)
    f1 = PATH_02.with_suffix(f0.suffix.lower())
    for h0 in PORT_00.glob(f"{PATH_02.name}.*"):
        h0.unlink()
    f1.symlink_to(f0.resolve())
    return f1
