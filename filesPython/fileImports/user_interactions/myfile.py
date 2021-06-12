print(__name__)

"""
The file that we run always has a __name__ variable with a value of "__main__". That is simply how Python tells us that we ran that file.

Running code only in script mode
Sometimes we want to include some code in a file, but we only want that code to run if we executed that file directly—and not if we imported the file.

Since we know that __name__ must be equal to "__main__" for a file to have been run, we can use an if statement.

We could type this in myfile.py:
"""


def get_user_age():
    return int(input("Enter your age: "))


if __name__ == "__main__":
    get_user_age()

"""
That could allow us to run myfile.py and see if the get_user_age() function works.

That is one of the key use cases of this construct: to help us see whether the stuff in a file works when we normally don't want it to run.

Another use case is for files which you don't normally run yourself. Sometimes you may write a file that is for use by another program, for example.

Using this construct would allow you to run your file for testing, while not affecting its functionality when it's imported by another program.
"""
