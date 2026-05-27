
import numpy as np
import cv2

import subprocess


def open_fred(input_path, settings):
    results = subprocess.run([
        'gmic', str(input_path),
        'tunnel', '20',
        '-output', str(input_path)
    ])
    return results


