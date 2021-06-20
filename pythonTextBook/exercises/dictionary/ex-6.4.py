py_glossary = {
    'list': 'A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a '
            'linked list since access to elements is O(1).',
    'loader': 'An object that loads a module. It must define a method named load_module(). A loader is typically '
              'returned by a finder. See PEP 302 for details and importlib.abc.Loader for an abstract base class.',
    'magic method': 'An informal synonym for special method.',
    'mutable': 'Mutable objects can change their value but keep their id(). See also immutable.',
    'object': 'Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class '
              'of any new-style class.'
}

for key, value in py_glossary.items():
    print(f"{key}:\n\t{value}\n")
