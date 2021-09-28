import fire

from yolov5.train import run as train
from yolov5.val import run as val
from yolov5.detect import run as detect
from yolov5.export import run as export


def app_train_val() -> None:
    """Cli app."""
    fire.Fire(
        {
            "train": train,
            "val": val,
        }
    )

def app_detect() -> None:
    fire.Fire(
        {
            "detect": detect,
        }
    )

def app_export() -> None:
    fire.Fire(
        {
            "export": export,
        }
    )