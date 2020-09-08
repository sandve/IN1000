# Writing tests for functions

## 1. Why is it good to write tests?
When you write a big program, it is very likely that at some point a bug will occur. The earlier you find those bugs, the better. One way to automatically detect bugs in your code is to write 'testing functions' which test whether some other piece of code behaves as it should. For simplicity, the testing functions will in this document be called 'tests', while 'functions' refers to the actual functions that your program consists of. 

Ideally, a function has a clear purpose and returns one value. This makes functions very good candidates for automatic tests. If you ever change some part of your code (for example: changing to a more efficient algorithm, or adding extra functionalities), tests will show if you did not accidentally break the old functionality of your code. 
Another advantage of those tests is that they provide examples of how your functions should be used. It is a good practice to at least have tests for the most complicated functions in your program, since those are most likely to contain mistakes.



## 1. How to write tests?

Before we write a function, we already know what we intend our function to do. Writing the test for a function is usually a lot easier than writing the function itself, and in some cases it may help to get the thinking process started about how we actually want to implement the function. It is therefore recommended to write the test before you write the actual function. Doing so also stimulates you to think about the 'border cases', e.g., what should happen when your function is called with unexpected arguments (such as a negative number or empty string).

The test simply calls the function with some parameters, and checks whether the resulting output matches the expected output using an *assert statement*. A good practice is to name your test functions 'test_' followed by the name of the function you are testing. 

As an example, consider the function `make_acronyms`. The purpose of this function is to make an acronym out of a phrase. It should use the first character of each word, but only if it is capitalized. This means that the phrase "Bed and Breakfast" should get the acronym "BB". Before implementing `make_acronyms`, we can already fill in its test:


    def make_acronyms(phrase):
        #todo fill in this function
        return ""
        
    def test_make_acronyms(phrase):
        result_acronym = make_acronyms("Bed and Breakfast")
        correct_acronym = "BB"
        assert result_acronym == correct_acronym, "Expected acronym " + correct_acronym + " but found " + result_acronym
        
        # border case: all-caps words
        result_acronym = make_acronyms("HELLO WORLD")
        correct_acronym = "HW"
        assert result_acronym == correct_acronym, "Expected acronym " + correct_acronym + " but found " + result_acronym
        
        # border case: no capital words
        result_acronym = make_acronyms("hello world")
        correct_acronym = ""
        assert result_acronym == correct_acronym, "Expected acronym " + correct_acronym + " but found " + result_acronym
        

Use hardcoded values (numbers, strings) in the test, instead of copying pieces code from your function. The latter practice can result in you copying over a buggy piece of code. Consider this example of a wrongly implemented square function:

    def square(number):
        return number ** number
        
    def test_square_wrong():
        for number in [1,2,3,4,5,6,7,8,9,10]:
            result_square = square(number)
            correct_square = number ** number
            assert result_square == correct_square, "Expected square " + correct_square + " but found " + result_square
    
    def test_square_correct():
        result_square = square(1)
        correct_square = 1
        assert result_square == correct_square, "Expected square " + correct_square + " but found " + result_square
        
        result_square = square(5)
        correct_square = 25
        assert result_square == correct_square, "Expected square " + correct_square + " but found " + result_square

The correct implementation would be `number * number` or `number ** 2`, but the `square` implementation above calculates `number` to the power of `number`, and the test uses the same faulty line of code. While `test_square_wrong` runs without any problems, `test_square_correct` gives us the following error message:

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in test_square_correct
    AssertionError: Expected square 25 but found 3125
