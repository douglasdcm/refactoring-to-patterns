# Original code
# It is not easy to understand the code


def add(element):
    readonly = False
    size = 0
    elements = []
    if not readonly:
        new_size = size + 1
        if new_size > len(elements):
            new_elements = []
            for i in range(size):
                new_elements[i] = elements[i]
            elements = new_elements
        size += 1
        elements[size] = element


# Code Refactored
# The new code has meaningfull names for blocks of code and is not nested. The Compose Method
# is a refactoring to simplificate the code
def at_capacity(new_size, elements):
    new_size > len(elements)


def grow(size):
    new_elements = []
    for i in range(size):
        new_elements[i] = elements[i]
    elements = new_elements


def add_elements(elements, element, size):
    size += 1
    elements[size] = element


def add_refac(element):
    readonly = False
    if readonly:
        return
    if at_capacity:
        grow()
    add_elements(element)
