"""
"r" = reading mode
"""
my_file_reading = open("data.txt", "r")
file_value = my_file_reading.read()
my_file_reading.close()
print(file_value)

user_input = input("Enter your name: ")

"""
"w" rewrites all values in file
"""
my_file_writing = open("data.txt", "w")
my_file_writing.write(user_input)
my_file_writing.close()

"""
Character Meaning

'r' - open for reading (default)

'w' - open for writing, truncating the file first

'x' - open for exclusive creation, failing if the file already exists

'a' - open for writing, appending to the end of the file if it exists

'b' - binary mode

't' - text mode (default)

'+' - open for updating (reading and writing)
"""

my_file_write_appending = open("data.txt", "a")
my_file_write_appending.write("\nzxc")
my_file_write_appending.close()

"""
context manager for auto closing files
"""
with open("data.txt", "a") as context_manager_example:
    context_manager_example.write("\n123")