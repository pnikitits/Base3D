from .vec import vec3



class Node:
    def __init__(self,
                 geometry,
                 render,
                 pos: vec3=vec3(0, 0, 0),
                 rot: vec3=vec3(0, 0, 0),
                 scale: vec3=vec3(1, 1, 1)):
        
        self._geometry = geometry
        self._geometry.reparentTo(render)
        
        self._pos = pos
        self._rot = rot
        self._scale = scale
        
        
    
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, value):
        self._pos = value
        self._geometry.setPos(value.x, value.y, value.z)
        
    @property
    def rot(self):
        return self._rot
    
    @rot.setter
    def rot(self, value):
        self._rot = value
        self._geometry.setHpr(value.x, value.y, value.z)
        
    @property
    def scale(self):
        return self._scale
    
    @scale.setter
    def scale(self, value):
        self._scale = value
        self._geometry.setScale(value.x, value.y, value.z)