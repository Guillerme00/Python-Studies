mylist = [1,2,3,4,5]

#normal iteration
for numb in mylist:
    print(numb)

#another iteration method
iter_example = iter(mylist)
print(iter_example)

#When you use the 'iter' method, you store the list's memory address

try:
    while True:
        # When you use the 'next' method on an iterated objetct, it returns the next value
        print(next(iter_example))
except StopIteration as error:
    # If the iterated object dosen't have a next value, it raise an error called 'StopIteration'
    print(error)


#Creating a generator with Yield
def generator():
    n = 0
    print(f"My N is now {n}")
    yield n

    n += 1
    print(f"My N is now {n}")
    yield n

    n += 1
    print(f"My N is now {n}")
    yield n

    n += 1
    print(f"My N is now {n}")
    yield n

#When the funcion is called, it store all the funcion on the variable, and stay there waiting for the next
gen = generator()

#When you call "next()" method, the function runs until the yield, and store the variable
print(next(gen))

#When you don't have next, it raises an error calle"StopIteration", like the Iter method
try:
    while True:
        print(next(gen))
except StopIteration as error:
    print(error)