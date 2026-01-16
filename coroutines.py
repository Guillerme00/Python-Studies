def coroutines():
    yield
    print("Test 1")

    yield
    print("Test 2")

    yield
    print("Test 3")

    yield
    print("Test 4")

    yield
    print("Test 5")

def coroutines_two():
    yield
    print("Test 1")

    yield
    print("Test 2")

    yield
    print("Test 3")

    yield
    print("Test 4")

    yield
    print("Test 5")

try:
    ex1 = coroutines()
    ex2 = coroutines_two()

    next(ex1)
    next(ex2)
    next(ex2)
    next(ex2)
    next(ex1)
    next(ex2)
    next(ex1)
    next(ex1)
    next(ex1)
    next(ex1)
    next(ex1)

except StopIteration as error:
    print(error)