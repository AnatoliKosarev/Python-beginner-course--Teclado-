class LockableList:
    """
    *values - allows us to take in an arbitrary number of positional arguments, make locked param keyword only
    convert values to list(), 'cause by default *values will be placed in tuple, and we need mutable collection
    Note that I've also prefaced the the locked property with an underscore.
    This is just a convention used to indicate that this variable is intended for internal use only.
    locked=False means that it's unlocked by default (LockableList can be changed)
    """

    def __init__(self, *values, locked=False):
        self.values = list(values)
        self._locked = locked

    """
    When we call print, Python goes looking inside the object we passed in as an argument for a method called __str__. 
    If it can't find one, it looks for one called __repr__ instead, which we'll get to in a little bit.
    __str__ allows us to define a user-friendly representation of a given object. In our case, I think it's fairly safe 
    to use the standard list syntax to represent our LockableList, but we could really return anything we want. The 
    only rule we need to keep in mind is that it has to return a string.
    """

    def __str__(self):
        return f"{self.values}"

    """
        An easy way to think about __str__ vs __repr__ is that __str__ is for showing information to the user, 
        while __repr__ is information for the developer. When we implement __repr__ we want to provide all the information 
        needed to reproduce the object, being as specific as we can. This might involve including the module name, e.g.
        In our case, we're going to show how to define a LockableList object, and we're going to show the arguments 
        required to recreate the specific LockableList instance __repr__ was called on.
        we're going to call __repr__ on each item in self.values, getting back an appropriate representation for each 
        object in values, based on their type. We'll then join each value with ", " as the joining string.
        """

    def __repr__(self):
        values = ", ".join([value.__repr__() for value in self.values])
        return f"LockableList({values})"

    """
    __len__ allows us to return the length of our object, indicating how many items the sequence contains. 
    This means we can call len on our function without it raising an error.
    """

    def __len__(self):
        return len(self.values)

    """
    Python uses a method called __getitem__ to retrieve the item at that index. 
    It uses the same method for retrieving a slice of some sequence.
    Before we write any code, there are a few things we need to think about when it comes to our implementation 
    Firstly, we need to distinguish between a slice and a reference to a single index, because we need to handle 
    these two uses of __getitem__ differently.
    Secondly, we need to consider how to handle negative indexes.
    Let's first consider how to handle negative indexes. If a user asks for the item at index -1, they want the final 
    item in the sequence. In a sequence of length 5, the index -1 and the index 4 are the same thing. There is a very 
    clear connection between these numbers which will allow us to handle negative indexes: the length of the sequence 
    plus the negative index equals the positive index version of that negative index.
    """

    def __getitem__(self, i):
        if isinstance(i, int):  # check that i = int
            # Perform conversion to positive index if necessary
            if i < 0:
                i = len(self.values) + i
                # for len(l) = 5 and i = -1: 5 - 1 = 4 which is index of last list element = -1
            # Check index lies within the valid range and return value if possible (e.g len = 5, i = -20: ERROR)
            if i < 0 or i >= len(self.values):
                raise IndexError("LockableList index out of range")
            else:
                return self.values[i]
        elif isinstance(i, slice):
            """"
            For example, if we have a slice object slice(-3, -1, 1) and we call indices on this slice object for a 
            sequence of length 5, we'd get a tuple back like this: (2, 4, 1). It contains a start index, 
            a non-inclusive stop index, and a step value.
            """
            start, stop, step = i.indices(len(self.values))
            rng = range(start, stop, step)
            # return new LockableList object
            return LockableList(*[self.values[index] for index in rng])
        else:
            invalid_type = type(i)
            raise TypeError("LockableList indices must be integers or slices, not {}"
                            .format(invalid_type.__name__))

    def __setitem__(self, i, values):
        if self._locked:
            raise RuntimeError("LockableList object does not support item assignment while locked")
        else:
            if isinstance(i, int):
                # Perform conversion to positive index if necessary
                if i < 0:
                    i = len(self.values) + i
                # Check index lies within the valid range and assign value if possible
                if i < 0 or i >= len(self.values):
                    raise IndexError("LockableList index out of range")
                else:
                    self.values[i] = values
            elif isinstance(i, slice):
                start, stop, step = i.indices(len(self.values))
                rng = range(start, stop, step)
                """
                1.Slices allow for asymmetrical assignment. We can assign more values than there is space to 
                accommodate them.
                2.We can also assign fewer items than we replace, and the proceeding values in the sequence will move 
                to fill the remaining space.
                3.When using extended slices, these special properties do not apply unless the step value is 1.
                т.е. если мы вставляем с шагом != 1 - мы не знаем сколько символов переносить, поэтому длина вставляемых
                значений должна быть = длине range, т.к. для каждого индекса range должно быть 1 вставляемое значение
                """
                if step != 1:
                    if len(rng) != len(values):
                        raise ValueError(
                            "attempt to assign a sequence of size {} to extended slice of size {}"
                                .format(len(values), len(rng))
                        )
                    else:
                        for index, value in zip(rng, values):
                            self.values[index] = value
                else:
                    self.values = self.values[:start] + values + self.values[stop:]
            else:
                invalid_type = type(i)
                raise TypeError(
                    "LockableList indices must be integers or slices, not {}"
                        .format(invalid_type.__name__)
                )

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    """
    When Python encounters a binary operator like +, Python first checks the left-hand operand for information on how 
    to perform the operation for the relevant types. If no such information exists, Python tries the right hand operand 
    instead, but this time looks for an r version of the relevant special method. We therefore have special methods 
    like __radd__, __rmul__, and __rsub__.
    i versions of the special methods represent an in-place operation (+= e.g.). This is an operation that doesn't 
    require an assignment.
    """

    def __add__(self, other):
        if isinstance(other, (list, LockableList)):
            return LockableList(*(self.values + other))
        invalid_type = type(other)
        raise TypeError(
            'can only concatenate list or LockableList (not "{}") to LockableList'
                .format(invalid_type.__name__)
        )

    """
    Remember that internally we use a list for storing values in our LockableList. Our return value for __add__ is 
    self.values + other.
    self.values is a list; other is a LockableList, so when we use +, we end up calling the list's __add__ method, 
    and lists only allow concatenation with other lists. We therefore get a TypeError.
    The solution is to implement __radd__, so that Python can fall back on the methods defined LockableList when the 
    list's method raises an error.
    """

    def __radd__(self, other):
        if isinstance(other, (list, LockableList)):
            return LockableList(*(other + self.values))

        invalid_type = type(other)
        raise TypeError(
            'can only concatenate list or LockableList (not "{}") to LockableList'
                .format(invalid_type.__name__)
        )

    """
    __iadd__ is a little different, since we have to take note of our lock state, but the rest of our implementation 
    will be fairly similar
    In the case of __iadd__, we update the internal list directly, and then return a reference to the current object. 
    This allows us to preserve the same object, while updating the values contained within the given LockableList
    
    An interesting thing to note is that our class was already capable of handling the += augmented arithmetic operator 
    before we implemented __iadd__. Try it out for yourself.
    If this is the case, why did we bother implementing __iadd__ at all? __iadd__ is really an optimisation feature. 
    In the absence of __iadd__ Python will fall back to the __add__ method, but our __add__ method creates a new 
    LockableList object, and creating an object isn't free. By implementing __iadd__ we can bypass the creation of 
    this new object, saving us a little bit of computing time.
    """

    def __iadd__(self, other):
        if self._locked:
            raise RuntimeError("LockedList object does not support in-place concatenation while locked")
        if isinstance(other, (list, LockableList)):
            self.values = self.values + other
            return self

        invalid_type = type(other)
        raise TypeError(
            'can only concatenate list or LockableList (not "{}") to LockableList'
            .format(invalid_type.__name__)
        )

    def __mul__(self, other):
        if isinstance(other, int):
            values = []
            for element in self.values:
                for _ in range(other):
                    values.append(element)
            return LockableList(*values)
        invalid_type = type(other)
        raise TypeError(
            'can only multiply integer (not "{}") with LockableList'
                .format(invalid_type.__name__)
        )

    def __imul__(self, other):
        if self._locked:
            raise RuntimeError("LockedList object does not support in-place multiplication while locked")
        if isinstance(other, int):
            for i in range(0, len(self.values) * other, other):
                for _ in range(other - 1):
                    self.values.__setitem__(slice(i, i), [self.values[i]])
            return self
        invalid_type = type(other)
        raise TypeError(
            'can only multiply integer (not "{}") with LockableList'
            .format(invalid_type.__name__)
        )


l = LockableList("a", [1, 2, 3], "c", "d", "e")
print(l)
print(len(l))
print(l[-1])
for i in l:
    print(i)
ls = l[-3: -1: 1]
print(ls)
print(l.__str__())
print(l.__repr__())

friends = LockableList("Rolf", "John", "Anna")
print(friends)
friends[0:3:2] = ["Jose", "Mary"]
print(friends)  # ["Jose", "John", "Mary"]
friends[2::-2] = ["Rolf", "Anna"]
print(friends)  # ["Anna", "John", "Rolf"]
friends[1:2] = ["Jose", "Mary"]
print(friends)  # ['Anna', 'Jose', 'Mary', 'Rolf']
friends[1:3] = ["Paul"]
print(friends)  # ['Anna', 'Paul', 'Rolf']
print(friends[:2])

print(friends + ["Ringo", "James"])
print(friends + LockableList("Kim", "Eric"))
friends += LockableList("James", "Cliff")
print(friends)
friends.lock()
friends.unlock()
print(friends * 2)
friends *= 3
print(friends)
