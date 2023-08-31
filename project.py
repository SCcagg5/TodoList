import os, json
from datetime import datetime
from ics import Calendar, Event

class Task:
    def __init__(self, title, priority, due_date, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = (datetime.strptime(due_date, "%Y-%m-%d").date()
                        if isinstance(due_date, str) else due_date)
        self.completed = completed

    def __str__(self):
        due_date_str = (self.due_date.strftime("%Y-%m-%d") if self.due_date else "N/A")
        status = "✓" if self.completed else " "
        return f"[{status}] (Due: {due_date_str}, Priority: {self.priority}) {self.title}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                self.tasks = [Task(**task_data) for task_data in json.load(f)]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        tasks_data = [{"title": task.title, "priority": task.priority,
                       "due_date": (task.due_date.strftime("%Y-%m-%d") if task.due_date else None),
                       "completed": task.completed}
                      for task in self.tasks]
        with open("tasks.json", "w") as f:
            json.dump(tasks_data, f)

    def list_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: (x.due_date, x.priority))
        for idx, task in enumerate(sorted_tasks, start=1):
            print(f"{idx}. {task}")

    def add_task(self, title, priority, due_date=None):
        self.tasks.append(Task(title, priority, due_date))
        self.save_tasks()

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number!")

    def export_to_ics(self, filename="tasks.ics"):
        c = Calendar()
        for task in self.tasks:
            if task.due_date:
                e = Event()
                e.name = task.title
                e.begin = task.due_date
                if task.completed:
                    e.status = "COMPLETED"
                c.events.add(e)

        with open(filename, "w") as f:
            f.writelines(c)
        print("Tasks exported to", filename)

class Input:
    class check:
        @staticmethod
        def choice(value):
            if value not in ["1", "2", "3", "9"]:
                raise ValueError
            return value

        @staticmethod
        def title(value):
            if not (0 < len(value) < 60):
                raise ValueError
            return value

        @staticmethod
        def priority(value):
            if value not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise ValueError
            return int(value)

        @staticmethod
        def due_date(value):
            try:
                value = datetime.strptime(value, "%Y-%m-%d")
            except:
                raise ValueError
            return value

    def __init__(self):
        self.data = {"priority": {"text": "Enter task priority (1 to 9): ", "wrong": None, "func": self.check.priority},
                     "title": {"text": "Enter task title: ", "wrong": "Title should be between 1 and 59 char long",
                               "func": self.check.title},
                     "due_date": {"text": "Enter due date (YYYY-MM-DD): ", "wrong": None, "func": self.check.due_date},
                     "choice": {"text": "Enter your choice: ", "wrong": None, "func": self.check.choice}}

    def value(self, type):
        value = ""
        while True:
            value = input(self.data[type]["text"])
            try:
                self.data[type]["func"](value)
                break
            except ValueError:
                if self.data[type]["wrong"] is not None:
                    print(self.data[type]["wrong"])
        return value


def clear_screen(test = False):
    if not test:
        os.system('cls' if os.name == 'nt' else 'clear')
    return 0

def print_menu(tl, test = False):
    if not test:
        clear_screen()
    if test:
        tl = TodoList()
        tl.load_tasks()
    tl.list_tasks()

    if not test:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. Export to ICS")
        print("9. Exit")
    return 0

def choice_menu(tl, test = False):
    if not test:
        choice = Input().value("choice")
    else:
        choice = "9"

    if choice == "1":
        title = Input().value("title")
        priority = Input().value("priority")
        due_date = Input().value("due_date")
        tl.add_task(title, priority, due_date)
    elif choice == "2":
        task_number = int(input("Enter task number to mark as completed: "))
        tl.mark_task_completed(task_number)
    elif choice == "3":
        tl.export_to_ics()
    elif choice == "9":
        print("Goodbye!")
        exit()
    return 0

def main():
    tl = TodoList()
    tl.load_tasks()

    while True:
        print_menu(tl)
        choice_menu(tl)

if __name__ == "__main__":
    main()
