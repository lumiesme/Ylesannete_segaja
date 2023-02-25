import tkinter.messagebox
import random


class Model:

    def __init__(self, names, tasks):
        self.names = names
        self.tasks = tasks

    def mixing(self):
        if len(self.names) > len(self.tasks):
            tkinter.messagebox.showwarning(title='Teade!',
                                           message='Failis ei jätku iga õpilase jaoks ülesandeid. \n Vali uus fail!')

            return []

        else:
            random.shuffle(self.tasks)
            answer = [(names, tasks) for names, tasks in zip(self.names, self.tasks)]

            return answer
