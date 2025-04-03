from .camera import Camera
from .node import Node
from .vec import vec3
import math


def input_manager(key: str, node: Node|Camera):
        
    movement_speed = 0.01
    rotation_speed = 0.15
    
    yaw = node.rot.x * math.pi / 180  # Convert to radians
    forward = vec3(-math.sin(yaw), math.cos(yaw), 0)
    right = vec3(math.cos(yaw), math.sin(yaw), 0)

    if key == "d":
        node.pos = node.pos + right * movement_speed  # Move right
    elif key == "q":
        node.pos = node.pos - right * movement_speed  # Move left
    elif key == "r":
        node.pos = node.pos + vec3(0, 0, movement_speed)  # Move up
    elif key == "f":
        node.pos = node.pos - vec3(0, 0, movement_speed)  # Move down
    elif key == "z":
        node.pos = node.pos + forward * movement_speed  # Move forward
    elif key == "s":
        node.pos = node.pos - forward * movement_speed  # Move backward
        
    elif key == "a":
        node.rot = node.rot + vec3(rotation_speed, 0, 0)  # Rotate left (yaw)
    elif key == "e":
        node.rot = node.rot - vec3(rotation_speed, 0, 0)  # Rotate right (yaw)