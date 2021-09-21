import io
import os
import re

from setuptools import setup, find_packages


def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        return f.read()

def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, "yolov5", "__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)

BASE_DEPENDENCIES = [
    "numpy>=1.18.5,<1.20;python_version=='3.6'",
    "numpy>=1.18.5;python_version>='3.7'",
    "matplotlib>=3.2.2,<4;python_version=='3.6'",
    "matplotlib>=3.2.2;python_version>='3.7'",
    "opencv-python>=4.1.2",
    "Pillow>=7.1.2",
    "PyYAML>=5.3.1",
    "scipy>=1.4.1",
    "torch>=1.7.0",
    "torchvision>=0.8.1",
    "tqdm>=4.41.0",
    "fire",
    "thop",
    "pandas",
    "seaborn>=0.11.0",
]

EXPORT_DEPENDENCIES = [
    "coremltools>=4.1",
    "onnx>=1.9.0",
    "onnx-simplifier>=0.3.6",
]

EXTRA_DEPENDENCIES = [
    "Cython", 
    "pycocotools>=2.0s",
    "albumentations>=1.0.3",
]

setup(
    name="yolov5",
    version=get_version(),
    author="",
    license="GPL",
    description="Packaged version of the Yolov5 object detector",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/fcakyon/yolov5-pip",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    install_requires=BASE_DEPENDENCIES,
    extras_require={
        "tests": ["pytest"],
        "export": EXPORT_DEPENDENCIES,
        "extras": EXTRA_DEPENDENCIES},
    include_package_data=True,
    options={'bdist_wheel':{'python_tag':'py36.py37.py38'}},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    keywords="machine-learning, deep-learning, ml, pytorch, YOLO, object-detection, vision, YOLOv3, YOLOv4, YOLOv5",
    entry_points={'console_scripts': [
        "yolov5=yolov5.cli:app",
        ],
    }
)