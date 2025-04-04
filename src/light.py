from .vec import vec3, vec4
from panda3d.core import PointLight



class Light:
    def __init__(self, pos:vec3, color:vec4, render):
        
        self._pos = pos
        
        plight = PointLight('plight')
        plight.setColor(color.to_tuple())
        self.light_np = render.attachNewNode(plight)
        self.light_np.setPos(pos.x, pos.y, pos.z)
        render.setLight(self.light_np)
        
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, value:vec3):
        self._pos = value
        self.light_np.setPos(value.x, value.y, value.z)