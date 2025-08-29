import bpy
from bpy.props import StringProperty, EnumProperty, PointerProperty
from bpy.types import Operator, Panel, PropertyGroup

class MyShortAddonProperties(PropertyGroup):
    """Store properties for the addon"""
    pass

class WM_OT_TemplateOperator(Operator):
    bl_idname = "wm.template_operator"
    bl_label = "Change Clothes"
    bl_description = "Toggle clothing visibility"

    def execute(self, context):
        scene = context.scene
        my_props = scene.my_short_addon_props
        
        # Get all clothing collections
        collections_to_check = [
            "Clothes 1",
            "Clothes 2", 
            "Clothes 3",
            "Clothes 4 (Add clothes here)",
            "Clothes 5 (Add clothes here)"
        ]
        
        # Hide all collections first
        for col_name in collections_to_check:
            if col_name in bpy.data.collections:
                bpy.data.collections[col_name].hide_viewport = True
        
        # Show the selected collection
        if my_props.clothes_enum == 'OPT1' and "Clothes 1" in bpy.data.collections:
            bpy.data.collections["Clothes 1"].hide_viewport = False
        elif my_props.clothes_enum == 'OPT2' and "Clothes 2" in bpy.data.collections:
            bpy.data.collections["Clothes 2"].hide_viewport = False
        elif my_props.clothes_enum == 'OPT3' and "Clothes 3" in bpy.data.collections:
            bpy.data.collections["Clothes 3"].hide_viewport = False
        elif my_props.clothes_enum == 'OPT4' and "Clothes 4 (Add clothes here)" in bpy.data.collections:
            bpy.data.collections["Clothes 4 (Add clothes here)"].hide_viewport = False
        elif my_props.clothes_enum == 'OPT5' and "Clothes 5 (Add clothes here)" in bpy.data.collections:
            bpy.data.collections["Clothes 5 (Add clothes here)"].hide_viewport = False
        
        # Force UI update
        for area in context.screen.areas:
            if area.type == 'PROPERTIES':
                area.tag_redraw()
                
        return {'FINISHED'}

class SCENE_PT_Objects(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Yug Panel"
    bl_idname = "SCENE_PT_objects"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_category = "Template Tab"   
    
    def draw(self, context):
        scene = context.scene
        my_props = scene.my_short_addon_props
        layout = self.layout
        
        # Clothing selection
        row = layout.row()
        row.prop(my_props, "clothes_enum", text="Clothes")
        
        # Pose selection  
        row = layout.row()
        row.prop(my_props, "pose_enum", text="Pose")
        
        # Apply button
        row = layout.row()
        row.operator("wm.template_operator", text="Apply Changes")
        
        # Clothing settings header
        row = layout.row()
        row.label(text="Clothes Settings")
        
        # Find which collection is currently visible
        visible_collection = None
        collections_to_check = [
            "Clothes 1",
            "Clothes 2", 
            "Clothes 3",
            "Clothes 4 (Add clothes here)",
            "Clothes 5 (Add clothes here)"
        ]
        
        for col_name in collections_to_check:
            if col_name in bpy.data.collections and not bpy.data.collections[col_name].hide_viewport:
                visible_collection = col_name
                break
        
        # Display objects from the visible collection
        if visible_collection and visible_collection in bpy.data.collections:
            collection = bpy.data.collections[visible_collection]
            for obj in collection.objects:
                row = layout.row(align=True)
                row.prop(obj, "hide_viewport", text="")
                row.label(text=obj.name)

# Property definitions
def register_properties():
    bpy.types.Scene.my_short_addon_props = PointerProperty(type=MyShortAddonProperties)
    
    # Define enum properties
    MyShortAddonProperties.pose_enum = EnumProperty(
        name="Pose",
        items=[
            ('OPT1', 'Pose 1', '', 3),
            ('OPT2', 'Pose 2', '', 4),
            ('OPT3', 'Pose 3', '', 3),
            ('OPT4', 'Pose 4', '', 4),
        ]
    )
    
    MyShortAddonProperties.clothes_enum = EnumProperty(
        name="Clothes",
        items=[
            ('OPT1', 'Clothes', '', 3),
            ('OPT2', 'Short', '', 4),
            ('OPT3', 'Swimsuit', '', 5),
            ('OPT4', 'Custom1', '', 6),
            ('OPT5', 'Custom2', '', 6),
        ]
    )

def unregister_properties():
    del bpy.types.Scene.my_short_addon_props

classes = [MyShortAddonProperties, WM_OT_TemplateOperator, SCENE_PT_Objects]

def register():
    from bpy.utils import register_class
    for cls in classes:
        bpy.utils.register_class(cls)
    register_properties()

def unregister():
    from bpy.utils import unregister_class
    unregister_properties()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

# Blender addon requirements
bl_info = {
    "name": "Clothing Manager",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "Properties Panel > Object Context > Template Tab",
    "description": "Manage clothing collections and visibility",
    "category": "3D View",
}

if __name__ == "__main__":
    register()
