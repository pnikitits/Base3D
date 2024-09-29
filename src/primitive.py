from .vec import vec3



def sphere(self, radius: float):
    # Load a model for now, will implement a sphere primitive later
    path = "/Users/pierrenikitits/Documents/GitHub/Base3D/assets/models/sphere.obj"
    sphere = self.loader.loadModel(path)
    sphere.setScale(radius)
    return sphere
    

def cube(size: vec3, pos: vec3):
    pass

def cylinder(radius: float, height: float, pos: vec3):
    pass

def cone(radius: float, height: float, pos: vec3):
    pass

def torus(radius: float, thickness: float, pos: vec3):
    pass

def plane(size: vec3, pos: vec3):
    pass

def quad(size: vec3, pos: vec3):
    pass

def line(start: vec3, end: vec3):
    pass