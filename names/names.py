#names/names.py



import time
from bst import BSTNode


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
#
#end_time = time.time()
#print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
#print (f"runtime: {end_time - start_time} seconds")
#
#runtime: 5.6640050411224365 seconds


# Use BST to look for values

# Create BST with first element as root

bst = BSTNode(names_1[0])

# Add all names from names_1 to the tree

for name in names_1:
    bst.insert(name)

# For each name in names_2 list check if the name is in the tree

# If True, add the name to the duplicates list

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# runtime: 0.09182572364807129 seconds


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
