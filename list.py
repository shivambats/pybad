""""
    Use list comprehension whenever possible,
    this is not as such a bad practice but list comprehension is
    a pythonic way to do such stuff
"""


def foo_avoid():
    list_to_be_populated = []
    for num in range(0, 5):
        list_to_be_populated.append(num*5)


def foo_prefer():
    return [num * 5 for num in range(0, 5)]


foo_prefer()
foo_avoid()
