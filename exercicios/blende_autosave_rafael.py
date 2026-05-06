bl_info = {
    "name": "Auto Save by CoelhoDEV",
    "blender": (4, 0, 0),
    "category": "System",
}

import bpy
import time
from bpy.app.handlers import persistent

last_change = time.time()
last_save = time.time()

SAVE_DELAY = 5

@persistent
def on_change(scene, depsgraph):
    global last_change
    last_change = time.time()
    print("Mudança detectada")

def autosave():
    global last_save

    now = time.time()

    if now - last_change > SAVE_DELAY:
        if now - last_save > SAVE_DELAY:
            if bpy.data.is_saved:
                bpy.ops.wm.save_mainfile(check_existing=False)
                print("Auto saved")
                last_save = now

    return 1.0

def register():
    print("Addon iniciado")

    if on_change not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(on_change)

    bpy.app.timers.register(autosave)

def unregister():
    print("Addon removido")

    if on_change in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(on_change)