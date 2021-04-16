from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import PaginaInicial 

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(PaginaInicial.PaginaInicial)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
app = SampleApp()
app.mainloop()

