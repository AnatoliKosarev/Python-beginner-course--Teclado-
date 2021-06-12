import re


def is_filename_safe(filename):
    regex = r"^[A-Za-z\d][A-z\d\-_()]*(.jpe?g|.png|.gif)$"
    return re.match(regex, filename) is not None


print(is_filename_safe("test.pngpng"))