# This is a list of the functions that I want to implement in the project.


class vec2:
    def __init__(self, x, y):
        pass


class vec3:
    def __init__(self, x, y, z):
        pass


class vec4:
    def __init__(self, x, y, z, w):
        pass


class Node:
    def __init__(self, pos: vec3, rot: vec3, scale: vec3, parent=None):
        pass
        

class Skybox:
    def __init__(self, path: str):
        pass


class Camera:
    def __init__(self, pos:vec3, rot:vec3):
        pass


class Light:
    def __init__(self, pos:vec3, color:vec3):
        pass


class Line:
    def __init__(self, start: vec3, end: vec3):
        pass


class Primitive:
    def sphere():
        pass

    def cube():
        pass

    def cylinder():
        pass

    def cone():
        pass

    def torus():
        pass

    def plane():
        pass

    def quad():
        pass


class Hud:
    def __init__(self):
        pass

    def text(text: str, pos: vec2, size: int):
        pass

    def image(path: str, pos: vec2, size: vec2):
        pass


class App:
    def __init__(self):
        pass

    def setup():
        pass

    def update():
        pass