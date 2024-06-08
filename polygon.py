from tkinter import *
class Polygon:
    def__init__(self):
    fill_color="blue"
    self.main_window=Tk()
    self.canvas=Canvas(self.main_window,height=200,width=150)
    self.canvas.create_polygon(60,20,100,140,100,100,140,60,140,20,100,20,60,fill=fill_color)
    self.canvas.pack()
    self.main_window.mainloop()
Polygon.object=Polygon()
        
