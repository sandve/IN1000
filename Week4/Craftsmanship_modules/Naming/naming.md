# Naming  


## 1. Naming conventions

Python allows a lot of freedom in how you name variables and 
 objects, but not every name is a good name. 
 Using consistent and common naming conventions makes it easier to identify whether some name refers to a variable, class, function or something else. 

In this course we aim to follow the naming conventions from the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) - although the book uses a different naming style. The most important thing is that you choose one style and use it consistently throughout a script or project. A style guide is not a harsh rule that must be followed at all times, but it is good to familiarize yourself with it and follow the guidelines unless there is a good reason not to. 

According to the PEP8 style guide, variable names and function names should be written `lowercase_with_underscores` (functions can be distinguished from variables by their brackets), whereas class names are written in `CamelCase` with capitalized acronyms (e.g. `HTTPServerError`). For more naming conventions check the link above. 

## 2. Good practices in variable naming

### 2.1 Length

When it comes to names, there is a trade-off between conciseness and informativeness. When names are too short (e.g. single characters or abbreviated words), it might not be clear what a variable means:

    u = 1234

but too much information also impairs readability:

    personal_unique_user_identification_number = 1234
    
a happy medium here could be:

    user_id = 1234

As an exercise, try reading through the following three scripts: one script that uses [too short variable names](sm.py), one that uses [too long variable names](script_that_makes_a_smoothie_based_on_user_specified_fruits.py), and one that uses [medium-length variable names](smoothie_maker). How do the variable names impact your ability to understand what is happening?

There is no golden rule for how long a variable name should be, but it is more common to write too short (not understandable) variable names rather than too long. 


Some short variable names become understandable because they are used by almost everyone. For example, the name `i` is often used as an index variable inside a loop:

    for i in [1, 2, 3, 4, 5]:
        print(i ** 2)
        
        
If you struggle to come up with a concise and meaningful name for a function, it might mean that your function has too many responsibilities, and that it should be split up into multiple functions. E.g the function `read_student_grades_and_calculate_average_grade()` could be split into `read_grades_from_file()` and `calculate_average()`. 


### 2.2 Descriptiveness and meaning

Besides the length of the variable name, aim to use meaningful variable names. A name like `list1` does not explain much about the purpose of this list (and it is even worse when `list1` actually is a dictionary!), instead try to give a more descriptive name such as `student_names` or `grades`. A general thought to keep in mind is that someone else (or yourself a year from now) should be able to understand what the variables in your code mean. 

It is usually a good idea for the names of functions (including procedures and methods) to be verbs, whereas the names of variables, classes and parameters should be nouns. This way the code reads more like human language, and it is easy to see that a function does something, whereas a variable is something. 
So the following example:

    file = read_file(file_path)
    display_content(file)

is better than: 

    contains_file = filereader(is_file_path)
    content_displayer(contains_file)





### 2.3 Avoiding existing names

There exist some [reserved keywords](https://www.tutorialspoint.com/What-are-Reserved-Keywords-in-Python) that have a specific meaning in Python and can therefore not be used as the name of a variable. These words include `def`, `and`, `return` and many more. Assignment to a reserved keyword results in a SyntaxError:

    >>> and = 42
      File "<stdin>", line 1
        and = 42
          ^
    SyntaxError: invalid syntax


Conversely, there exist [built-in functions](https://docs.python.org/3/library/functions.html#func-list), like `print()`, `input()` and `range()`, which can be overwritten. This is bad practice and must be avoided, as it may result in unintended consequences if another part of the code is dependant on this function, and it makes the code more confusing to read. For example, when `print` is overwritten by a string, it can not be used for printing anymore:

    >>> print("hello, print works like normal!")
    hello, print works like normal!
    >>> print = "some string"
    >>> print("hello world!")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object is not callable

Depending on your editor built-in functions may be highlighted, which gives you a hint that another name should be used. 

### 2.4 Other things to avoid

Although it is technically possible to use certain special characters like æ, ø and å in variable names, it is better to avoid these characters because in rare cases encoding issues can arise. And names that can easily be misread as another character (`O`, `l`, `I`) should never be used as names. 
