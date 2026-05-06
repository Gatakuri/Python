import bpy
import time

last_save = 0
save_interval = 10  # segundos

def autosave(scene, depsgraph):
    global last_save

    current_time = time.time()

    # evita salvar toda hora
    if current_time - last_save > save_interval:
        if bpy.data.is_saved:
            bpy.ops.wm.save_mainfile()
            print("Projeto salvo automaticamente!")
            last_save = current_time

# remove duplicados
for h in bpy.app.handlers.depsgraph_update_post:
    if h.__name__ == "autosave":
        bpy.app.handlers.depsgraph_update_post.remove(h)

bpy.app.handlers.depsgraph_update_post.append(autosave)