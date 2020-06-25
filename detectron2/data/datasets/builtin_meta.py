# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved


# All coco categories, together with their nice-looking visualization colors
# It's from https://github.com/cocodataset/panopticapi/blob/master/panoptic_coco_categories.json
COCO_CATEGORIES = [{'color': [128, 128, 128], 'isthing': 1, 'id': 1, 'name': 'person'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 2, 'name': 'bicycle'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 3, 'name': 'car'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 4, 'name': 'motorcycle'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 5, 'name': 'airplane'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 6, 'name': 'bus'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 7, 'name': 'train'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 8, 'name': 'truck'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 9, 'name': 'boat'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 10, 'name': 'traffic light'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 11, 'name': 'fire hydrant'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 13, 'name': 'stop sign'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 14, 'name': 'parking meter'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 15, 'name': 'bench'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 16, 'name': 'bird'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 17, 'name': 'cat'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 18, 'name': 'dog'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 19, 'name': 'horse'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 20, 'name': 'sheep'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 21, 'name': 'cow'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 22, 'name': 'elephant'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 23, 'name': 'bear'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 24, 'name': 'zebra'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 25, 'name': 'giraffe'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 27, 'name': 'backpack'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 28, 'name': 'umbrella'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 31, 'name': 'handbag'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 32, 'name': 'tie'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 33, 'name': 'suitcase'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 34, 'name': 'frisbee'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 35, 'name': 'skis'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 36, 'name': 'snowboard'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 37, 'name': 'sports ball'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 38, 'name': 'kite'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 39, 'name': 'baseball bat'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 40, 'name': 'baseball glove'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 41, 'name': 'skateboard'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 42, 'name': 'surfboard'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 43, 'name': 'tennis racket'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 44, 'name': 'bottle'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 46, 'name': 'wine glass'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 47, 'name': 'cup'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 48, 'name': 'fork'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 49, 'name': 'knife'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 50, 'name': 'spoon'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 51, 'name': 'bowl'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 52, 'name': 'banana'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 53, 'name': 'apple'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 54, 'name': 'sandwich'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 55, 'name': 'orange'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 56, 'name': 'broccoli'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 57, 'name': 'carrot'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 58, 'name': 'hot dog'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 59, 'name': 'pizza'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 60, 'name': 'donut'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 61, 'name': 'cake'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 62, 'name': 'chair'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 63, 'name': 'couch'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 64, 'name': 'potted plant'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 65, 'name': 'bed'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 67, 'name': 'dining table'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 70, 'name': 'toilet'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 72, 'name': 'tv'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 73, 'name': 'laptop'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 74, 'name': 'mouse'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 75, 'name': 'remote'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 76, 'name': 'keyboard'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 77, 'name': 'cell phone'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 78, 'name': 'microwave'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 79, 'name': 'oven'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 80, 'name': 'toaster'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 81, 'name': 'sink'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 82, 'name': 'refrigerator'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 84, 'name': 'book'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 85, 'name': 'clock'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 86, 'name': 'vase'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 87, 'name': 'scissors'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 88, 'name': 'teddy bear'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 89, 'name': 'hair drier'},
 {'color': [128, 128, 128], 'isthing': 1, 'id': 90, 'name': 'toothbrush'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 92, 'name': 'banner'},
 {'color': [128, 128, 128], 'isthing': 0, 'id': 93, 'name': 'blanket'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 95, 'name': 'bridge'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 100, 'name': 'cardboard'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 107, 'name': 'counter'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 109, 'name': 'curtain'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 112, 'name': 'door-stuff'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 118, 'name': 'floor-wood'},
 {'color': [128, 128, 128], 'isthing': 0, 'id': 119, 'name': 'flower'},
 {'color': [128, 128, 128], 'isthing': 0, 'id': 122, 'name': 'fruit'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 125, 'name': 'gravel'},
 {'color': [70, 70, 70], 'isthing': 0, 'id': 128, 'name': 'house'},
 {'color': [255, 228, 255], 'isthing': 0, 'id': 130, 'name': 'light'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 133, 'name': 'mirror-stuff'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 138, 'name': 'net'},
 {'color': [128, 128, 128], 'isthing': 0, 'id': 141, 'name': 'pillow'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 144, 'name': 'platform'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 145, 'name': 'playingfield'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 147, 'name': 'railroad'},
 {'color': [255, 255, 255], 'isthing': 0, 'id': 148, 'name': 'river'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 149, 'name': 'road'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 151, 'name': 'roof'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 154, 'name': 'sand'},
 {'color': [255, 255, 255], 'isthing': 0, 'id': 155, 'name': 'sea'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 156, 'name': 'shelf'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 159, 'name': 'snow'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 161, 'name': 'stairs'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 166, 'name': 'tent'},
 {'color': [128, 128, 128], 'isthing': 0, 'id': 168, 'name': 'towel'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 171, 'name': 'wall-brick'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 175, 'name': 'wall-stone'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 176, 'name': 'wall-tile'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 177, 'name': 'wall-wood'},
 {'color': [255, 255, 255], 'isthing': 0, 'id': 178, 'name': 'water-other'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 180, 'name': 'window-blind'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 181, 'name': 'window-other'},
 {'color': [255, 0, 255], 'isthing': 0, 'id': 184, 'name': 'tree-merged'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 185, 'name': 'fence-merged'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 186, 'name': 'ceiling-merged'},
 {'color': [0, 255, 0], 'isthing': 0, 'id': 187, 'name': 'sky-other-merged'},
 {'color': [255, 255, 0], 'isthing': 0, 'id': 188, 'name': 'cabinet-merged'},
 {'color': [128, 128, 128], 'isthing': 0, 'id': 189, 'name': 'table-merged'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 190, 'name': 'floor-other-merged'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 191, 'name': 'pavement-merged'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 192, 'name': 'mountain-merged'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 193, 'name': 'grass-merged'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 194, 'name': 'dirt-merged'},
 {'color': [206, 186, 171], 'isthing': 0, 'id': 195, 'name': 'paper-merged'},
 {'color': [128, 128, 128], 'isthing': 0, 'id': 196, 'name': 'food-other-merged'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 197, 'name': 'building-other-merged'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 198, 'name': 'rock-merged'},
 {'color': [0, 0, 255], 'isthing': 0, 'id': 199, 'name': 'wall-other-merged'},
 {'color': [255, 0, 0], 'isthing': 0, 'id': 200, 'name': 'rug-merged'}
 ]

# fmt: off
COCO_PERSON_KEYPOINT_NAMES = (
    "nose",
    "left_eye", "right_eye",
    "left_ear", "right_ear",
    "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow",
    "left_wrist", "right_wrist",
    "left_hip", "right_hip",
    "left_knee", "right_knee",
    "left_ankle", "right_ankle",
)
# fmt: on

# Pairs of keypoints that should be exchanged under horizontal flipping
COCO_PERSON_KEYPOINT_FLIP_MAP = (
    ("left_eye", "right_eye"),
    ("left_ear", "right_ear"),
    ("left_shoulder", "right_shoulder"),
    ("left_elbow", "right_elbow"),
    ("left_wrist", "right_wrist"),
    ("left_hip", "right_hip"),
    ("left_knee", "right_knee"),
    ("left_ankle", "right_ankle"),
)

# rules for pairs of keypoints to draw a line between, and the line color to use.
KEYPOINT_CONNECTION_RULES = [
    # face
    ("left_ear", "left_eye", (102, 204, 255)),
    ("right_ear", "right_eye", (51, 153, 255)),
    ("left_eye", "nose", (102, 0, 204)),
    ("nose", "right_eye", (51, 102, 255)),
    # upper-body
    ("left_shoulder", "right_shoulder", (255, 128, 0)),
    ("left_shoulder", "left_elbow", (153, 255, 204)),
    ("right_shoulder", "right_elbow", (128, 229, 255)),
    ("left_elbow", "left_wrist", (153, 255, 153)),
    ("right_elbow", "right_wrist", (102, 255, 224)),
    # lower-body
    ("left_hip", "right_hip", (255, 102, 0)),
    ("left_hip", "left_knee", (255, 255, 77)),
    ("right_hip", "right_knee", (153, 255, 204)),
    ("left_knee", "left_ankle", (191, 255, 128)),
    ("right_knee", "right_ankle", (255, 195, 77)),
]


def _get_coco_instances_meta():
    thing_ids = [k["id"] for k in COCO_CATEGORIES if k["isthing"] == 1]
    thing_colors = [k["color"] for k in COCO_CATEGORIES if k["isthing"] == 1]
    assert len(thing_ids) == 80, len(thing_ids)
    # Mapping from the incontiguous COCO category id to an id in [0, 79]
    thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
    thing_classes = [k["name"] for k in COCO_CATEGORIES if k["isthing"] == 1]
    ret = {
        "thing_dataset_id_to_contiguous_id": thing_dataset_id_to_contiguous_id,
        "thing_classes": thing_classes,
        "thing_colors": thing_colors,
    }
    return ret


def _get_coco_panoptic_separated_meta():
    """
    Returns metadata for "separated" version of the panoptic segmentation dataset.
    """
    stuff_ids = [k["id"] for k in COCO_CATEGORIES if k["isthing"] == 0]
    assert len(stuff_ids) == 53, len(stuff_ids)

    # For semantic segmentation, this mapping maps from contiguous stuff id
    # (in [0, 53], used in models) to ids in the dataset (used for processing results)
    # The id 0 is mapped to an extra category "thing".
    stuff_dataset_id_to_contiguous_id = {k: i + 1 for i, k in enumerate(stuff_ids)}
    # When converting COCO panoptic annotations to semantic annotations
    # We label the "thing" category to 0
    stuff_dataset_id_to_contiguous_id[0] = 0

    # 54 names for COCO stuff categories (including "things")
    stuff_classes = ["things"] + [
        k["name"].replace("-other", "").replace("-merged", "")
        for k in COCO_CATEGORIES
        if k["isthing"] == 0
    ]

    # NOTE: I randomly picked a color for things
    stuff_colors = [[82, 18, 128]] + [k["color"] for k in COCO_CATEGORIES if k["isthing"] == 0]
    ret = {
        "stuff_dataset_id_to_contiguous_id": stuff_dataset_id_to_contiguous_id,
        "stuff_classes": stuff_classes,
        "stuff_colors": stuff_colors,
    }
    ret.update(_get_coco_instances_meta())
    return ret


def _get_builtin_metadata(dataset_name):
    if dataset_name == "coco":
        return _get_coco_instances_meta()
    if dataset_name == "coco_panoptic_separated":
        return _get_coco_panoptic_separated_meta()
    elif dataset_name == "coco_person":
        return {
            "thing_classes": ["person"],
            "keypoint_names": COCO_PERSON_KEYPOINT_NAMES,
            "keypoint_flip_map": COCO_PERSON_KEYPOINT_FLIP_MAP,
            "keypoint_connection_rules": KEYPOINT_CONNECTION_RULES,
        }
    elif dataset_name == "cityscapes":
        # fmt: off
        CITYSCAPES_THING_CLASSES = [
            "person", "rider", "car", "truck",
            "bus", "train", "motorcycle", "bicycle",
        ]
        CITYSCAPES_STUFF_CLASSES = [
            "road", "sidewalk", "building", "wall", "fence", "pole", "traffic light",
            "traffic sign", "vegetation", "terrain", "sky", "person", "rider", "car",
            "truck", "bus", "train", "motorcycle", "bicycle", "license plate",
        ]
        # fmt: on
        return {
            "thing_classes": CITYSCAPES_THING_CLASSES,
            "stuff_classes": CITYSCAPES_STUFF_CLASSES,
        }
    raise KeyError("No built-in metadata for dataset {}".format(dataset_name))
