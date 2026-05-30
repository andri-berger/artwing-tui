
import imagesize
from PIL import Image as PILImage
from watchfiles import awatch
from textual.worker import Worker

# async def watch_directory(self) -> None:
#     async for changes in awatch(str(self.query_one(DirectoryTree).path)):
#         self.query_one(DirectoryTree).reload()
#
# def on_mount(self) -> None:
#     self.run_worker(self.watch_directory(), exclusive=True)


# def testlauf(self, image_outs, Image):
#     size = self.size
#     cell_w, cell_h = 9, 18
#     target_w = size.width * cell_w
#     target_h = size.height * cell_h
#     container_ratio = target_w / target_h
#
#     with PILImage.open(str(image_outs)) as img:
#         width, height = img.size  # note: PIL returns (width, height), opposite of cv2
#     img_ratio = width / height
#
#     if img_ratio > container_ratio:
#         self.query_one(Image).styles.width = "100%"
#         self.query_one(Image).styles.height = "auto"
#     else:
#         self.query_one(Image).styles.width = "auto"
#         self.query_one(Image).styles.height = "100%"


def testlauf(self, image_outs, Image):
    size = self.size
    cell_w, cell_h = 9, 18
    target_w = size.width * cell_w
    target_h = size.height * cell_h
    container_ratio = target_w / target_h

    width, height = imagesize.get(str(image_outs))
    img_ratio = width / height

    if img_ratio > container_ratio:
        self.query_one(Image).styles.width = "100%"
        self.query_one(Image).styles.height = "auto"
    else:
        self.query_one(Image).styles.width = "auto"
        self.query_one(Image).styles.height = "100%"