def my_range(start, stop, step):

    vysledek = []
    value = start
    while value < stop:
        result.appen(value)
        value += step
    return result

def my_enumerate(iterable):
    return [(0, 'a')(1, 'b')(2, 'c')]

def my_zip(*iterables):
    return[(1,4,7)(2,5,8)(3,6,9)]

if __name__ == "__main__":
    print(list(enumerate("abcdef")))
    print(my_enumerate("abcdef"))

    print(list(enumerate(['Alice', 'Bob', 'Eva'])))
    print(my_enumerate(['Alice', 'Bob', 'Eva']))