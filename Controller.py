from tkinter import filedialog
from View import View
import tkinter as tk


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)
        self.file_types = (('text files', '*.txt'), ('All files', '*.*'))

    def choose_name_file(self):
        name_file = filedialog.askopenfilename(filetypes=self.file_types)
        if name_file:
            with open(name_file, encoding='utf-8') as f:
                self.model.names = [line.strip() for line in f]
                self.view.window_names.delete(0, tk.END)
            for name in self.model.names:
                self.view.window_names.insert(tk.END, name)

    def choose_tasks_file(self):
        task_file = filedialog.askopenfilename(filetypes=self.file_types)
        if task_file:
            with open(task_file, encoding='utf-8') as f:
                self.model.tasks = [line.strip() for line in f]
                self.view.window_tasks.delete(0, tk.END)
            for tasks in self.model.tasks:
                self.view.window_tasks.insert(tk.END, tasks)

    def mix(self):
        self.view.window_mix.delete(0, tk.END)
        self.save = list(self.model.mixing(self.model))
        for names, tasks in self.save:
            self.view.window_mix.insert(tk.END, f'{names} - {tasks}')

    def save_new_file(self):
        savefile = filedialog.asksaveasfilename(filetypes=self.file_types, defaultextension='generated.txt')
        if savefile:
            with open(savefile, 'w', encoding='utf-8') as f:
                for names, tasks in self.save:
                    f.write(f'{names} - {tasks}\n')

    def main(self):
        self.view.main()
