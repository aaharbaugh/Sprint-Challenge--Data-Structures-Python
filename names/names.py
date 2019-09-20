import time

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

    if value < self.value:
        if self.left is None:
             self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)

    else:
        if self.right is None: 
            self.right = BinarySearchTree(value)
        else: 
            self.right.insert(value)



  def contains(self, target):
    current = self

    while current:
      if target == current.value:
        return True
      elif target > current.value:
          if current.right is None:
            return False
          current = current.right

      elif target < current.value:
          if current.left is None:
            return False
          current = current.left

    # if target == self.value:
    #     return True
    # elif target < self.value:
    #     if self.left is not None: 
    #         self.left.contains(target)
    #     else: 
    #         return False
    # elif target > self.value:
    #     if self.right is not None: 
    #         self.right.contains(target)
    #     else:
    #         return False

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


#---first attempt, created a binary search tree and hashed values
#---runtime is around 0.1
#create a binary tree
#when addding to tree, we will hash the name, and insert the numerical value. 
#store the hash

# bst = BinarySearchTree(0)
# for name_1 in names_1:
#     hashedName = hash(name_1)
#     bst.insert(hashedName)

# for name_2 in names_2: 
#     hashedName = hash(name_2)
#     if bst.contains(hashedName):
#         duplicates.append(name_2)

#---second attempt. runtime is around 0.01
# dictionaryList = {key:1 for key in names_1}
# duplicates = [name_2 for name_2 in names_2 if name_2 in dictionaryList]

#---stretch. only use an array. runtime is around 1s
duplicates = [name_2 for name_2 in names_2 if name_2 in names_1]



#check if hash matches, if so, return name of hash

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

