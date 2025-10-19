###827pm 10/9/2025 Brainstorm: Item Line Up. Lies up selected objects along an axis###
### Done 1057pm 10/9/2025 ### 2h 30 mins

bl_info = {
    "name": "N Item line up",
    "author": "Lancine Doumbia",
    "version": (1, 0, 0),
    "blender": (2, 8, 0),
    "location": "View3D > Sidebar",
    "description": "Lies up the selected amount of objects along an axis",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy

class CoordinateProperties(bpy.types.PropertyGroup):
    coord_x: bpy.props.FloatProperty(
        name="", 
        min= -10000.00, 
        max=10000.00,
        )
    coord_y: bpy.props.FloatProperty(
        name="", 
        min= -10000.00, 
        max=10000.00,
        )
    coord_z: bpy.props.FloatProperty(
        name="", 
        min= -10000.00, 
        max=10000.00,
        )
    x_mode: bpy.props.BoolProperty(name="", default=False)
    y_mode: bpy.props.BoolProperty(name="", default=False)
    z_mode: bpy.props.BoolProperty(name="", default=False)


class OBJECT_OT_Toggle_X(bpy.types.Operator):
    bl_idname = "operator.activate_x_axis"
    bl_label = "My Class Name"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self, context):
        prop_ref = context.scene.where
        prop_ref.x_mode = not prop_ref.x_mode
   
        self.report({'INFO'}, f"{ 'Do not l' if not prop_ref.x_mode else 'L'}ine up on X axis")
        return {"FINISHED"}

    
class OBJECT_OT_Toggle_Y(bpy.types.Operator):
    bl_idname = "operator.activate_y_axis"
    bl_label = "My Class Name"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self, context):
        prop_ref = context.scene.where
        prop_ref.y_mode = not prop_ref.y_mode
      
        self.report({'INFO'}, f"{ 'Do not l' if not prop_ref.y_mode else 'L'}ine up on Y axis")
        return {"FINISHED"}

    
class OBJECT_OT_Toggle_Z(bpy.types.Operator):
    bl_idname = "operator.activate_z_axis"
    bl_label = "My Class Name"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self, context):
        prop_ref = context.scene.where
        prop_ref.z_mode = not prop_ref.z_mode
        
        self.report({'INFO'}, f"{ 'Do not l' if not prop_ref.z_mode else 'L'}ine up on Z axis")
        return {"FINISHED"}


class OBJECT_OT_Align_Axes(bpy.types.Operator):
    bl_idname = "operator.my_class_name"
    bl_label = "My Class Name"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        prop_ref = context.scene.where
        all_obj = context.selected_objects
        
        print(f"{all_obj}")

        for obj_ in all_obj:
            
            if (prop_ref.x_mode, prop_ref.y_mode, prop_ref.z_mode) == (True,True,True):
                self.report({'INFO'}, f"XYZ Anti-collide function activated.")
                return {"CANCELLED"}
            
            if prop_ref.x_mode:
                obj_.location.x = prop_ref.coord_x
                print("Name: {} X({})".format(obj_.name, obj_.location.x))  
            else:
                obj_.location.x
                print("Name: {} X({})".format(obj_.name, obj_.location.x))  
                
                
            if prop_ref.y_mode:
                obj_.location.y = prop_ref.coord_y
                print("Name: {} Y({})".format(obj_.name, obj_.location.y))
            else:
                obj_.location.y
                print("Name: {} Y({})".format(obj_.name, obj_.location.y))
            
            
            if prop_ref.z_mode:
                obj_.location.z = prop_ref.coord_z
                print("Name: {} Z({})".format(obj_.name, obj_.location.z))
            else:
                obj_.location.z   
                print("Name: {} Z({})".format(obj_.name, obj_.location.z))
            
            
            print("Name: {} ({},{},{})".format(obj_.name, obj_.location.x,obj_.location.y, obj_.location.z))
            
        
        self.report({'INFO'}, "Status info")
        return {"FINISHED"}


class OBJECT_PT_Panel(bpy.types.Panel):
    bl_idname = "panelname"
    bl_label = "Object Line Up"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"

    @classmethod
    def poll(cls,context):
        return context.selected_objects and context.object.mode == "OBJECT"

    def draw(self, context):
        layout = self.layout
        prop_ref = context.scene.where
        
        neat = layout.box()
        
        neat_row_x = neat.row(align=True)
        
        neat_row_x.prop(prop_ref,"coord_x")
        neat_row_x.operator("operator.activate_x_axis",text="X", depress=prop_ref.x_mode)
        
        neat_row_y = neat.row(align=True)
        
        neat_row_y.prop(prop_ref,"coord_y")
        neat_row_y.operator("operator.activate_y_axis",text="Y", depress=prop_ref.y_mode)
        
        neat_row_z = neat.row(align=True)
        
        neat_row_z.prop(prop_ref,"coord_z")
        neat_row_z.operator("operator.activate_z_axis",text="Z", depress=prop_ref.z_mode)
        
        layout.operator("my_operator.my_class_name",text="Align!")


classes = [CoordinateProperties, OBJECT_OT_Align_Axes, OBJECT_OT_Toggle_X, OBJECT_OT_Toggle_Y, OBJECT_OT_Toggle_Z, OBJECT_PT_Panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.where = bpy.props.PointerProperty(type=CoordinateProperties)
    
def unregister():
    for cls in reversed(classes):
        bpy.utils.register_class(cls)
    del bpy.types.Scene.where
    
if __name__ == "__main__":
    register()
