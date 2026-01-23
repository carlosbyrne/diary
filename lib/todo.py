class ToDo:
    def __init__(self):
        self.__tasks = []

    def add(self, task):
        self.__tasks.append(task)
        return f"{task} added to to-do list."

    def view(self):
        if not self.__tasks:
            raise Exception("Nothing to do!")
        return self.__tasks

    def mark_complete(self, completed_task):
        if completed_task not in self.__tasks:
            raise Exception(f"{completed_task}, could not be found in to-do list.")
        self.__tasks.remove(completed_task)
        return f"{completed_task} has been marked as complete!"
        