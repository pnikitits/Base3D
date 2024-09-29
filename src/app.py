from direct.showbase.ShowBase import ShowBase



class App(ShowBase):

    def setup(self, frame_rate: int, renderer: callable):
        ShowBase.__init__(self)
        self.taskMgr.doMethodLater(delayTime=1/frame_rate, funcOrTask=renderer,name='renderer')