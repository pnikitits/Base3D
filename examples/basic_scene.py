from src.app import App
from src.node import Node
from src.primitive import sphere
from src.hud import label
from src.vec import vec2, vec3, vec4
from src.light import Light
from src.camera import Camera
from src.skybox import Skybox
import math
from panda3d.core import Point3, Point2


class BasicScene(App):

    def __init__(self):
        self.setup(frame_rate=60, renderer=self.renderer)
        
        self.camera = Camera(self,
                             pos=vec3(1.02, -2.21, 0.75),
                             rot=vec3(20, -10, 0))
        self.setup_inputs()
        self.light_1 = Light(pos=vec3(1,1,1), color=vec4(1,1,1,1), render=self.render)
        
        
        # Center of the scene with axis lines
        _line_size = 0.5
        self.line_manager.make_line("line_x", points=[(0,0,0), (_line_size,0,0)], color=(1, 0, 0, 1), thickness=2.0)
        self.line_manager.make_line("line_y", points=[(0,0,0), (0,_line_size,0)], color=(0, 1, 0, 1), thickness=2.0)
        self.line_manager.make_line("line_z", points=[(0,0,0), (0,0,_line_size)], color=(0, 0, 1, 1), thickness=2.0)
        
        self.node_center = Node(geometry=sphere(self, radius=0.01), render=self.render)
        self.node_x = Node(geometry=sphere(self, radius=0.01), render=self.render, pos=vec3(_line_size, 0, 0))
        self.node_y = Node(geometry=sphere(self, radius=0.01), render=self.render, pos=vec3(0, _line_size, 0))
        self.node_z = Node(geometry=sphere(self, radius=0.01), render=self.render, pos=vec3(0, 0, _line_size))
        
        self.label_x = label(text="X", pos=vec2(0.5, 0), size=0.1, align='center')
        self.label_y = label(text="Y", pos=vec2(0, 0.5), size=0.1, align='center')
        self.label_z = label(text="Z", pos=vec2(0, 0), size=0.1, align='center')
        
        
        
        self.label_1 = label(text="placeholder", pos=vec2(0, 0.8), size=0.1, align='center')
        self.label_2 = label(text="placeholder", pos=vec2(0, 0.9), size=0.1, align='center')
        skybox = Skybox(app=self, path="/Users/pierrenikitits/Documents/GitHub/Base3D/assets/textures/Skybox", size=20)
        

    def renderer(self, task):
        
        _cam_pos = self.camera.pos
        _cam_pos = vec3(_cam_pos.x, _cam_pos.y, _cam_pos.z)
        _cam_rot = self.camera.rot
        _cam_rot = vec3(_cam_rot.x, _cam_rot.y, _cam_rot.z)
        
        self.label_1.text = f"Camera Position: {_cam_pos}"
        self.label_2.text = f"Camera Rotation: {_cam_rot}"
        
        
        
        yaw = self.camera.rot.x * math.pi / 180
        forward = vec3(-math.sin(yaw), math.cos(yaw), 0)
        right = vec3(math.cos(yaw), math.sin(yaw), 0)
        forward_point = self.node_center.pos + forward * 0.1
        right_point = self.node_center.pos + right * 0.1
        
        self.line_manager.update_line("foward", points=[self.node_center.pos.to_tuple(),
                                                        forward_point.to_tuple()],
                                       color=(1, 1, 0, 1), thickness=2.0)
        self.line_manager.update_line("right", points=[self.node_center.pos.to_tuple(),
                                                        right_point.to_tuple()],
                                       color=(1, 1, 0, 1), thickness=2.0)
        
        
        
        
        self.label_x.pos = self.get_object_screen_pos(self.node_x._geometry)
        self.label_y.pos = self.get_object_screen_pos(self.node_y._geometry)
        self.label_z.pos = self.get_object_screen_pos(self.node_z._geometry)
        
        
        
        return task.cont



if __name__ == '__main__':
    BasicScene().run()