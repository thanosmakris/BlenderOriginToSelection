bl_info = {
    "name": "Origin To Selection",
    "author": "Thanos Makris",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "View3D > Mesh > Origin To Selection",
    "description": "Snaps the Origin to the selected element",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}


import bpy
from mathutils import Vector


def main(context):
    initialLocation = Vector(bpy.context.scene.cursor.location)
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.context.scene.cursor.location = (initialLocation[0], initialLocation[1], initialLocation[2])



class OriginToSelection(bpy.types.Operator):
    bl_idname = "object.origin_to_selection"
    bl_label = "Origin To Selection"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OriginToSelection.bl_idname, text=OriginToSelection.bl_label)


def register():
    bpy.utils.register_class(OriginToSelection)
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OriginToSelection)
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu_func)


if __name__ == "__main__":
    register()