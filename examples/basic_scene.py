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
        
        self.camera = Camera(self)
        self.light_1 = Light(pos=vec3(1,1,1), color=vec4(1,0,0,1), render=self.render)
        self.node_1 = Node(geometry=sphere(self, radius=0.1), render=self.render)
        # label_1 = text(text="Hello, World!", pos=vec2(0, 0), size=0.1, align='center')
        skybox = Skybox(app=self, path="/Users/pierrenikitits/Documents/GitHub/Base3D/assets/textures/Skybox", size=20)
        

    def renderer(self, task):
        return task.cont



if __name__ == '__main__':
    BasicScene().run()