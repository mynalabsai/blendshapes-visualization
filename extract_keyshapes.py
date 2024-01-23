# based on this script: https://gist.github.com/versluis/2e092b466b989b1e91f316599bcce016
# adapted for Blender 4.0

import bpy
import os
from pathlib import Path

cur_dir = "/specify/a/path"
os.chdir(cur_dir)

# Reference the active object
o = bpy.context.active_object

# CHANGE THIS to the folder you want to save your OBJ files in
exportPath = "shape_keys"
Path(exportPath).mkdir(exist_ok=True)

# Reset all shape keys to 0 (skipping the Basis shape on index 0
for skblock in o.data.shape_keys.key_blocks[1:]:
    skblock.value = 0

export_materials = False
# Iterate over shape key blocks and save each as an OBJ file
for skblock in o.data.shape_keys.key_blocks[1:]:
    skblock.value = 1.0  # Set shape key value to max

    # Set OBJ file path and Export OBJ
    objFileName = skblock.name + ".obj" # File name = shapekey name
    objPath = os.path.join(exportPath, objFileName)
    bpy.ops.wm.obj_export(filepath=objPath, export_selected_objects=False, export_materials=False, export_uv=False, apply_modifiers=True)

    skblock.value = 0 # Reset shape key value to 0

objPath = os.path.join(exportPath, "_neutral.obj")
bpy.ops.wm.obj_export(filepath=objPath, export_selected_objects=False, export_materials=False, export_uv=False, apply_modifiers=True)
