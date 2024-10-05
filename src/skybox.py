from .primitive import plane
import os
from panda3d.core import TextureStage



class Skybox:
    def __init__(self, app, path: str, size: float):
        
        names = [
            'top',
            'bottom',
            'right',
            'left',
            'front',
            'back'
        ]
        
        positions = [
            (0, 0, size),
            (0, 0, -size),
            (size, 0, 0),
            (-size, 0, 0),
            (0, size, 0),
            (0, -size, 0)
        ]
        
        rotations = [
            (0, -90, 0),
            (0, 90, 0),
            (90, 0, 180),
            (-90, 0, 180),
            (-180, 0, 180),
            (0, 0, 180)
        ]
        
        self._planes = []
        for i in range(1,7):
            name = f"{names[i-1]}.png"
            texture = app.loader.loadTexture(os.path.join(path, name))
            plane_i = plane(app)
            base_ts = TextureStage('base_ts')
            base_ts.setMode(TextureStage.MReplace)
            plane_i.setTexture(base_ts, texture)
            plane_i.setScale(size)
            plane_i.setPos(positions[i-1])
            plane_i.setHpr(rotations[i-1])
            plane_i.reparentTo(app.render)
            self._planes.append(plane_i)