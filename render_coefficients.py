import bpy
from os.path import join
from pathlib import Path
import os
import numpy as np
import pickle


coeffs = np.load("video_coefficients.npy")
blendshape_names = np.load("blendshape_names.npy")

# reference the active object
o = bpy.context.active_object

output_dir = Path("blender_renders")
output_dir.mkdir(exist_ok=True)

for k in blendshape_names[1:]:
    o.data.shape_keys.key_blocks[k].value = 0

for i in range(coeffs.shape[0]):
    cur_scores = dict(zip(blendshape_names[1:], coeffs[i][1:]))
    for k, v in cur_scores.items():
            o.data.shape_keys.key_blocks[k].value = v

    bpy.context.scene.render.filepath = output_dir / "out_{i}.jpg"
    bpy.ops.render.render(write_still = True)
