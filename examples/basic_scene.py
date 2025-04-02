from src.app import App
from src.node import Node
from src.primitive import sphere
from src.hud import text
from src.vec import vec2, vec3, vec4
from src.light import Light
from src.camera import Camera
from src.skybox import Skybox


class BasicScene(App):

    def __init__(self):
        self.setup(frame_rate=60, renderer=self.renderer)
        
        self.camera = Camera(self, pos=vec3(0.22, 0.33, 2.02))
        self.setup_inputs()
        self.light_1 = Light(pos=vec3(1,1,1), color=vec4(1,1,1,1), render=self.render)
        
        
        # Center of the scene with axis lines
        _line_size = 0.5
        self.line_manager.make_line("line_x", points=[(0,0,0), (_line_size,0,0)], color=(1, 0, 0, 1), thickness=2.0)
        self.line_manager.make_line("line_y", points=[(0,0,0), (0,_line_size,0)], color=(0, 1, 0, 1), thickness=2.0)
        self.line_manager.make_line("line_z", points=[(0,0,0), (0,0,_line_size)], color=(0, 0, 1, 1), thickness=2.0)
        self.node_center = Node(geometry=sphere(self, radius=0.01), render=self.render)
        
        
        
        self.label_1 = text(text="placeholder", pos=vec2(0, 0), size=0.1, align='center')
        self.label_2 = text(text="placeholder", pos=vec2(0, 0.1), size=0.1, align='center')
        skybox = Skybox(app=self, path="/Users/pierrenikitits/Documents/GitHub/Base3D/assets/textures/Skybox", size=20)
        

    def renderer(self, task):
        
        _cam_pos = self.camera._camera.getPos()
        _cam_pos = vec3(_cam_pos.x, _cam_pos.y, _cam_pos.z)
        _cam_rot = self.camera._camera.getHpr()
        _cam_rot = vec3(_cam_rot.x, _cam_rot.y, _cam_rot.z)
        
        self.label_1.text = f"Camera Position: {_cam_pos}"
        self.label_2.text = f"Camera Rotation: {_cam_rot}"
        
        return task.cont



if __name__ == '__main__':
    BasicScene().run()