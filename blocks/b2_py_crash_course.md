# The 15 Minute Python Crash Course
Lets learn some of the basics :).

Create a new file and save it as `crash_course.py`.

How this is going to work is I'm going to give you code, you'll write that code yourself, you'll run the code, and then I'll explain how it works! 

If you don't remember how to run code, check out the setup proccess here where we ran the "Hello World" program.

*Note: Please don't copy/paste my code from here. You'll learn more by writing it for yourself!*

Okay, lets do this.

## Basic Prints
Write and run this code. Be sure that each `print` is on a seperate line!

    print("Memes")
    print(1+1)
    print(5*2)
    print(10/2)

In your terminal this will print

    Memes
    2
    10
    5.0

Basically, `print` is a thing given to us by Python that lets us output stuff to the terminal. So, when we did `print("Memes")` it printed out the word *Memes* to our terminal. When we want to print out actual words, we need to make sure to wrap them in `" "` quotation marks!

We can also do math within print. When we did `print(5*2)` it output *10* since 5 multiplied by 2 is 10. Notice here we don't use quotation marks since we're just doing math and are not getting actual words involved!

Delete all your code. Type in:

    print(Nice memes everyone)

When you run this, your program *crashes*. The nice thing when a program crashes is it will tell you exactly where it crashed and the error within the terminal. These are called the *error logs*.

In this case, it tells us that it crashes right on Line 1 and the error type is `SyntaxError: invalid syntax`.

We tried to print out the sentence *Nice memes everyone* but we didn't wrap it with quotation marks!

    print("Nice memes everyone")

There we go :).

Get used to getting crashes and errors. Get used to getting errors you've never even seen before. 

Don't worry. It doesn't mean you're a bad programmer. They happen a lot to everyone. The best you can do is get good at quickly looking at the error logs and fixing the mistake in your program.

Sometimes you may come accross a new error and you might have no idea how to fix it. In this case, take the error and **Google** it :).

## Variables
Variables are boxes that we can put stuff in. Run this:

    this_is_a_variable = "elon musk"
    a_number = 66 * 10 + 6
    print(this_is_a_variable, a_number)

We took the word `"elon musk"` and put it in the variable `this_is_a_variable` by using the `=` sign to say put `"elon musk"` in the box with the name `this_is_a_variable`.

We also took `66 * 10 + 6` and put that in a variable. Then, at the very end we printed both of the variables out :).

Again, just think of variables as boxes that can hold whatever we want.

Delete everything. Try and run this program:

    first_youtuber = "T Series"
    print("The #1 most subscribed Youtuber is", first_youtuber)
    print("The #2 most subscribed Youtuber is", second_youtuber)

Do you understand why it crashes? 

We never declared a variable with the name `second_youtuber`. 

    first_youtuber = "T Series"
    second_youtuber = "PewDiePie"
    print("The #1 most subscribed Youtuber is", first_youtuber)
    print("The #2 most subscribed Youtuber is", second_youtuber)


There we go. Also, sorry PewDiePie :(.

## For Loops
For loops let you do the same thing however many times you want. Run the code below. 

    for i in range(0, 10):
        print(i)
    print("Done!")

Make sure you press "Tab" on the second line where it says `print(i)`, I'll explain why in a second.

When you run this you'll see that it prints out:

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    Done

Do you kinda see what's happening? We ran `print` 10 times and at each iteration `i` had a different value! This is the magic of a for loop. It will take the `range`, iterate through the values, and assign `i` that value. Also, notice also how "Done" was printed at the very end after the for loop was done!


Go ahead and mess with the values within `range(0,10)`, try something like `range(60, 69)` and run it!

Now, try and run this code with no "Tab" on the second line.

    for i in range(0, 10):
    print(i)
    print("Done")

It crashes! What's the error? An `IndentationError`! Basically, the for loop needs to know what code to run in the loop. It does this based on the indentation of the code.

This is a very important concept to understand in Python.

Run this code:

    num = 0
    for i in range(0, 5):
        num = num + 2
        print(num)
    print("Complete")

What happens? How does it work?

Try and understand it yourself! If you don't get it, hit me up in the Discord. I'm happy to help :).






