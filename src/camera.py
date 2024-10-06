from .vec import vec3



class Camera:
    def __init__(self, app, pos: vec3=vec3(1, 1, 1), lookAt: vec3=vec3(0, 0, 0)):
        
        self._pos = pos
        self._lookAt = lookAt
        
        app.disableMouse()
        self._camera = app.camera
        self._camera.setPos(pos.x, pos.y, pos.z)
        self._camera.lookAt(lookAt.x, lookAt.y, lookAt.z)
        
        self._camLens = app.camLens
        self._camLens.setNear(0.1)
        self._camLens.setFar(100.0)
        
        self._rot = vec3(self._camera.getH(), self._camera.getP(), self._camera.getR())
        
        
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, value):
        self._pos = value
        self._camera.setPos(value.x, value.y, value.z)
        
    @property
    def lookAt(self):
        return self._lookAt
    
    @lookAt.setter
    def lookAt(self, value):
        self._lookAt = value
        self._camera.lookAt(value.x, value.y, value.z)
        
    @property
    def rot(self):
        return self._rot
    
    @rot.setter
    def rot(self, value):
        self._rot = value
        self._camera.setHpr(value.x, value.y, value.z)