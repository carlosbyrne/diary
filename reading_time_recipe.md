
# Estimate Reading Time Function Design Recipe


## 1. Describe the Problem

>As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

```python
# EXAMPLE

def estimate_reading_time(text):
    """ Estimates reading time for a piece of text
        based on a presumption the user reads at 200 
        words per minute 

    Parameters: 
        text: a string containing words (e.g. "hello world")

    Returns: 
        a float, (e.g. 1.0)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string of 200 words
It returns 1.0
"""
words = "word " * 200
estimate_reading_time(words) => 1.0

"""
Given a string of 400 words
It returns 2.0
"""
words = "word " * 400
estimate_reading_time(words) => 2.0

"""
Given a string of 300 words
It returns 1.5
"""
words = "word " * 300
estimate_reading_time(words) => 1.5

"""
Given an empty string
Or incorrect type
It raises an Exception
"""
empty = ''
integer = 1
estimate_reading_time(empty) => Exception
estimate_reading_time(integer) => Exception
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

