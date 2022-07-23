def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1,2,3,4,5,6,7,8,9,0))