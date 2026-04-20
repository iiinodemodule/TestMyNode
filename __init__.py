from .custom_wrapper_node import BrightnessAdjustmentNode

NODE_CLASS_MAPPINGS = {
    "custom.algorithm.new_node_0420_160502": BrightnessAdjustmentNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "custom.algorithm.new_node_0420_160502": "0420自定節點名稱_0420_160502",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
