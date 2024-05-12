import wx 

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        button = wx.Button(self, label='Press Me')

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='HeLLo')
        panel = MyPanel(self)
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()