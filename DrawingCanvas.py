from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
from tkinter.simpledialog import *
import numpy as np

class DrawingCanvas(Canvas):

    def __init__(self, p, w, h, bg):
        Canvas.__init__(self,master = p,width=w, height=h, bg=bg)
        self.globalAnnotationColor = "red"
        self.globalLineWidth = 3
        self.currentDrawingImage = 0

        # drawingMode attribute: 0 means not drawing. 1 means draw line.
        # 2 means draw arrow.  4 means draw circle
        self.drawingMode = 0

        self.firstClick = None
        self.secondClick = None


    def drawComponent(self):
        if self.drawingMode == 1:
            self.DrawLine()
        elif self.drawingMode ==2:
            self.DrawArrow()
        elif self.drawingMode == 4:
            self.DrawCircle()


        self.firstClick = None
        self.secondClick = None
        self.drawingMode = 0

    def DrawLine(self):
        x1 = self.firstClick[0]
        y1 = self.firstClick[1]
        x2 = self.secondClick[0]
        y2 = self.secondClick[1]

        return self.create_line(x1, y1, x2, y2, width=self.globalLineWidth,fill=self.globalAnnotationColor)

    def DrawArrow(self):

        x1 = self.firstClick[0]
        y1 = self.firstClick[1]
        x2 = self.secondClick[0]
        y2 = self.secondClick[1]

        a1 = x2 + 0.15 * ((x1 - x2) * 0.8660 + (y1 - y2) * 0.5)
        b1 = y2 + 0.15 * ((y1 - y2) * 0.8660 - (x1 - x2) * 0.5)
        a2 = x2 + 0.15 * ((x1 - x2) * 0.8660 - (y1 - y2) * 0.5)
        b2 = y2 + 0.15 * ((y1 - y2) * 0.8660 + (x1 - x2) * 0.5)

        return self.create_line(x1, y1, x2, y2, width=self.globalLineWidth,fill=self.globalAnnotationColor), self.create_line(a1, b1, x2, y2, width=self.globalLineWidth,fill=self.globalAnnotationColor), self.create_line(a2, b2, x2, y2, width=self.globalLineWidth,fill=self.globalAnnotationColor)




    def DrawCircle(self):
        # Task 1-a : Please install 'numpy' module to operate in your environment.
        x1 = self.firstClick[0]
        y1 = self.firstClick[1]
        x2 = self.secondClick[0]
        y2 = self.secondClick[1]
        r = np.sqrt(np.square(x2-x1)+np.square(y2-y1))
        a1 = x1 - r
        b1 = y1 - r
        a2 = x1 + r
        b2 = y1 + r
        return self.create_oval(a1, b1, a2, b2, width=self.globalLineWidth, fill="",
                                     outline=self.globalAnnotationColor)

    def DrawImage(self, filename):
        if(self.currentDrawingImage>0):
            self.delete(self.currentDrawingImage)

        file = PIL.Image.open(filename)
        file = file.resize((300,300))

        image = ImageTk.PhotoImage(file)

        self.currentDrawingImage = self.create_image(0,0, anchor=NW, image = image)
        self.image = image


    def changeLineWidth(self):
        newvalue = askinteger("New Line Width","The current line width is "+str(self.globalLineWidth)+". Please enter new value")
        if newvalue > 0:
            self.globalLineWidth = newvalue

    def ChangeAnnotationColor(self):
        a = askstring("Ask message","Please insert a color (e.g. red, blue, green, gray, black, white, purple ...)")
        self.globalAnnotationColor = str(a)
        return None
