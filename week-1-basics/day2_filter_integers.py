def filter_integer(numbers):
    return [i for i in numbers if isinstance(i, int) and not isinstance(i, bool)]
print(filter_integer([1, "hello", 3.5, 2, "hi", 10, True]))