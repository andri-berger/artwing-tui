from pathlib import Path


def select_child(parent_node, f8, tree) -> None:
    for child in parent_node.children:
        if child.data.path.name == f8:
            tree.move_cursor(child)
            break

def checker(self, f05) -> None:
    f1 = self.app.query_one("#dir-tree-1")
    f02 = self.app.store["1"]
    f10 = f02.get(f05, [])
    if f10[0] is not None:
        f12 = Path(f1.path).resolve()
        for node in f1.root.children:
            f13 = node.data.path
            f14 = f13.relative_to(f12)
            if f14 == Path(f10[0]):
                node.expand()
                self.call_after_refresh(
                    select_child,
                    node, f05, f1)
                break

def helsing(self, param) -> list:
    f1 = [0,0,0,"",""]
    self.setdefault("_blank",f1)
    f3 = self.get("_blank")[4]
    f4 = self.get("_blank")[3]
    f5 = self.get(f4,None)
    f7 = f3 or param or ""
    self['_blank'][4] = f7
    if f5 is not None:
        f7 = [*f5,f4,f7]
        f1 = [0,*f7]
    return f1
