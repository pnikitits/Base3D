from .vec import vec2, vec4
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from typing import Literal



class label:
    def __init__(self,
                 text: str='',
                 pos: vec2=vec2(0, 0),
                 size: float=0.1,
                 color: vec4=vec4(1, 1, 1, 1),
                 background: vec4=vec4(0, 0, 0, 0),
                 align: Literal['left', 'center', 'right']='left',
                 parent=None):
        
        if align == 'left':
            align = TextNode.ALeft
        elif align == 'center':
            align = TextNode.ACenter
        elif align == 'right':
            align = TextNode.ARight
            
        self._text = text
        self._pos = pos
            
        self._label = OnscreenText(
            text=text,
            pos=(pos.x, pos.y),
            scale=size,
            fg=color.to_tuple(),
            bg=background.to_tuple(),
            align=align,
            parent=parent
        )
        
    @property
    def pos(self):
        return self._pos
        
    @pos.setter
    def pos(self, value: vec2):
        self._pos = value
        self._label.setPos(value.x, value.y)
    
    @property
    def text(self):
        return self._text
        
    @text.setter
    def text(self, value: str):
        self._text = value
        self._label.setText(value)
        
    def hide(self):
        self._label.hide()
        
    def show(self):
        self._label.show()