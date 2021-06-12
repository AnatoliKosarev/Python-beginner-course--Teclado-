"""
iterable has to implement __iter__() method or __len__() + __getitem__() methods
iterable can be generator and iterator at the same time, e.g.

iterator: used to get the next value
iterable: used to go over all the values of the iterator
"""


class HundredIterableIteratorGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration

    def __iter__(self):
        return self  # returns iterator, which in this case is object itself as it implements __next__()


print(sum(HundredIterableIteratorGenerator()))

for n in HundredIterableIteratorGenerator():
    print(n)


class AnotherIterable:
    def __init__(self):
        self.cars = ["Ford", "Kia"]

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


for car in AnotherIterable():
    print(car)

"""
First let's talk about two important protocols we need to understand: the iteration protocol, and the iterator protocol. In case you're unsure, a protocol is really just an agreement that something will happen when certain qualifying conditions are met. In the case of the iterator and iteration protocol, the condition is that we implement certain special methods, and the agreement is that these special methods, if properly implemented, will permit certain behaviour for our objects.

Finding reference to the iteration protocol is quite hard in the documentation. You can find one reference under the built-in iter function:

"... object must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0)."



You can find the original text here: https://docs.python.org/3.8/library/functions.html#iter

So, to satisfy the iteration protocol, we need one of two things:

1) An __iter__ method, and this __iter__ method must return an iterator. We know this because the documentation for __iter__ specifies the return type.

2) A __getitem__ method which is implemented using sequence semantics. This means that we can retrieve items from this object using indices, the indices increment in steps of one, the elements are ordered by these indices, and the starting index is 0. The kind of behaviour you see with a list or tuple.

We get further confirmation of what we've found here by looking at the glossary term for an iterable: https://docs.python.org/3.8/glossary.html#term-iterable

Directly below this term we find iterator, and here we get a very clear statement that all iterators are iterables, because all iterators are required to implement __iter__, and so every iterator satisfies the iteration protocol:

"Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted."



The iterator protocol is actually a superset of the iterator protocol, and requires an __iter__ method and a __next__ method, with the __iter__ method simply returning self. We can find a clear definition of the protocol here:

"The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:

 iterator.__iter__()

Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.

iterator.__next__()

Return the next item from the container. If there are no further items, raise the StopIteration exception. This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API."



You can find the original text here: https://docs.python.org/3/library/stdtypes.html#iterator-types

As we can see, there's no need to have a __len__ method at all for iteration, and an __iter__ method is required for both an iterator, and an iterable which doesn't implement __getitem__ in an appropriate way.

So, once again, all iterators are iterables. There is no such thing as a non-iterable iterator, and a class which implements only __next__ is nothing. It's just a class which implements a random special method.

So, where do generators fit in? Generators are a means for us to define an iterator without implementing these special methods on our own. The "generator class" that gets created in an exercise in this section is not a generator, as we'll soon see, and it fails to satisfy both the iterator and iteration protocols.

There are three ways we can make a generator (actually called a generator iterator) in Python:

1) We can create a class which inherits from GeneratorType. Objects of this class are generator iterators.

2) We can add a yield statement to a function, turning it into a generator. The object returned when we call this special function is a generator iterator.

3) We can use a generator expression. The expression evaluates to a generator iterator object.

From the documentation on generator types:

"Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s __iter__() method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the __iter__() and __next__() methods."



What this tells us very clearly is that generators all implement the iterator protocol, so they are all iterators. Since the iterator protocol is a superset of the iteration protocol, all generators are also iterable. There's therefore also no such thing as a non-iterable generator.

Generators also have nothing at all to do with "generating values", which is a common misunderstanding. Regular iterators can do this as well, and generators may not do anything to create new values. They are just shortcuts for writing iterators, and the generator iterator we get back is just an iterator.

The only difference is that generators, as of a few versions ago, were given additional methods automatically, to help us use them more effectively as coroutines.

I hope that helps, but please let me know if you're not still clear on anything.
"""

"""
The __next__ method is a required method for the iterator protocol, not the iteration protocol, so you don't need to implement it to make something iterable. As such, we should only really be defining __next__ for iterators, and it should always be in conjunction with __iter__.

All we need to make something an iterable is either a __getitem__ method, implemented as though the class were a sequence type, or an __iter__ method which returns an iterator.

By defining a sequence-like __getitem__ method, you're giving Python the ability to automatically create an iterator for this type, and this iterator will necessarily implement __next__ and __iter__. __getitem__ is therefore an alternative to defining __iter__, though you can define both if you like.

While __getitem__ and __iter__ are fine together, I think it would be highly unusual to define __getitem__ and __next__ for the same class. By defining __next__ and __iter__, we'd be creating an iterator, and iterators can be consumed. This is generally not desirable behaviour for a type for which we can also access items by index.

We could end up in a situation where an object has been completely exhausted, and using it in a for loop yields nothing, but where we can still access all of the items by index. That's highly unusual behaviour.

For this particular type, you also have a set of fixed values, and these are stored permanently. This completely removes one of the major benefits of iterators, which is lazy evaluation.

What you'd generally do instead is define a separate iterator class which can be used by instances of your type when we need to perform iteration. You can then return an instance of this type using an __iter__ method on the Cars class. The iterator you define would implement __next__ and __iter__, and the __iter__ method would just return self.

You can find information on this in the documentation:

"Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted."
"""