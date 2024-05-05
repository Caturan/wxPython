import wx 

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='HeLLo')
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


"""
    Python 3 recommends using super() when working
    with classes. The built-in super() function’s primary purpose in wxPython is used for referring to
    the parent class without actually naming it
"""