from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter import filedialog

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from PIL import ImageTk, Image

from DrawingCanvas import DrawingCanvas
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from PIL import *
import ImageFiltering2
import Histogramgenerator
from Calculations import *

class GUI_geonuk():

    def __init__(self):
        self.window = Tk()
        self.filepath = None
        self.SEM_Image = None
        self.SEM_Image_ArrayRemoved = None
        self.SEM_Image_Filtered = None
        self.canvas = None
        self.canvas2 = None
        self.canvas3 = None
        self.drawingCanvas = None
        self.f_plot = None
        self.Histogram_SEM_Filtered = None
        self.porosity = None
        self.IronPortion = None
        self.IronOxPortion = None
        self.GanguePortion = None
        self.DRIStrength = None
        self.calculus = None


    def newFilePressed(self):
        messagebox.showinfo("New File", "Hi, you clicked new File")

    def openFilePressed(self):

        filepath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        #clear the initial canvas
        self.drawingCanvas = DrawingCanvas(self.window, 500, 300, "white")
        self.drawingCanvas.grid(row = 0, column= 0, columnspan = 4,  rowspan = 6)

        self.filepath = filepath
        self.SEM_Image = plt.imread(filepath)
        self.SEM_Image_ArrayRemoved = self.SEM_Image[:350, :400]

        f = plt.figure(figsize = (5,3), dpi = 100)
        self.f_plot = f.add_subplot(111)
        self.f_plot.imshow(self.SEM_Image_ArrayRemoved)
        self.canvas = FigureCanvasTkAgg(f, master = self.drawingCanvas)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill = BOTH, expand = 1)
        toolbar = NavigationToolbar2Tk(self.canvas, self.drawingCanvas)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, self.canvas, toolbar)

        self.canvas.mpl_connect("key_press_event", on_key_press)

    def saveFilePressed(self):
        savefilepathandname = filedialog.asksaveasfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        print(savefilepathandname)
    def saveAsPressed(self):
        print("Save As")
    def exitPressed(self):
        self.window.quit()
    def aboutPressed(self):
        print("This is a test software for lecture 5")

    def ImageFilteringPressed(self):
        answer = simpledialog.askstring("Input","Please type '1' for gaussian filtration, '2' for median filtration")

        print(answer, type(answer))

        if answer == "1":
            self.SEM_Image_Filtered = ImageFiltering2.GausianFiltration(self.SEM_Image_ArrayRemoved)

            self.drawingCanvas2 = DrawingCanvas(self.window, 500, 300, "white")
            self.drawingCanvas2.grid(row=8, column=0, columnspan=4, rowspan=6)

            f = plt.figure(figsize=(5, 3), dpi=100)
            self.f_plot2 = f.add_subplot(111)
            self.f_plot2.imshow(self.SEM_Image_Filtered)
            self.canvas2 = FigureCanvasTkAgg(f, master=self.drawingCanvas2)
            self.canvas2.draw()
            self.canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            toolbar = NavigationToolbar2Tk(self.canvas2, self.drawingCanvas2)
            toolbar.update()
            self.canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

            #Histogram generation
            self.Histogram_SEM_Filtered = Histogramgenerator.histogramgenerator(self.SEM_Image_Filtered)
            self.drawingCanvas3 = DrawingCanvas(self.window, 400, 300, "white")
            self.drawingCanvas3.grid(row=8, column=4, columnspan=4, rowspan=6)
            f = plt.figure(figsize=(4, 3), dpi=100)
            self.f_plot3 = f.add_subplot(111)
            self.f_plot3.plot(np.arange(256), self.Histogram_SEM_Filtered, color='green')
            self.canvas3 = FigureCanvasTkAgg(f, master=self.drawingCanvas3)
            self.canvas3.draw()
            self.canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            toolbar = NavigationToolbar2Tk(self.canvas3, self.drawingCanvas3)
            toolbar.update()
            self.canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


            a,b,c,d = DRIcalculations(self.Histogram_SEM_Filtered)
            self.porosity = a * 100
            self.GanguePortion = b  * 100
            self.IronOxPortion = c  * 100
            self.IronPortion = d  * 100


        if answer == "2":
            self.SEM_Image_Filtered = ImageFiltering2.MedianFiltration(self.SEM_Image_ArrayRemoved)

            self.drawingCanvas2 = DrawingCanvas(self.window, 500, 300, "white")
            self.drawingCanvas2.grid(row=8, column=0, columnspan=4, rowspan=6)

            f = plt.figure(figsize=(5, 3), dpi=100)
            self.f_plot2 = f.add_subplot(111)
            self.f_plot2.imshow(self.SEM_Image_Filtered)
            self.canvas2 = FigureCanvasTkAgg(f, master=self.drawingCanvas2)
            self.canvas2.draw()
            self.canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            toolbar = NavigationToolbar2Tk(self.canvas2, self.drawingCanvas2)
            toolbar.update()
            self.canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

            #Histogram generation
            self.Histogram_SEM_Filtered = Histogramgenerator.histogramgenerator(self.SEM_Image_Filtered)
            self.drawingCanvas3 = DrawingCanvas(self.window, 400, 300, "white")
            self.drawingCanvas3.grid(row=8, column=4, columnspan=4, rowspan=6)
            f = plt.figure(figsize=(4, 3), dpi=100)
            self.f_plot3 = f.add_subplot(111)
            self.f_plot3.plot(np.arange(256), self.Histogram_SEM_Filtered, color='green')
            self.canvas3 = FigureCanvasTkAgg(f, master=self.drawingCanvas3)
            self.canvas3.draw()
            self.canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            toolbar = NavigationToolbar2Tk(self.canvas3, self.drawingCanvas3)
            toolbar.update()
            self.canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


            a,b,c,d = DRIcalculations(self.Histogram_SEM_Filtered)
            self.porosity = a * 100
            self.GanguePortion = b  * 100
            self.IronOxPortion = c  * 100
            self.IronPortion = d  * 100


    def CalcPorosity(self):

        if str(type(self.Histogram_SEM_Filtered)) == "<class 'numpy.ndarray'>":

            Result_Porosity = Label(self.window, text="= " + str(int(self.porosity)) + "%", bg = "white")
            Result_Porosity.grid(row=1, column=5, padx=10, pady=10, ipadx = 30, sticky=W)
            messagebox.showinfo("Calculate Porosity", "Calculation Successfully Finished")
        else:
            messagebox.showinfo("Do filtration first", "Do Image Filteration First")



    def CalcIronPortion(self):
        if str(type(self.Histogram_SEM_Filtered)) == "<class 'numpy.ndarray'>":

            Result_IronPortion = Label(self.window, text="= " + str(int(self.IronPortion)) + "%", bg = "white")
            Result_IronPortion.grid(row=2, column=5, padx=10, pady=10, ipadx = 30, sticky=W)
            messagebox.showinfo("Calcualte Iron Portion", "Calculation Successfully Finished")
        else:
            messagebox.showinfo("Do filtration first", "Do Image Filteration First")



    def CalcIronOxPortion(self):
        if str(type(self.Histogram_SEM_Filtered)) == "<class 'numpy.ndarray'>":

            Result_IronOxPortion = Label(self.window, text="= " + str(int(self.IronOxPortion)) + "%", bg = "white")
            Result_IronOxPortion.grid(row=3, column=5, padx=10, pady=10, ipadx = 30, sticky=W)
            messagebox.showinfo("Calculate Iron Oxide Portion", "Calculation Successfully Finished")
        else:
            messagebox.showinfo("Do filtration first", "Do Image Filteration First")




    def CalcGanguePortion(self):
        if str(type(self.Histogram_SEM_Filtered)) == "<class 'numpy.ndarray'>":

            Result_GanguePortion = Label(self.window, text="= " + str(int(self.GanguePortion)) + "%", bg = "white")
            Result_GanguePortion.grid(row=4, column=5, padx=10, pady=10, ipadx = 30, sticky=W)
            messagebox.showinfo("Calculate Gangue Portion","Calculation Successfully Finished")
        else:
            messagebox.showinfo("Do filtration first", "Do Image Filteration First")




    def CalcStrength(self):

        self.DRIStrength = 60*(100 - 0.8* self.porosity - 0.2 * self.GanguePortion + 0.2* self.IronOxPortion)/100
        Result_DRIStrength = Label(self.window, text = "= "+str(int(self.DRIStrength)) + " kgf/pellet", bg = "white")
        Result_DRIStrength.grid(row=5, column = 5, padx = 10, pady = 10, ipadx= 30, sticky = W)
        messagebox.showinfo("Calculate Strength","Calculation Successfully Finished")


    def drawLinePressed(self):
        self.drawingCanvas.drawingMode = 1

    def drawArrowPressed(self):
        self.drawingCanvas.drawingMode = 2

    def drawCirclePressed(self):
        self.drawingCanvas.drawingMode = 4
    def clearTheCanvas(self):
        self.drawingCanvas = DrawingCanvas(self.window, 500, 300, "white")
        self.drawingCanvas.grid(row=0, column=0, columnspan=4, rowspan=6)
        self.drawingCanvas.delete("all")
    def canvasClicked(self,event):
        if self.drawingCanvas.drawingMode >0:
            if self.drawingCanvas.firstClick == None:
                self.drawingCanvas.firstClick = [event.x, event.y]
            else:
                self.drawingCanvas.secondClick = [event.x, event.y]
                self.drawingCanvas.drawComponent()

    def changeLineWidthPressed(self):
        self.drawingCanvas.changeLineWidth()

    def changeLineColorPressed(self):
        self.drawingCanvas.ChangeAnnotationColor()


    def createComponents(self):

        self.window.title('DRI Back-scattered Electron Image ANALYZER')
        self.window.geometry("900x700")

        self.drawingCanvas = DrawingCanvas(self.window, 500, 300, "white")
        # self.drawingCanvas = DrawingCanvas(self.window, 350, 400, "white")
        self.drawingCanvas.grid(row = 0, column= 0, columnspan = 4,  rowspan = 6)
        self.drawingCanvas.bind("<Button-1>", self.canvasClicked)

        self.ImageFilteringButton = Button(self.window,text="Image Filtering",command=self.ImageFilteringPressed)
        self.ImageFilteringButton.grid(row=0, column = 4, padx = 10, pady = 10, sticky = W)

        self.ImageFilteringButton = Button(self.window,text="Calculate Porosity",command=self.CalcPorosity)
        self.ImageFilteringButton.grid(row=1, column = 4, padx = 10, pady = 10, sticky = W)

        self.ImageFilteringButton = Button(self.window,text="Calculate Portion of Iron",command=self.CalcIronPortion)
        self.ImageFilteringButton.grid(row=2, column = 4, padx = 10, pady = 10, sticky = W)

        self.ImageFilteringButton = Button(self.window,text="Calculate Portion of Iron Oxide",command=self.CalcIronOxPortion)
        self.ImageFilteringButton.grid(row=3, column = 4, padx = 10, pady = 10, sticky = W)

        self.ImageFilteringButton = Button(self.window,text="Calculate Portion of Gangue",command=self.CalcGanguePortion)
        self.ImageFilteringButton.grid(row=4, column = 4, padx = 10, pady = 10, sticky = W)

        self.ImageFilteringButton = Button(self.window,text="Calculate Strength",command=self.CalcStrength)
        self.ImageFilteringButton.grid(row=5, column = 4, padx = 10, pady = 10, sticky = W)


    def createMenu(self):
        # Creating an empty menu bar
        menubar = Menu(self.window)
        self.window.config(menu=menubar)  # ....... need to follow this...

        # Adding new items to menu bar
        fileMenu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=fileMenu)

        # Adding new menu items under this File menu..
        fileMenu.add_command(label="New File", command=self.newFilePressed)
        fileMenu.add_command(label="Open File", command=self.openFilePressed)
        fileMenu.add_command(label="Save File", command=self.saveFilePressed)
        fileMenu.add_command(label="Save as", command=self.saveAsPressed)

        # add a seperator to divide the menu to portions..
        fileMenu.add_separator()

        # add a command to exit the program
        fileMenu.add_command(label="Exit", command=self.exitPressed)

        # Add another menu item
        aboutMenu = Menu(fileMenu, tearoff=False)
        fileMenu.add_cascade(label="about", menu=aboutMenu)
        aboutMenu.add_command(label="ABOUT THIS SOFTWARE", command=self.aboutPressed)

        annotationMenu = Menu(menubar)
        menubar.add_cascade(label="Annotation", menu=annotationMenu)
        annotationMenu.add_command(label="Clear Canvas", command=self.clearTheCanvas)
        annotationMenu.add_command(label="Draw Line", command=self.drawLinePressed)
        annotationMenu.add_command(label="Draw Arrow", command=self.drawArrowPressed)
        annotationMenu.add_command(label="Draw Circle", command=self.drawCirclePressed)
        annotationMenu.add_separator()
        annotationMenu.add_command(label="Change Line Width", command=self.changeLineWidthPressed)
        annotationMenu.add_command(label="Change Line Color", command=self.changeLineColorPressed)





