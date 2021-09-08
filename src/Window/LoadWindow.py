from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import time

from src.Window.MainWindow import MainWindow


class LoadWindow:
    progress = None
    loadWindow = Tk()

    def __init__(self):
        width_of_window = 427
        height_of_window = 250

        screen_width = self.loadWindow.winfo_screenwidth()
        screen_height = self.loadWindow.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.loadWindow.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        self.loadWindow.overrideredirect(1)

        # ProgressBar
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
        self.progress = Progressbar(self.loadWindow, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate')
        self.progress.place(x=-10, y=235)

        Frame(self.loadWindow, width=427, height=241, bg='#249794').place(x=0, y=0)
        #b1 = Button(self.w, width=10, height=1, text='JOUER', command=self.bar, border=0, fg='#249794')
        #b1.place(x=170, y=200)

        l1 = Label(self.loadWindow, text="DONJON & DRAGON", fg='white', bg='#249794')
        lst1 = ('Calirbi (Body)', 18, 'bold')
        l1.config(font=lst1)
        l1.place(x=50, y=80)

        l2 = Label(self.loadWindow, text="V1", fg='white', bg='#249794')
        lst2 = ('Calirbi (Body)', 10)
        l2.config(font=lst2)
        l2.place(x=300, y=100)

        l3 = Label(self.loadWindow, text="Premier Sang", fg='white', bg='#249794')
        lst3 = ('Calirbi (Body)', 13)
        l3.config(font=lst3)
        l3.place(x=50, y=110)

        l4 = Label(self.loadWindow, text='Loading...', fg='white', bg='#249794')
        lst4 = ('Calirbi (Body)', 10)
        l4.config(font=lst4)
        l4.place(x=0, y=210)

        r = 0
        for i in range(100):
            print('test')
            self.progress['value'] = r
            self.loadWindow.update_idletasks()
            time.sleep(0.03)
            r = r + 1
        #self.loadWindow.destroy()
        #mainWindow = MainWindow()

        self.loadWindow.mainloop()