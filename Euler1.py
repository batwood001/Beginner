itersleft = 999
set = []

while (itersleft != 0):
    if itersleft % 3 == 0 or itersleft % 5 == 0:
        set.append(itersleft)
    pass
    itersleft = itersleft - 1

print sum(set)
    
    