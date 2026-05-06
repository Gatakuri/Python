bl_info = {
    "name": "Auto Save by CoelhoDEV",
    "blender": (4, 0, 0),
    "category": "System",
}

import bpy
import time
from bpy.app.handlers import persistent

last_change = 0
last_save = 0
is_dirty = False

SAVE_DELAY = 5

@persistent
def on_change(scene, depsgraph):
    global last_change, is_dirty

    is_dirty = True
    last_change = time.time()

def autosave():
    global last_save, is_dirty

    now = time.time()

    # só salva se houve mudança
    if is_dirty:

        # espera parar de mexer
        if now - last_change > SAVE_DELAY:

            if bpy.data.is_saved:
                bpy.ops.wm.save_mainfile(check_existing=False)

                print("Auto saved")

                last_save = now
                is_dirty = False

    return 1.0

def register():
    print("Addon iniciado")

    if on_change not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(on_change)

    bpy.app.timers.register(autosave)

def unregister():
    if on_change in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(on_change)