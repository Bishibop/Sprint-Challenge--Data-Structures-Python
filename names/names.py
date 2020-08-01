import time
from binary_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# This is an 0(n**2) complexity algorithm. Sprint says I need to identify it
# but doesn't say where, so I'm putting it here. Sprint also gives answer in
# readme. lol.

# Replace the nested for loops below with your improvements
#  for name_1 in names_1:
#      for name_2 in names_2:
#          if name_1 == name_2:
#              duplicates.append(name_1)

# and then this method is O(nlog(n)). To build the tree, we perform n insertion
# operations, each exhibiting log(n) time for a total of nlog(n).

# for finding duplicates, we perform n search operations, each exhibiting
# log(n) time as well, for another nlog(n) operation. Add these together and
# we get 2nlog(n) time which is equivalent to nlog(n).
names_tree = BSTNode()
for name_1 in names_1:
    names_tree.insert(name_1)

for name_2 in names_2:
    if names_tree.contains(name_2):
        duplicates.append(name_2)
    else:
        pass

# speedy stretch version
#  names_1_set = set(names_1)
#  names_2_set = set(names_2)
#  duplicates = names_1_set.intersection(names_2_set)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this
# problem

# What's the best time you can accomplish?

# Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did
# not write yourself.

