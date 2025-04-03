from .vec import vec3



class Camera:
    def __init__(self,
                 app,
                 pos: vec3 = vec3(0, 0, 5),
                 rot: vec3 = vec3(0, 0, 0),
                 lookAt: vec3 = vec3(0, 0, 0)):
        self._pos = pos
        self._lookAt = lookAt

        app.disableMouse()
        self._camera = app.camera
        self._camera.setPos(pos.x, pos.y, pos.z)
        # self._camera.lookAt(lookAt.x, lookAt.y, lookAt.z)
        self._camera.setHpr(rot.x, rot.y, rot.z)
        self._rot = rot

        self._camLens = app.camLens
        self._camLens.setNear(0.1)
        self._camLens.setFar(100.0)
        
        
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self._camera.setPos(value.x, value.y, value.z)

    # @property
    # def lookAt(self):
    #     return self._lookAt
    
    # @lookAt.setter
    # def lookAt(self, value):
    #     self._lookAt = value
    #     self._camera.lookAt(value.x, value.y, value.z)

    @property
    def rot(self):
        # Always fetch the latest rotation values from the camera
        return vec3(self._camera.getH(), self._camera.getP(), self._camera.getR())

    @rot.setter
    def rot(self, value):
        
        # Clamp rotation values to 0-360 degrees
        if value.x >= 360:
            value.x -= 360
        elif value.x < 0:
            value.x += 360
        
        if value.y >= 360:
            value.y -= 360
        elif value.y < 0:
            value.y += 360
            
        if value.z >= 360:
            value.z -= 360
        elif value.z < 0:
            value.z += 360
        
            
        self._rot = value
        self._camera.setHpr(value.x, value.y, value.z)