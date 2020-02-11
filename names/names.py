import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# My version - running at .02 seconds
# lru = LRUCache()
# for name_1 in names_1:
#     lru.set(name_1, name_1)
    
# for name_2 in names_2:
#     if lru.get(name_2):
#         duplicates.append(name_2)

# another option - using python built in intersection - fastest option, running at .004 - .005 seconds
# duplicates = list(set(names_1).intersection(set(names_2)))

# option 3 - runs at the same speed as the python intersection function...  .004 - .005 seconds
def intersecting(l1, l2):
    return list(set(l1) & set(l2))

duplicates = intersecting(names_1, names_2)

# Original GitHub Code - running at 6-9 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
