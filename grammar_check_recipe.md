
# Grammar Check Function Design Recipe


## 1. Describe the Problem

> As a user so that I can improve my grammar,
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature


```python
# EXAMPLE

def grammar_check(text):
    """Checks that a string starts with a capital letter
       and ends in a valid punctuation mark 

    Parameters: 
        text: a string (e.g. "Hello World!")

    Returns: 
        a boolean value, True if valid, False if not

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
     
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string that starts with capital
and ends in a valid punctuation mark
It returns True
"""
grammar_check("Hello world.") => True
grammar_check("Hello world!") => True
grammar_check("Hello world?") => True

"""
Given a string that starts with capital
and ends without a valid punctuation mark
but still a punctuation 
It returns False
"""
grammar_check("HELLO WORLD,") => False
grammar_check("HELLO WORLD:") => False

"""
Given a string that starts with capital
and ends without a punctuation mark
It returns False
"""
grammar_check("HELLO WORLD") => False


"""
Given a string that starts with lowercase
but ends with a valid punctuation mark
It returns False
"""
grammar_check("hELLO WORLD!") => False

"""
Given an invalid input
It raises Exception
"""
grammar_check("") => Exception
grammar_check(5) => Exception
```

## 4. Implement the Behaviour


