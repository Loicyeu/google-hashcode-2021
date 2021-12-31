# Class Singleton from StackOverflow : https://stackoverflow.com/a/6798042/16027155
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Writer(metaclass=Singleton):

    def __init__(self):
        self.filename = 'solution1.txt'
        self.engineerTasks = dict()  # Key = Engineer number, Value = List of their tasks (i.e. ['wait 1', 'impl bar 1'])

    def addTask(self, engineerNumber, task):
        if engineerNumber in self.engineerTasks.keys():
            self.engineerTasks[engineerNumber].append(task)
        else:
            self.engineerTasks[engineerNumber] = [task]

    def writeToFile(self):
        with open(self.filename, 'w') as f:
            f.write(str(len(self.engineerTasks)) + "\n")
            for key in self.engineerTasks:
                tasks = self.engineerTasks[key]
                f.write(str(len(tasks)) + "\n")
                for task in tasks:
                    f.write(task + "\n")


if __name__ == '__main__':
    w = Writer()
    w.addTask(1, 'wait 1')
    w.addTask(1, 'impl bar 1')
    w.addTask(2, 'wait 2')
    print(w.engineerTasks)
    w.writeToFile()
