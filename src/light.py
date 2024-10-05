from .vec import vec3, vec4
from panda3d.core import PointLight



class Light:
    def __init__(self, pos:vec3, color:vec4, render):
        
        plight = PointLight('plight')
        plight.setColor(color.to_tuple())
        light_np = render.attachNewNode(plight)
        light_np.setPos(pos.x, pos.y, pos.z)
        render.setLight(light_np)