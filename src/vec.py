class vec2:
    def __init__(self, x: float, y: float):
        """
        Create a 2D vector
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)
    
    
class vec3:
    def __init__(self, x: float, y: float, z: float):
        """
        Create a 3D vector
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return vec3(self.x * other, self.y * other, self.z * other)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def normalize(self):
        length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return vec3(self.x / length, self.y / length, self.z / length)
    

class vec4:
    def __init__(self, x: float, y: float, z: float, w: float):
        """
        Create a 4D vector
        """
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    
    def __sub__(self, other):
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)