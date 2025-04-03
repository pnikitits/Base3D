from src.app import App
from src.node import Node
from src.primitive import sphere
from src.hud import label
from src.vec import vec2, vec3, vec4
from src.light import Light
from src.camera import Camera
from src.skybox import Skybox



class BasicScene(App):

    def __init__(self):
        self.setup(frame_rate=60, renderer=self.renderer)
        Skybox(app=self, path="/Users/pierrenikitits/Documents/GitHub/Base3D/assets/textures/Skybox", size=20)
        self.camera = Camera(self, pos=vec3(1.02, -2.21, 0.75), rot=vec3(20, -10, 0))
        self.light_1 = Light(pos=vec3(1,1,1), color=vec4(1,1,1,1), render=self.render)
        self.add_world_origin()
        self.debug_labels()
        
        self.node = Node(geometry=sphere(self, radius=0.1), render=self.render, pos=vec3(0.5, 0.5, 0))


    def renderer(self, task):
        self.update_debug_labels()
        self.update_world_origin()
        return task.cont



if __name__ == '__main__':
    BasicScene().run()