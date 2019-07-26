import time


""" class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            # If left child is empty, store the new value there
            if not self.left:
                self.left = BinarySearchTree(value)
            # If not, keep searching for an empty spot
            else:
                self.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.insert(value)

    def contains(self, target):

    Was going this route but realized that, like in JavaScript, Python also has a built in set() function
"""


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


def find_dupes(list1, list2):
    # Using set, runtime = 0.014957189559936523 seconds
    unique_set = set(list1)

    dupes_list = []
    for el in list2:
        if el in unique_set:
            dupes_list.append(el)
    return dupes_list


duplicates = find_dupes(names_1, names_2)


# Without using set, runtime = 3.341212749481201 seconds
# def find_dupes(list1, list2):
#     dupes_list = []
#     for el in list2:
#         if el in list1:
#             dupes_list.append(el)
#     return dupes_list


# Runtime on my laptop = 14.64 seconds O_o
# O(n^2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
