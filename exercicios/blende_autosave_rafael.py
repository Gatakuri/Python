bl_info = {
    "name": "Auto Save Like VSCode",
    "blender": (4, 0, 0),
    "category": "System",
}

import bpy
import time

last_change = time.time()
last_save = time.time()

SAVE_DELAY = 5

def on_change(scene, depsgraph):
    global last_change
    last_change = time.time()

def autosave_timer():
    global last_save

    now = time.time()

    if now - last_change > SAVE_DELAY:
        if now - last_save > SAVE_DELAY:
            if bpy.data.is_saved:
                bpy.ops.wm.save_mainfile()
                print("Auto saved")
                last_save = now

    return 1

def register():
    if on_change not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(on_change)

    bpy.app.timers.register(autosave_timer)

def unregister():
    if on_change in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(on_change)