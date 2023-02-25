from Controller import Controller
from Model import Model


class Task:

    def __init__(self):
        Controller(Model).main()


if __name__ == '__main__':
    Task()
