from src.app import App
from src.node import Node
from src.primitive import *
from src.hud import label
from src.vec import vec2, vec3, vec4
from src.light import Light
from src.camera import Camera
from src.skybox import Skybox
from panda3d.core import ClockObject



class BasicScene(App):

    def __init__(self):
        super().__init__(frame_rate=60, renderer=self.renderer, show_fps=True, show_world_origin=True)
        self.time = 0
        
        Skybox(app=self, path="../assets/textures/Skybox_2", size=20)
        self.camera = Camera(self, pos=vec3(1.02, -2.21, 0.75), rot=vec3(20, -10, 0))
        
        
        self.light_1 = Light(pos=vec3(0.001, 0.001, 0.001), color=vec4(1,1,1,1), render=self.render)


        
        self.node = Node(geometry=sphere(self, radius=1, color=vec4(1, 0, 0, 1)),
                         render=self.render, pos=vec3(1.0, 1.0, 0),
                         scale=vec3(0.05, 0.05, 0.05))
        self.node_2 = Node(geometry=sphere(self, radius=1, color=vec4(0, 1, 0, 1)),
                           render=self.render, pos=vec3(1.0, 1.0, 0),
                           scale=vec3(0.02, 0.02, 0.02))
        

    def renderer(self, task):
        """Update the scene"""    
        self.time += ClockObject.getGlobalClock().getDt()
        if self.time > 10000:
            self.time = 0
            
        self.node.pos = self.compute_pos_on_circle(centre=vec3(0, 0, 0), radius=1, angle=(self.time / 5) * 2 * math.pi)
        self.node_2.pos = self.compute_pos_on_circle(centre=self.node.pos, radius=0.1, angle=(self.time / 1) * 2 * math.pi)
            
        self.app_updates()
        return task.cont
    
    
    @staticmethod
    def compute_pos_on_circle(centre:vec3, radius:float, angle:float):
        """Compute the position on a circle given the centre, radius, and angle"""
        x = centre.x + radius * math.cos(angle)
        y = centre.y + radius * math.sin(angle)
        return vec3(x, y, centre.z)



if __name__ == '__main__':
    BasicScene().run()