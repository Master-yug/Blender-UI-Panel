import bpy
from bpy.props import StringProperty, EnumProperty

             

class MyShortAddonProperties(bpy.types.Operator):
    bl_idname = "wm.template_operator"
    bl_label = "Clothes"

    pose_enum : bpy.props.EnumProperty(
        name="",
        items= [
                    ('OPT1','Pose 1','',3),
                    ('OPT2','Pose 2','',4),
                    ('OPT3','Pose 3','',3),
                    ('OPT4','Pose 4','',4),
                ]
            )

    
    clothes_enum : bpy.props.EnumProperty(
        name="",
        items= [
                    ('OPT1','Clothes','',3),
                    ('OPT2','Short','',4),
                    ('OPT3','Swimsuit','',5),
                    ('OPT4','Custom1','',6),
                    ('OPT5','Custom2','',6),
                ]
            )
    
#    def invoke(self, context, event):
#        wm = context.window_manager
#        return wm.invoke_props_dialog(self, width=500)

    def execute(self, context):
        
        col = bpy.data.collections
        if col is not None:
            if self.clothes_enum == 'OPT1':            
                col["Clothes 1"].hide_viewport = False
            elif self.clothes_enum != 'OPT1':
                col["Clothes 1"].hide_viewport = True
            if self.clothes_enum == 'OPT2':            
                col["Clothes 2"].hide_viewport = False                
            elif self.clothes_enum != 'OPT2':
                col["Clothes 2"].hide_viewport = True
            if self.clothes_enum == 'OPT3':            
                col["Clothes 3"].hide_viewport = False
            elif self.clothes_enum != 'OPT3':
                col["Clothes 3"].hide_viewport = True
            if self.clothes_enum == 'OPT4':            
                col["Clothes 4 (Add clothes here)"].hide_viewport = False
            elif self.clothes_enum != 'OPT4':
                col["Clothes 4 (Add clothes here)"].hide_viewport = True
            if self.clothes_enum == 'OPT5':            
                col["Clothes 5 (Add clothes here)"].hide_viewport = False
            elif self.clothes_enum != 'OPT5':
                col["Clothes 5 (Add clothes here)"].hide_viewport = True      
                          
        else:
            print("error")
        return {'FINISHED'} 

       
    def draw(self, context):
        layout = self.layout
        layout.operator("wm.template_operator")
#        layout.operator_menu_enum("wm.template_operator", "clothes_enum", text = "Change Clothes")
#        layout.operator_menu_enum("wm.template_operator", "pose_enum", text = "Change Pose")
        row = layout.row()
        
        int = self.clothes_enum
        
#        myInt = 0
#        
#        if int == 'OPT1':
#            myInt = 3
#        if int == 'OPT2':
#            myInt = 4
#        if int == 'OPT3':
#            myInt = 5
#        if int == 'OPT4':
#            myInt = 6       
        
#        col1 = bpy.data.collections[myInt].objects
#        for obj in col1:
#            print(obj.name)
#            row.prop(obj, "hide_viewport", icon = 'CHECKBOX_HLT', text = "")
#            row.label(text="" + obj.name)


class Parts(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Kay Panel"
    bl_idname = "SCENE_PT_objects"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_category = "Template Tab"   
    
    def draw(self, context):
        scn = bpy.context.scene
        layout = self.layout
        row = layout.row()
        col = layout.column()
        row_col = row.column(align=True)
        layout.operator_menu_enum("wm.template_operator", "clothes_enum", text = "Change Clothes")
        layout.operator_menu_enum("wm.template_operator", "pose_enum", text = "Change Pose")
        row.label(text="Clothes Settings")
        
        col1 = bpy.data.objects
        col2 = bpy.data.collections
        if col2["Clothes 1"].hide_viewport == False: 
            tes = bpy.data.collections["Clothes 1"].objects 
            for obj1 in tes:
                
                row = layout.row(align=True) 
                      
                row.prop(obj1, "hide_viewport", icon = 'CHECKBOX_HLT', text = "")
                row.label(text="" + obj1.name) 
        if col2["Clothes 2"].hide_viewport == False: 
            tes = bpy.data.collections["Clothes 2"].objects 
            for obj2 in tes:
                
                row = layout.row(align=True) 
                      
                row.prop(obj2, "hide_viewport", icon = 'CHECKBOX_HLT', text = "")
                row.label(text="" + obj2.name)                 
        if col2["Clothes 3"].hide_viewport == False: 
            tes = bpy.data.collections["Clothes 3"].objects 
            for obj1 in tes:
                
                row = layout.row(align=True) 
                      
                row.prop(obj1, "hide_viewport", icon = 'CHECKBOX_HLT', text = "")
                row.label(text="" + obj1.name) 
        if col2["Clothes 4 (Add clothes here)"].hide_viewport == False: 
            tes = bpy.data.collections["Clothes 4 (Add clothes here)"].objects 
            for obj2 in tes:
                
                row = layout.row(align=True) 
                      
                row.prop(obj2, "hide_viewport", icon = 'CHECKBOX_HLT', text = "")
                row.label(text="" + obj2.name)
        if col2["Clothes 5 (Add clothes here)"].hide_viewport == False: 
            tes = bpy.data.collections["Clothes 5 (Add clothes here)"].objects 
            for obj2 in tes:
                
                row = layout.row(align=True) 
                      
                row.prop(obj2, "hide_viewport", icon = 'CHECKBOX_HLT', text = "")
                row.label(text="" + obj2.name)

#        row.operator("mesh.dropdownexample")
#        col.prop(scn, "comboBox", text="")



classes = [Parts, MyShortAddonProperties]
                
def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class

    for cls in classes:
        unregister_class(cls)

    
if __name__ == "__main__":
    register()
