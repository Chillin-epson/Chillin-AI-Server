# Copyright (c) Meta Platforms, Inc. and affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from .image_to_annotations import image_to_annotations
from .annotations_to_animation import annotations_to_animation
from pathlib import Path
from pkg_resources import resource_filename


def convert_to_GIF(img: any, char_anno_dir: str, motion_type: str):

    
    if motion_type == "dance":
        motion_yaml = "dab.yaml"
    elif motion_type == "hello":
        motion_yaml = "wave_hello.yaml"
    elif motion_type == "jump":
        motion_yaml = "jumping.yaml"
    elif motion_type == "zombie":
        motion_yaml = "zombie.yaml"
    else:
        motion_yaml = "dab.yaml"

    motion_cfg_fn = resource_filename(__name__, 'config/motion/'+motion_yaml)
    retarget_cfg_fn = resource_filename(__name__, 'config/retarget/fair1_ppf.yaml')

    # create the annotations
    image_to_annotations(img, char_anno_dir)

    print("image_to_annotations is successful")

    # create the animation
    annotations_to_animation(char_anno_dir, motion_cfg_fn, retarget_cfg_fn)

    print("annotations_to_animation is successful")


