from .vec import vec3, vec4
from panda3d.core import Geom, GeomNode, GeomVertexData, GeomVertexFormat, GeomTriangles, GeomVertexWriter, Material
import math



def model(app, path:str):
    """Loads a model from a file"""
    model = app.loader.loadModel(path)
    return model
    

def sphere(app,
           radius: float,
           subdivisions: int = 12,
           color: vec4 = vec4(1, 1, 1, 1)):
    """Creates a procedural sphere geometry with normals and a material"""
    # vertex data structure (with normals)
    format = GeomVertexFormat.getV3n3()
    vdata = GeomVertexData("sphere", format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")

    vertices = [] # vertex indices
    indices = [] # triangle indices (for mesh connectivity)
    
    # vertices, normals generation
    for i in range(subdivisions + 1):
        theta = math.pi * i / subdivisions # angle from north pole
        for j in range(subdivisions + 1):
            phi = 2 * math.pi * j / subdivisions # angle around the equator
            x = radius * math.sin(theta) * math.cos(phi)
            y = radius * math.sin(theta) * math.sin(phi)
            z = radius * math.cos(theta)
            vertex.addData3(x, y, z)
            normal.addData3(x, y, z) # normal is the same as the position for a unit sphere
            vertices.append(len(vertices))
    
    # triangle indices generation
    for i in range(subdivisions):
        for j in range(subdivisions):
            i1 = i * (subdivisions + 1) + j
            i2 = i1 + 1
            i3 = i1 + (subdivisions + 1)
            i4 = i3 + 1
            
            # two triangles for each grid cell
            indices.append((i1, i2, i4))
            indices.append((i1, i4, i3))
    
    # GeomTriangles object and add triangles
    triangles = GeomTriangles(Geom.UHStatic)
    for tri in indices:
        triangles.addVertices(*tri)
        triangles.closePrimitive()

    # Geom object and attach it to a GeomNode
    geom = Geom(vdata)
    geom.addPrimitive(triangles)
    node = GeomNode("sphere")
    node.addGeom(geom)

    sphere_np = app.render.attachNewNode(node)

    # material
    material = Material()
    material.setDiffuse(color.to_tuple())
    material.setShininess(20)
    sphere_np.setMaterial(material, 1)
    sphere_np.setTwoSided(True)

    return sphere_np



def cube(app,
         size: vec3,
         pos: vec3 = vec3(0, 0, 0),
         color: vec4 = vec4(1, 1, 1, 1)):
    """Creates a procedural cube geometry with normals and a material"""
    # vertex data structure (with normals)
    format = GeomVertexFormat.getV3n3()
    vdata = GeomVertexData("cube", format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")

    # half-sizes for positioning
    hw, hh, hd = size.x / 2, size.y / 2, size.z / 2


    vertices = [
        (vec3(-hw, -hh, -hd), vec3(0, 0, -1)), # back face
        (vec3(hw, -hh, -hd), vec3(0, 0, -1)),
        (vec3(hw, hh, -hd), vec3(0, 0, -1)),
        (vec3(-hw, hh, -hd), vec3(0, 0, -1)),

        (vec3(-hw, -hh, hd), vec3(0, 0, 1)), # front face
        (vec3(hw, -hh, hd), vec3(0, 0, 1)),
        (vec3(hw, hh, hd), vec3(0, 0, 1)),
        (vec3(-hw, hh, hd), vec3(0, 0, 1)),

        (vec3(-hw, -hh, -hd), vec3(-1, 0, 0)), # left face
        (vec3(-hw, hh, -hd), vec3(-1, 0, 0)),
        (vec3(-hw, hh, hd), vec3(-1, 0, 0)),
        (vec3(-hw, -hh, hd), vec3(-1, 0, 0)),

        (vec3(hw, -hh, -hd), vec3(1, 0, 0)), # right face
        (vec3(hw, hh, -hd), vec3(1, 0, 0)),
        (vec3(hw, hh, hd), vec3(1, 0, 0)),
        (vec3(hw, -hh, hd), vec3(1, 0, 0)),

        (vec3(-hw, hh, -hd), vec3(0, 1, 0)), # top face
        (vec3(hw, hh, -hd), vec3(0, 1, 0)),
        (vec3(hw, hh, hd), vec3(0, 1, 0)),
        (vec3(-hw, hh, hd), vec3(0, 1, 0)),

        (vec3(-hw, -hh, -hd), vec3(0, -1, 0)), # bottom face
        (vec3(hw, -hh, -hd), vec3(0, -1, 0)),
        (vec3(hw, -hh, hd), vec3(0, -1, 0)),
        (vec3(-hw, -hh, hd), vec3(0, -1, 0)),
    ]

    
    for v, n in vertices:
        v = v + pos # offset vertices by position
        vertex.addData3(v.x, v.y, v.z)
        normal.addData3(n.x, n.y, n.z)

    # define cube faces using indices (counterclockwise winding order)
    faces = [
        (0, 1, 2), (0, 2, 3), # back
        (4, 6, 5), (4, 7, 6), # front
        (8, 9, 10), (8, 10, 11), # left
        (12, 13, 14), (12, 14, 15), # right
        (16, 17, 18), (16, 18, 19), # top
        (20, 21, 22), (20, 22, 23), # bottom
    ]

    triangles = GeomTriangles(Geom.UHStatic)
    for tri in faces:
        triangles.addVertices(*tri)
        triangles.closePrimitive()

    geom = Geom(vdata)
    geom.addPrimitive(triangles)
    node = GeomNode("cube")
    node.addGeom(geom)

    cube_np = app.render.attachNewNode(node)

    # material
    material = Material()
    material.setDiffuse(color.to_tuple())
    material.setShininess(20)
    cube_np.setMaterial(material, 1)
    cube_np.setTwoSided(True)

    return cube_np
    


def cylinder(radius: float, height: float, pos: vec3):
    pass

def cone(radius: float, height: float, pos: vec3):
    pass

def torus(radius: float, thickness: float, pos: vec3):
    pass

def plane(app):
    path = "../assets/models/plane.obj"
    plane = app.loader.loadModel(path)
    return plane

def quad(size: vec3, pos: vec3):
    pass

def line(start: vec3, end: vec3):
    pass