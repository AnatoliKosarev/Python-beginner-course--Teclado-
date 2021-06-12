from user_interactions.myfile import get_user_age

"""
The file that we run always has a __name__ variable with a value of "__main__". That is simply how Python tells us that we ran that file.

Any file that doesn't have a __name__ equal to "__main__" was imported.
"""

print(__name__)

get_user_age()