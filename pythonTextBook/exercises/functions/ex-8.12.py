def make_sandwich(*components):
    print("Sandwich made with following components:")
    for component in components:
        print(f"\t{component}")
    print(components)


make_sandwich("bread")
make_sandwich("bread", "cheese")
make_sandwich("bread", "chicken", "butter", "cheese")