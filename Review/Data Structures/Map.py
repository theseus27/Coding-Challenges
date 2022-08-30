#MAPS
    # Process iterables without a loop
    #Use lambda to create inline functions to do to iterable

#list(map(function, iterable))
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: 2*x, numbers))
even = list(map(lambda x: 2*x, [y for y in numbers if y%2 == 0]))
print(doubled)
print(even)

#Map w/ two iterables
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
alphanumeric = list(map(lambda x,y: str(x) + str(y), letters, numbers))
print(alphanumeric)