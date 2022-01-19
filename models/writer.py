from typing import Optional


class Singleton(type):
    """
    Represent a Singleton, that allow a Class to have only one instance even if we call the constructor to have a new one.

    Class Singleton from StackOverflow : https://stackoverflow.com/a/6798042/16027155
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Writer(metaclass=Singleton):
    """
    Represent the writer for the exit file.
    """

    def __init__(self):
        """
        Create the Writer only once and then give the instance already created.
        """
        self.filename = 'solutions/solution.txt'
        # Key = Engineer number, Value = List of their tasks (i.e. ['wait 1', 'impl bar 1'])
        self.engineerTasks = dict()

    def addTask(self, engineerId, task):
        """
        Add a task done by an engineer to the buffer engineerTasks.

        :param engineerId: The id of the engineer
        :param task: The task done by the engineer, pre-formated and ready to print in the file
        """
        if engineerId in self.engineerTasks.keys():
            self.engineerTasks[engineerId].append(task)
        else:
            self.engineerTasks[engineerId] = [task]

    def writeToFile(self, filename: Optional[str] = None):
        """
        Write the buffer in the exit file.

        :param filename: The name of the file, None for default name.
        """
        with open(filename or self.filename, 'w') as f:
            f.write(str(len(self.engineerTasks)) + "\n")
            for key in self.engineerTasks:
                tasks = self.engineerTasks[key]
                f.write(str(len(tasks)) + "\n")
                for task in tasks:
                    f.write(task + "\n")
        self.reset()

    def reset(self):
        """
        Delete and reset the buffer.
        """
        self.engineerTasks = dict()
