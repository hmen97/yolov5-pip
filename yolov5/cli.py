import fire

from yolov5.train import run as yolov5_train
from yolov5.val import run as yolov5_val
from yolov5.detect import run as yolov5_detect
from yolov5.export import run as yolov5_export


def train() -> None:
    fire.Fire(
        {
            "train": yolov5_train,
        }
    )

def val() -> None:
    fire.Fire(
        {
            "val": yolov5_val,
        }
    )

def detect() -> None:
    fire.Fire(
        {
            "detect": yolov5_detect,
        }
    )

def export() -> None:
    fire.Fire(
        {
            "export": yolov5_export,
        }
    )

# def app() -> None:
#     fire.Fire(
#         {
#             "train": yolov5_train,
#             "val": yolov5_val,
#             "detect": yolov5_detect,
#             "export": yolov5_export,
#         }
#     )