# Asserting assumptions

## 1. Testing assumptions by printing

While programming we constantly make assumptions. One way to check whether those assumptions are met is by printing out some variables to see if they match our expectation. 

Imagine a company that sends out birthday cards to its customers. The company has set up an automatic system for this. However, the information that is available on the customers has been acquired in various ways, and it might contain some errors. So, before sending the post card, the customer information needs to be checked. 
The first field to check is whether someone has filled in a valid age, which must be a positive number of at most 120.  Furthermore, the street number must be above 0, and the postal code must be a number between 0000 and 9999. The information is stored in the variables `age` and `street_number` which are integers, and `postal_code` which is a string. We can print all of these fields out:

    print(age)
    print(street_number)
    print(postal_code)
    
...and by running this program with the first 3 customers in the system we may see:

    53
    12
    8609
    17
    130
    495
    34
    1
    3950
    
How long does it take you to check whether all printed numbers are valid? This quickly becomes unmanageable when we have to read through the customer information of tens or hundreds of customers...
Perhaps a better solution would be to directly print whether our assumptions are true:

    print(120 >= age >= 0)
    print(street_number > 0)
    print(len(postal_code) == 4 and 9999 >= int(postal_code) >= 0) 
    
which shows us:

    True
    True
    True
    True
    True
    False
    True
    True
    True

It can now immediately be seen that one of the fields is incorrect, although it still requires some digging to find out what the problem was. 

## 2. Assert statements

With a larger program having a lot of print statements can become very confusing. Furthermore, unexpected values typically mean there is a bug in your program, and it is better to stop the program execution immediately to show the failed assumption, rather than waiting for the program to crash at a later point or produce a strange output. 
 
A better alternative for quickly testing your assumptions is through *assert statements*. We can assert that the street number is above 0 like this:

    assert street_number > 0

If `street_number` is indeed above 0, nothing happens and the program continues executing. But if `street_number` for some reason is negative, an assertion error is raised:

    Traceback (most recent call last):
      File "my_program.py", line 3, in <module>
        assert counter > 0
    AssertionError


In some cases it may be useful to show a bit more information about what went wrong. An optional error message can be added to your assert statement like so:

    assert street_number > 0, "Street number must be above 0"

which raises:

    Traceback (most recent call last):
      File "my_program.py", line 2, in <module>
        assert street_number > 0, "Street number must be above 0"
    AssertionError: Number of sheep can not be negative


## 3. More complex expressions

Assert statements are not limited to simple expressions, any valid boolean expression can be used. We can for example assert the other two examples presented in section 1: 

    assert 120 >= age >= 0, "Age must be between 0 and 120"
    assert len(postal_code) == 4 and 9999 >= int(postal_code) >= 0, "The postal code must be 4 characters long and be a number between 0 and 9999"
    


## 3. One last note
While assert statements are a useful debugging tool to quickly test your assumptions, they should not be used to write important error messages to the user in a real life setting. A proper error message is produced by *raising an exception*, but that will be taught in a later course. 
