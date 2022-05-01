DEFAULT_BLOCKS_ARGS = {
    "originnet-s": [
        {
            "kernel_size": (3, 3),
            "num_repeat": 2,
            "input_filters": 16,
            "output_filters": 16,
            "expand_ratio": 1,
            "se_ratio": 0.0,
            "strides": 1,
            "conv_type": 1,
        }, {
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "input_filters": 16,
            "output_filters": 32,
            "expand_ratio": 4,
            "se_ratio": 0.0,
            "strides": 2,
            "conv_type": 1,
        }, {
            "conv_type": 1,
            "expand_ratio": 4,
            "input_filters": 32,
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "output_filters": 48,
            "se_ratio": 0,
            "strides": 2,
        }, {
            "conv_type": 0,
            "expand_ratio": 4,
            "input_filters": 48,
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "output_filters": 96,
            "se_ratio": 0.25,
            "strides": 2,
        }, {
            "conv_type": 0,
            "expand_ratio": 6,
            "input_filters": 96,
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "output_filters": 192,
            "se_ratio": 0.25,
            "strides": 2,
        }
    ],
    "originnet-m": [
        {
            "kernel_size": (3, 3),
            "num_repeat": 2,
            "input_filters": 24,
            "output_filters": 24,
            "expand_ratio": 1,
            "se_ratio": 0.0,
            "strides": 1,
            "conv_type": 1,
        }, {
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "input_filters": 24,
            "output_filters": 48,
            "expand_ratio": 4,
            "se_ratio": 0.0,
            "strides": 2,
            "conv_type": 1,
        }, {
            "conv_type": 1,
            "expand_ratio": 4,
            "input_filters": 48,
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "output_filters": 64,
            "se_ratio": 0,
            "strides": 2,
        }, {
            "conv_type": 0,
            "expand_ratio": 4,
            "input_filters": 64,
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "output_filters": 128,
            "se_ratio": 0.25,
            "strides": 2,
        }, {
            "conv_type": 0,
            "expand_ratio": 6,
            "input_filters": 128,
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "output_filters": 256,
            "se_ratio": 0.25,
            "strides": 2,
        }
    ],
    'originnet-l': [
        {
            "kernel_size": (3, 3),
            "num_repeat": 4,
            "input_filters": 32,
            "output_filters": 32,
            "expand_ratio": 1,
            "se_ratio": 0.0,
            "strides": 1,
            "conv_type": 1,
        }, {
            "kernel_size": (3, 3),
            "num_repeat": 8,
            "input_filters": 32,
            "output_filters": 64,
            "expand_ratio": 4,
            "se_ratio": 0.0,
            "strides": 2,
            "conv_type": 1,
        }, {
            "conv_type": 1,
            "expand_ratio": 4,
            "input_filters": 64,
            "kernel_size": (3, 3),
            "num_repeat": 8,
            "output_filters": 96,
            "se_ratio": 0,
            "strides": 2,
        }, {
            "conv_type": 0,
            "expand_ratio": 4,
            "input_filters": 96,
            "kernel_size": (3, 3),
            "num_repeat": 8,
            "output_filters": 192,
            "se_ratio": 0.25,
            "strides": 2,
        }, {
            "conv_type": 0,
            "expand_ratio": 6,
            "input_filters": 192,
            "kernel_size": (3, 3),
            "num_repeat": 16,
            "output_filters": 256,
            "se_ratio": 0.25,
            "strides": 2,
        },
    ]
}