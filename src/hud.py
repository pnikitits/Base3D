from .vec import vec2, vec4
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from typing import Literal



def text(text: str='',
         pos: vec2=vec2(0, 0),
         size: float=0.1,
         color: vec4=vec4(1, 1, 1, 1),
         background: vec4=vec4(0, 0, 0, 0),
         align: Literal['left', 'center', 'right']='left'):
    
    if align == 'left':
        align = TextNode.ALeft
    elif align == 'center':
        align = TextNode.ACenter
    elif align == 'right':
        align = TextNode.ARight
    
    text = OnscreenText(text=text,
                        pos=(pos.x, pos.y),
                        scale=size,
                        fg=color.to_tuple(),
                        bg=background.to_tuple(),
                        align=align)
    return text


def image(self, path: str, pos: vec2, size: vec2):
    pass


def line(self, start: vec2, end: vec2):
    pass