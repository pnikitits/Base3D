from direct.showbase.ShowBase import ShowBase
from .input_manager import input_manager
from panda3d.core import KeyboardButton
from .line import LineManager
from panda3d.core import AntialiasAttrib, loadPrcFileData, Point3, Point2
from .vec import vec2


class App(ShowBase):

    def setup(self, frame_rate: int, renderer: callable):
        ShowBase.__init__(self)
        self.taskMgr.doMethodLater(delayTime=1/frame_rate, funcOrTask=renderer,name='renderer')
        self.line_manager = LineManager(self.render)
        
        # loadPrcFileData('', 'multisamples 4') # Enable MSAA
        # self.render.setAntialias(AntialiasAttrib.MAuto)
        
        
    def setup_inputs(self):
        self.taskMgr.add(self.check_keys, "check_keys")
        
        
    def check_keys(self, task):
        
        _node_to_move = self.camera
        
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('z')):
            input_manager("z", _node_to_move)
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('s')):
            input_manager("s", _node_to_move)
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('q')):
            input_manager("q", _node_to_move)
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('d')):
            input_manager("d", _node_to_move)
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('f')):
            input_manager("f", _node_to_move)
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('e')):
            input_manager("e", _node_to_move)
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('a')):
            input_manager("a", _node_to_move)
        if self.mouseWatcherNode.is_button_down(KeyboardButton.ascii_key('r')):
            input_manager("r", _node_to_move)
        return task.cont
        
        
    def get_object_screen_pos(self, obj):
        # Get the object's position relative to the camera
        pos3d = self.camera._camera.getRelativePoint(obj, Point3(0, 0, 0))
        
        # Project the 3D point to 2D screen coordinates
        pos2d = Point2()
        if self.camLens.project(pos3d, pos2d):
            screen_x = pos2d.getX() * self.getAspectRatio()
            screen_y = pos2d.getY()
            return vec2(screen_x, screen_y)
        else:
            return vec2(-2, -2)