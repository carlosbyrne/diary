MD TEMPLATE CLASSES:

# TodoList Class Design Recipe


## 1. Describe the Problem

>As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

>As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToDo:
    

    def __init__(self):
        self.__tasks = []

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass

    def view(self):
        # Returns:
        #   A list of tasks the user has yet to mark as complete
        # Side-effects:
        #   Throws an exception if no tasks
        pass # No code here yet

    def mark_complete(self, completed_task):
        # Returns:
        #   A confirmation message the task was completed
        # Side-effects:
        #   Throws an exception if the task to complete can not be found
        #   If task can be found in task list, task is deleted from task list object
            
        
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
.view() allows the user to see uncomplete tasks
"""
todo = ToDo()
todo.add("Walk the dog")
todo.view() => ["Walk the dog"]

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
