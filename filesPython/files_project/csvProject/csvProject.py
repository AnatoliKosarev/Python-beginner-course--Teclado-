with open("iris.csv", "r") as iris_file:
    """
    Since the data is displayed on separate lines, we know one very important thing. Every line ends with a newline 
    character to mark the line break. We can therefore split our data based on the "\\n" character, giving us each line 
    as a list.
    iris_data = iris_file.read().split("\\n")
    However, because this is a very common operation, Python gives us a tool to do pretty much the same thing. 
    Instead of calling read, we can call readlines.
    The main difference between the two is that readlines is going to preserve this "\\n" character, so we're going to 
    need to remember to trim it off.
    """
    iris_data = iris_file.readlines()

irises = []
"""
Now I'm going to iterate over the list in iris_data using a for loop. Remember that the first line isn't really data 
though. It's just the table headers. I'm therefore not going to iterate over all of the iris data, I'm going to iterate 
over a slice.
"""
for row in iris_data[1:]:
    """
    For each iteration, I'm going to start by stripping off the "\n" character, and splitting the string using a comma 
    as the delimiting string.
    To make it easier to refer to the values later on, I'm going to destructure the list we get back from split.
    """
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")
    """
    Now that we have all of our data assigned to these variables, we can construct our dictionary and append it to 
    irises:
    """
    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }
    irises.append(iris_dict)
    """
    If we wanted to be a little more succinct, we could define the dictionary when making the append call instead:
    irises.append({
		"sepal_length": sepal_length,
		"sepal_width": sepal_width,
		"petal_length": petal_length,
		"petal_width": petal_width,
		"species": species
	})
    """

    """
    Using the dict function
This is a perfectly good approach, but I want to show you another way using the dict function.

dict is an alternative method for creating a dictionary, and it's quite versatile in how we can call it. One way we 
can create a dictionary with dict is to pass it an iterable of iterables, where each of these inner iterables contains 
a key and a value.

For example, let's say I have a list like this:

iris = [
	("sepal_length", "5.1"),
	("sepal_width", "3.5"),
	("petal_length", "1.4"),
	("petal_width", "0.2"),
	("species", "Iris-setosa")
]
This list contains a number of two-element tuples, and we can think of these tuples as containing a key value pair. 
The first element in each tuple is the key, and the second element is the associated value.

If we pass this list to dict, Python is able to construct a dictionary for us, like this:

{
	"sepal_length": "5.1",
	"sepal_width": "3.5",
	"petal_length": "1.4",
	"petal_width": "0.2",
	"species": "Iris-setosa"
}
This is very useful for us, because we can create a structure very similar to this by using zip.
    """

with open("iris.csv", "r") as iris_file2:
    iris_data2 = iris_file2.readlines()
"""
Instead of throwing away the header row, let's store its values and process them like the different lines of data.
"""
headers = iris_data2[0].strip().split(",")
irises2 = []
"""
Now let's iterate over the rows again, but this time, let's match each header item to an value in a given row using zip.
"""
for row in iris_data2[1:]:
    iris2 = row.strip().split(",")
    iris_dict2 = dict(zip(headers, iris2))
    irises2.append(iris_dict2)
