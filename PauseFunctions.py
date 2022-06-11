def foo():
    """Yields a list, the function is resumed on iteration.
    Or on "next()" call.

    Yields:
        list: Empty list which is used as a pointer.
    """
    # Declares "pointer"
    lst = []
    # Returns an iterable. When the generator is itered, the function continues
    yield lst
    print("Foo continues to execute...")
    # Outputs the new value of the pointer
    print(lst)

# Defines an iterable
bar = foo()
# Gets the first element of bar (Which is the list address)
val = next(bar)
# Adds "baz" to the list
val.append("baz")
# Continues the function at the yield
# Ensures the entire generator reaches the end
# If number next statements == number yield statements this isnt required
(i for i in bar)
# This method stacks:

'''
def foo():
    lst = []
    yield lst
    print(lst)
    yield lst
    print(lst)

bar = foo()
val = next(bar)
val.append("baz")
val = next(bar)
val.append("baz")
(i for i in bar)
'''
