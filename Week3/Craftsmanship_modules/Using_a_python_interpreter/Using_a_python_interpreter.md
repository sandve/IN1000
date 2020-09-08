# Using the Python Interpreter


## 1. What is the Python Interpreter?
So far you have learned to make a Python script and to run this script by calling it from the terminal. If you quickly want to test out short pieces of Python code, an alternative solution is to use the [Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html). This is an interactive environment where you can type in Python code which immediately runs. 

## 2. Starting the Interpreter

In most cases, the Python Interpreter can be started simply by typing `python` or `python3` in the terminal*. Use the same python command that you would normally use when running a script. If everything works correctly**, you should see something like this:


    my-computer:~ user$ python3
    Python 3.7.6 (default, Dec 30 2019, 19:38:28) 
    [Clang 11.0.0 (clang-1100.0.33.16)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 


<sub>
* Python 2 is deprecated, so you should be using Python 3. On some computers only one of the two versions is installed, and on some computers both. The version number is printed in the first line when starting the Python Interpreter, and can otherwise also be found by running `python --version` or `python3 --version` in the terminal.
</sub>

\
<sub>
** If the Python Interpreter does not automatically start, refer to this manual about [Invoking the Interpreter](https://docs.python.org/3/tutorial/interpreter.html#invoking-the-interpreter)
</sub>



## 3. Coding in the Interpreter


You can now start typing code! If you write an expression, the result of this expression will immediately be printed to the next line, for example:


    >>> 2 + 10 * 4
    42
    >>> my_string = "Hello world!"
    >>> my_string * 3
    'Hello world!Hello world!Hello world!'
    >>> 5 > 10
    False
    >>> animal = input("what is your favorite animal? ")
    what is your favorite animal? Hedgehog
    >>> animal
    'Hedgehog'
    >>>

Variables that are declared in the interpreter will stay available throughout the rest of the session. It is also possible to execute multi-line commands such as if/else statements, loops or procedures/functions. The interpreter will recognize when you are typing a multi-line statement, and start the line with `...`, for example:

    >>> if animal == "giraffe":
    ...     "I like giraffes too!" # note that it is not necessary to type print()
    ... else:
    ...     "oh, I prefer giraffes"
    ... 
    'oh, I prefer giraffes'
    >>> 

When writing multi-line statements, only the current line can be edited and previous lines can not be changed. 

To repeat lines of code, the up and down arrows can be used to scroll through the previously written lines. 

To exit the Python Interpreter, just write `exit()`. 

## 4. When is it useful to use the Python interpreter?

The Python Interpreter is not the appropriate tool for writing big programs, but it is very useful for playing around with code where you are not sure what will happen, or if you are just curious if something is possible. For example, if I write `a = print(2+3)`, will this code give an error? And if not, what will `a` be? With the interpreter we can quickly check this:

    >>> a = print(2+3)
    5   
    >>> print(a)
    None

It turns out the code does not give an error, and `a` is None!

Another reason to use the interpreter is if you want to work with some objects or functions that you haven't used before, and you want to test them out to check if you are calling them properly. For example, we may want to test how to use the `append` functionality for lists. 

    >>> my_list = [1,2,3]
    >>> my_long_list = my_list.append(4)
    >>> my_list
    [1, 2, 3, 4]
    >>> my_long_list
    >>> print(my_long_list)
    None
    >>>   

By testing this, we see that `append` modifies the original variable `my_list`, and the new variable `my_long_list` contains nothing. 

The interpreter is also a great tool to test out small pieces of code that you need inside a larger program. For example if you are writing a very difficult expression or procedure, and you want to make sure your code is running without errors. Let's say we want to write a procedure that asks the user for their favorite animal, and it tells the user if the length of the set of characters in the animal name is even. In the interpreter, we can build this code one step at a time and see what happens at each step:


    >>> animal = "Hedgehog"
    >>> set(animal)
    {'H', 'g', 'h', 'd', 'o', 'e'}
    >>> # I see both 'H' and 'h' occur in the set, let's fix that
    >>> set(animal.lower())
    {'g', 'h', 'd', 'o', 'e'}
    >>> len(set(animal.lower()))
    5
    >>> # the modulo operator can be used to see if something is divisible by 2
    >>> 1 % 2 # not divisible
    1
    >>> 2 % 2 # divisible
    0
    >>> 4 % 2 # divisible
    0
    >>> # now let's add all the pieces together 
    >>> len(set(animal.lower())) % 2 
    1
    >>> len(set(animal.lower())) % 2 == 0
    False
    >>> def test_animal_name():
    ...     animal = input("What is your favorite animal? ")
    ...     if len(set(animal.lower())) % 2 == 0:
    ...         print("Set of characters divisible by two!")
    ...     else:
    ...         print("Set of characters is NOT divisible by two!")
    ...              
    >>> test_animal_name()
    What is your favorite animal? Hedgehog
    Set of characters is NOT divisible by two!


