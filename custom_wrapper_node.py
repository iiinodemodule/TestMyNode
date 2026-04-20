import torch
from .src.BrightnessAdj import adjust_brightness


class BrightnessAdjustmentNode:
    CATEGORY = "0420_160502自訂演算法/III影像處理"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "strength": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.0,
                        "max": 10.0,
                        "step": 0.1,
                    },
                ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "execute"

    def execute(self, image, strength):
        return adjust_brightness(image, strength)
