from direct.showbase.ShowBase import ShowBase
from .input_manager import input_manager
from panda3d.core import KeyboardButton
from .line import LineManager
from panda3d.core import Point3, Point2
from .vec import vec2
from .node import Node
from .primitive import sphere
from .hud import label
from .vec import vec3


class App(ShowBase):

    def setup(self, frame_rate: int, renderer: callable):
        """Setup the application"""
        ShowBase.__init__(self)
        self.taskMgr.doMethodLater(delayTime=1/frame_rate, funcOrTask=renderer,name='renderer')
        self.line_manager = LineManager(self.render)
        self.setup_inputs()
        
        
    def setup_inputs(self):
        """Setup the keyboard inputs"""
        self.taskMgr.add(self.check_keys, "check_keys")
        
        
    def add_world_origin(self,
                         line_size: float=0.5,
                         line_thickness: float=2.0,
                         text_size: float=0.05):
        """Center of the scene with axis lines"""
        self.line_manager.make_line("line_x", points=[(0,0,0), (line_size,0,0)], color=(1, 0, 0, 1), thickness=line_thickness)
        self.line_manager.make_line("line_y", points=[(0,0,0), (0,line_size,0)], color=(0, 1, 0, 1), thickness=line_thickness)
        self.line_manager.make_line("line_z", points=[(0,0,0), (0,0,line_size)], color=(0, 0, 1, 1), thickness=line_thickness)
        
        self.node_center = Node(geometry=sphere(self, radius=0.001), render=self.render)
        self.node_x = Node(geometry=sphere(self, radius=0.001), render=self.render, pos=vec3(line_size, 0, 0))
        self.node_y = Node(geometry=sphere(self, radius=0.001), render=self.render, pos=vec3(0, line_size, 0))
        self.node_z = Node(geometry=sphere(self, radius=0.001), render=self.render, pos=vec3(0, 0, line_size))
        
        self.label_x = label(text="X", pos=vec2(0, 0), size=text_size, align='center')
        self.label_y = label(text="Y", pos=vec2(0, 0), size=text_size, align='center')
        self.label_z = label(text="Z", pos=vec2(0, 0), size=text_size, align='center')
        
        
    def update_world_origin(self):
        """Update the world origin label positions"""
        self.label_x.pos = self.get_object_screen_pos(self.node_x._geometry)
        self.label_y.pos = self.get_object_screen_pos(self.node_y._geometry)
        self.label_z.pos = self.get_object_screen_pos(self.node_z._geometry)
        
        
    def check_keys(self, task):
        """Check the keyboard inputs"""
        _node_to_move = self.camera
        keys = ['z', 's', 'q', 'd', 'f', 'e', 'a', 'r']
        
        for key in keys:
            if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key(key)):
                input_manager(key, _node_to_move)
        
        return task.cont
        
        
    def get_object_screen_pos(self, obj):
        """Get the screen position of a 3D object in the scene"""
        pos3d = self.camera._camera.getRelativePoint(obj, Point3(0, 0, 0))
        pos2d = Point2()
        if self.camLens.project(pos3d, pos2d):
            screen_x = pos2d.getX() * self.getAspectRatio()
            screen_y = pos2d.getY()
            return vec2(screen_x, screen_y)
        else:
            return vec2(-2, -2)
        
        
    def get_window_size(self):
        """Get the window size"""
        return self.win.getXSize(), self.win.getYSize()
    
    
    def debug_labels(self):
        """Create debug labels for the camera position, rotation, and window size"""
        self.debug_label_1 = label(text="cam_pos", pos=vec2(0, 0.9), size=0.05, parent=self.a2dLeftCenter)
        self.debug_label_2 = label(text="cam_rot", pos=vec2(0, 0.85), size=0.05, parent=self.a2dLeftCenter)
        self.debug_label_3 = label(text="win_size", pos=vec2(0, 0.8), size=0.05, parent=self.a2dLeftCenter)

    def update_debug_labels(self):
        """Update the debug labels with the camera position, rotation, and window size"""
        self.debug_label_1.text = f"Camera Position: {self.camera.pos}"
        self.debug_label_2.text = f"Camera Rotation: {self.camera.rot}"
        self.debug_label_3.text = f"Window Size: {self.get_window_size()}"