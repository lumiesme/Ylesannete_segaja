import tkinter.font as tkfont
from tkinter import *  # tkinterit kasutad selleks, et näha graafiliselt kogu mängu
import tkinter as tk


class View(Tk):

    def __init__(self, controller, model):
        super().__init__()     # super on selleks, et kasutame Tk interit, et saaks kogu sisu kasutada
        self.controller = controller
        self.model = model
        self.geometry('1200x700')
        self.title('Ülesannete jagaja')
        self.resizable(False, False)
        self.configure(bg='#EEDFCC')
        self.default_font_style = tkfont.Font(family='Verdana', size=10)
        self.big_font_style = tkfont.Font(family='Verdana', size=14, weight='bold')
        self.frame_base, self.frame1 = self.create_frames()
        self.btn2, self.btn3, self.btn4, self.savebtn = self.create_all_buttons()
        self.base, self.lbl_names, self.lbl_tasks, self.lbl_namesandtasks = self.create_all_labels()
        self.window_names, self.window_tasks, self.window_mix = self.windows()

    def main(self):
        self. mainloop()

    def create_frames(self):
        self.frame_base = Frame(self, bg="#CDB79E", height=50, width=1200)
        self.frame_base.pack(side=TOP)
        self.frame1 = Frame(self, bg="#EEDFCC", width=1200, height=630)
        self.frame1.pack(side=TOP)

        return self.frame_base, self.frame1  # meetod tagastab 2 asja, method return objects

    def create_all_buttons(self):

        self.btn2 = tk.Button(self.frame1, text='Vali nimede fail', font=self.default_font_style,
                              command=self.controller.choose_name_file, height=1, width=30)
        self.btn2.place(x=60, y=15, in_=self.frame1)

        self.btn3 = tk.Button(self.frame1, text='Vali ülesannete fail', font=self.default_font_style,
                              command=self.controller.choose_tasks_file, height=1, width=30)
        self.btn3.place(x=400, y=15, in_=self.frame1)

        self.btn4 = tk.Button(self.frame1, text='Sega omavahel nimed ja ülesanded', font=self.default_font_style,
                              command=self.controller.mix, height=1, width=30)
        self.btn4.place(x=800, y=15, in_=self.frame1)

        self.savebtn = tk.Button(self.frame1, text='Salvesta fail', font=self.default_font_style,
                                 command=self.controller.save_new_file, height=1, width=10)
        self.savebtn.place(x=1100, y=590, in_=self.frame1)

        return self.btn2, self.btn3, self.btn4, self.savebtn

    def create_all_labels(self):
        self.base = Label(self.frame_base, bg='#CDB79E', text='Nimede ja ülesannete segaja',
                          font=self.big_font_style).place(x=450, y=10)
        self.lbl_names = Label(self.frame1, text='Nimed', anchor='w',
                               font=self.default_font_style)
        self.lbl_tasks = Label(self.frame1, text='Ülesanded', anchor='w',
                               font=self.default_font_style)
        self.lbl_namesandtasks = Label(self.frame1, text='Segatud nimed ja ülesanded', anchor='w',
                                       font=self.default_font_style)

        return self.base, self.lbl_names, self.lbl_tasks, self.lbl_namesandtasks  # tagastamine

    def windows(self):
        self.window_names = tk.Listbox(self.frame1, width=50, height=33)
        self.window_names.place(x=35, y=50)
        self.window_tasks = tk.Listbox(self.frame1, width=50, height=33)
        self.window_tasks.place(x=370, y=50)
        self.window_mix = tk.Listbox(self.frame1, width=80, height=33)
        self.window_mix.place(x=700, y=50)

        return self.window_names, self.window_tasks, self.window_mix
