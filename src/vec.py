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
    
    def to_tuple(self):
        return (self.x, self.y)
    
    
class vec3:
    def __init__(self, x: float, y: float, z: float):
        """
        Create a 3D vector
        """
        self._x = x
        self._y = y
        self._z = z
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value: float):
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value: float):
        self._y = value
        
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value: float):
        self._z = value
        
    def __add__(self, other: 'vec3'):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'vec3'):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other: float):
        return vec3(self.x * other, self.y * other, self.z * other)
    
    def dot(self, other: 'vec3'):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: 'vec3'):
        return vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def normalize(self):
        length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return vec3(self.x / length, self.y / length, self.z / length)
    
    def __str__(self):
        return f"vec3({self.x}, {self.y}, {self.z})"
    
    def to_tuple(self):
        return (self.x, self.y, self.z)
    

class vec4:
    def __init__(self, x: float, y: float, z: float, w: float):
        """
        Create a 4D vector
        """
        self._x = x
        self._y = y
        self._z = z
        self._w = w
    
    # Position properties 
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value: float):
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value: float):
        self._y = value
        
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value: float):
        self._z = value
        
    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, value: float):
        self._w = value
        
    # Color properties
    @property
    def r(self):
        return self._x
    
    @r.setter
    def r(self, value: float):
        self._x = value
        
    @property
    def g(self):
        return self._y
    
    @g.setter
    def g(self, value: float):
        self._y = value
        
    @property
    def b(self):
        return self._z
    
    @b.setter
    def b(self, value: float):
        self._z = value
        
    @property
    def a(self):
        return self._w
    
    @a.setter
    def a(self, value: float):
        self._w = value
        
        
    def __add__(self, other):
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    
    def __sub__(self, other):
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    
    def __str__(self) -> str:
        return f"vec4({self.x}, {self.y}, {self.z}, {self.w})"
    
    def to_tuple(self) -> tuple:
        return (self.x, self.y, self.z, self.w)