from textual.widgets import DirectoryTree
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widgets import DataTable
from textual.widget import Widget
from pathlib import Path
from textual import on
from textual.app import ComposeResult
import imagesize
import asyncio
import shutil
import time
import json


CWD = Path.cwd()
APP = Path(__file__)
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR.parent / "Fontend"
ASSETS = ASSETS_DIR / "Formula/za.png"
CONFIGS = APP_DIR.parent / "Formula/za.json"
IMAGES = APP_DIR.parent / "Formula/za.png"
TEST = APP_DIR.parent / "uread.png"

class ImageTab(Widget):
    config: reactive[dict] = reactive(dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(TEST)

    def on_mount(self) -> None:
        self.query_one(Image).styles.width = "auto"
        self.query_one(Image).styles.height = "100%"

    def _select_child(self, parent_node, f8,tree) -> None:
        for child in parent_node.children:
            if child.data.path.name == f8:
                tree.move_cursor(child)
                break

    # 2 2 boxfit {}
    async def watch_config(self, value: dict):
        tree = self.app.query_one("#dir-tree-1")
        f0 = self.app.query_one("#cont-switch-1")
        f1 = self.app.query_one("#label-0")
        f2 = int(f0.current.split("-")[-1])
        f3 = self.app.query(DataTable)
        f4 = self.app.store["0"]
        f5 = self.app.store["3"]
        f7 = value[1][2:-1]
        f8 = value[1][-1]
        f9 = value[1]
        self.app.clear_notifications()
        self.notify(
            f"model: {value}")

        if value[0] == 0:
            with (self.app.batch_update()):
                f3[0].clear(columns=False)
                f07 = f4[f"{f8}"]
                for row_i in range(9):
                    tt = f07[row_i] if len(f07) > row_i else [""]
                    ja = f7[row_i] if len(f7) > row_i else ""
                    row = [tt[0],ja]
                    f3[0].add_row(*row)

            f3[0].move_cursor(
                row=f9[0],
                column=f9[1])

            two = Path(tree.path).resolve()
            for node in tree.root.children:
                one = node.data.path
                three = one.relative_to(two)
                if three == Path("artist"):
                    node.expand()
                    self.call_after_refresh(
                        self._select_child,
                        node, f8,tree)
                    break

        def after_focus():
            f1.update(f5[f8])
        self.call_after_refresh(
            after_focus)

        if value[0] >= 0:
            params = ",".join(str(p) for p in f7)
            check = [x for x in f7 if x != ""]
            params0 = params if len(check) else ","
            if self.query(Image):
                self.query_one(Image).remove()
            proc = await (asyncio
            .create_subprocess_exec(
                "gmic", str(TEST),
                f8, params0, '-output', str(IMAGES),
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL))
            await proc.communicate()
            await self.mount(Image(IMAGES))

            size = self.size
            cell_w, cell_h = 9, 18
            target_w = size.width * cell_w
            target_h = size.height * cell_h
            container_ratio = target_w / target_h

            width, height = imagesize.get(str(IMAGES))
            img_ratio = width / height

            if img_ratio > container_ratio:
                self.query_one(Image).styles.width = "100%"
                self.query_one(Image).styles.height = "auto"
            else:
                self.query_one(Image).styles.width = "auto"
                self.query_one(Image).styles.height = "100%"

    def render(self):
        return ""


class FileTypeTree(DirectoryTree):
    show_root = False

    def __init__(self, path, file_type: str, **kwargs):
        self.file_type = file_type
        super().__init__(path, **kwargs)

    def filter_paths(self, paths):
        return [p for p in paths if not p.name.startswith(".") and self._is_allowed(p)]

    def _is_allowed(self, p):
        if p.is_dir():
            return True  # always show dirs for navigation

        match self.file_type:
            case "naked":
                return p.suffix == ""
            case "multi":
                return (p.suffix.lower() == ".png"
                        or p.suffix.lower() == ".json")
        return False


    @on(DirectoryTree.FileSelected)
    async def selected(self, event: DirectoryTree.FileSelected) -> None:
        e_images = self.app.query_one(ImageTab)
        f00 = self.app.query_one("#data-table-0")
        f0 = self.app.query_one("#cont-switch-2")
        f1 = self.app.query_one(f"#{f0.current}")
        f02 = self.app.query_one("#label-0")
        f2 = f0.current.split("-")[-1]
        f3 = self.app.stores
        f03 = self.app.store["3"]
        # f4 = self.app.coord
        f5 = event.control.id
        f6 = f5.split("-")[-1]
        f7 = ['4','5'][int(f6)-1]
        f8 = ["module","modules"]
        f9 = f8[int(f6)-1]
        f10 = event.path


        if not f10.is_file():
            return

        if f5 == "dir-tree-0":
            shutil.copy2(f10, CONFIGS)
            f13 = f10.read_text()
            f14 = json.loads(f13)
            f14.update({'_': [2,1]})
            self.app.stores = f14
            self.e_images.config = f14
            await self.reload()

        elif f5 == "dir-tree-2":
            pass

        elif f5 == "dir-tree-1":
                temp = self.app.now
                self.app.now = f10.name
                # f15 = ASSETS_DIR / f9
                # f16 = f15 / f10.name
                # f02.update(f03[f10.name][0] or "")

                # f18 = f4.row
                # f17 = f4.column
                # if (int(f2) in [4, 5]
                #         and f17 == 12):
                #     f19 = f3.setdefault(f7, {})
                #     f20 = f19.setdefault(f18, {})
                #     f20[f17 or '11'] = f10.name
                #     f21 = f1.get_cell_at(f4)
                #     f22 = f15 / f21.name
                #     if f22.exists():
                #         f22.unlink()
                #     f1.update_cell_at(
                #         f4,f10.name)
                # else:
                #     f23 = f3.setdefault('0', {})
                #     f24 = f23.setdefault('40', {})
                #     f25 = f24[int(f6)-1] or ""
                #     f24[int(f6)-1] = f10.name
                #     f26 = f15 / f25
                #     if f26.exists():
                #         f26.unlink()

                f70 = self.app.store["0"]
                f77 = self.app.stores
                f05 = f70[f10.name] or []
                f90 = f77.get(f10.name)
                ts = f00.cursor_coordinate
                test = sum(1 for row in f05
                           if row[0] != "")
                f06 = [""] * test
                l60 = f90 or [0,0,*f06]
                l94 = [0,[*l60,f10.name]]
                jau = self.app.stores.get(temp,[])
                if len(jau) > 0:
                    jau[0] = ts.row if len(jau) > 0 else 0
                    jau[1] = ts.column if len(jau) > 0 else 0

                self.app.stores["_blank"] = [0,0,f10.name]
                if f77.get(f10.name) is None:
                    self.app.stores[f10.name] = l60
                e_images.config = l94

                CONFIGS.write_text(
                    json.dumps(f77))

                # on_message(self,
                #            f10.name,
                #            "f0")



