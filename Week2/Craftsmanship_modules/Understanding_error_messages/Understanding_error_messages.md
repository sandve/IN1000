# Understanding error messages

The text in this module heavily borrows from [The Python Tutorial chapter 8: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).

## 1. Types of errors



There are three types of errors: *syntax errors*, *runtime errors* and *logic errors*. Syntax and runtime errors are easy to detect, as they will show you an error message. Logic errors are more hidden; they do not give an error message but instead result in a wrong output of your program. In this module the focus will only be on reading and understanding error messages. 

### 1.1 Syntax errors
Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python: 

    >>> while True print('Hello world')
      File "<stdin>", line 1
        while True print('Hello world')
                   ^
    SyntaxError: invalid syntax
    
The parser repeats the line where the error was found, and displays a little 'arrow' pointing at the earliest point in the line where the error was detected. The error is thus caused by something written before the arrow: in this example, the error is detected at the function print(), since a colon (':') is missing before it. 

Because the arrow only shows where the error was detected, this means that in some cases the error may even be on the previous line, such as in this example:

    # contents of my error.py script
    def procedure():
        print("Hello world"

    procedure()

which gives the error:

      File "error.py", line 4
        procedure()
                ^
    SyntaxError: invalid syntax

because of the missing bracket of the print statement. 

### 1.2 Runtime errors


Even if an expression is syntactically correct, it may still cause an error when attempting to execute it. *Runtime errors* are errors that come up during the execution ('running') of a program. In Python, these errors are called Exceptions. There exist a lot of different [built in Python exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions), here are some examples you may have encountered:



    >>> 10 * (1/0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    >>> 4 + spam*3
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'spam' is not defined
    >>> '2' + 2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly


The last line of the error message describes what went wrong. The preceding part of the error message shows the context where the error happened, in the form of a *stack traceback*. The stack traceback will contain a listing of where in the program the error occurs (the line number and function calls). For example, this script: 

    # contents of traceback.py
    def inner():
        10 / 0

    def outer():
        inner()

    outer()
    
will print the following stack traceback:

    Traceback (most recent call last):
      File "traceback.py", line 7, in <module>
        outer()
      File "traceback.py", line 5, in outer
        inner()
      File "traceback.py", line 2, in inner
        arg / 0
    ZeroDivisionError: division by zero

Notice that the further you go down the stack traceback, the closer you come to the place where the error occurred. 
The stack traceback is useful to look at when your program is large and the same functions are called multiple times. 


## 2. Try it yourself!

The best way to learn to deal with errors and exceptions is to solve them yourself! Relevant trix exercises are: [02.22](https://trix.ifi.uio.no/assignments/446), [02.23](https://trix.ifi.uio.no/assignments/448), [03.15](https://trix.ifi.uio.no/assignments/877), [07.07](https://trix.ifi.uio.no/assignments/644).

## 3. Some final notes

- Logic errors do not give you an error message. Such bugs are usually a lot more difficult to solve. It is important to always test pieces of code to make sure they function as you expect them to! 

- Instead of letting the program crash, it is possible to handle an exception directly (if this exception occurs, do that) using [try and except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions), but this will be taught in a later course. 





