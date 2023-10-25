def looping_func(range, current):
    print(current)
    current += 1

    if(current < range):
        return looping_func(range, current)
    return current

print(looping_func(5, 0))

# def looping_func(range):
#     if n == 0
#     print(current)
#     current += 1

#     if(current < range):
#         return looping_func(range)
#     return current

# print(looping_func(5))