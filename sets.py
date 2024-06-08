'''print("implement the use of set and various operactions on set")

A = {1, 2, 3, 5, 7, 9}
B = {2, 4, 6, 7, 9, 0}

# union of A and B is A | B
print('union of A and B is', A | B)

# intersection of A and B is A & B
print('intersection of A and B is', A & B)

# difference of A and B is A - B
print('difference of A and B is', A - B)

# symmetric difference of A and B is A ^ B
print('symmetric difference of A and B is', A ^ B)


# using built-in set() function
s = set()
s.add(10)
s.add(20)
s.add(30)
print(s)

# adding multiple elements
primenums = {2, 3, 5, 7, 11, 13, 17, 19}
s.update(primenums)

# removing elements
s.remove(2)
print(s)

# convets string to set 
s = set('hello')
print(s)

# converting tuple to set
s = set((1, 2, 3, 4, 5))
print(s)

# converting dicstionary to set
d = {1: 'one', 2: 'two'}
s = set(d)
print(s)
'''

'''
print("bubble sort")

def bubble_sort(seq):
    n = len(seq)

    for i in range(n - 1):
        flag = 0

        for j in range(n - 1):

            if seq[j] > seq[j + 1]:
                tmp = seq[j]
                seq[j] = seq[j + 1]
                seq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return seq

a = [21, 6, 9, 33, 3]

result = bubble_sort(a)
print(result)
'''
'''
def combinations_with_repetition(arr, k):
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])
            return
        for i in range(start, len(arr)):
            current_combination.append(arr[i])
            backtrack(i, current_combination)
            current_combination.pop()

    result = []
    backtrack(0, [])
    return result
integer_array = [1, 2, 3]
k = 2
result = combinations_with_repetition(integer_array, k)
print(result)
'''
'''
print("insertion sort")

def insertion_sort(newlist):
    for i in range(1, len(newlist)):
        value = newlist[i]

        j = i - 1
        while j >= 0 and value < newlist[j]:
            newlist[j + 1] = newlist[j]
            j -= 1
        newlist[j + 1] = value

    return newlist

newlist = [10 , 5, 13, 8, 2]
print("the unsorted list is", newlist)

print("the sorted list is", insertion_sort(newlist))
'''
'''
print('implementation of factorial')
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
num = int(input("enter any number"))
if num <0:
    print('factorial doe not exist for negative numbers')
elif num==0:
    print('factorial of 0 is 1')
else:
    print("factorial of ", num ,"is ", factorial(num))
'''
'''
print('fibonacci series using recursion')

def recur_fib(n):
    if n <= 1:
        return n
    else:
        return(recur_fib(n-1)+recur_fib(n-2))

nterms = int(input("enter any number: "))
if nterms <= 0:
    print('please enter a positive integer')
else:
    print('fibonacci sequence:')
    for i in range(nterms):
        print(recur_fib(i))
'''

print('implement binary tree and its traversel')

class root_node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder_traverse(root):
    if  root:
        inorder_traverse(root.left)
        print(str(root.val))
        inorder_traverse(root.right)

def preorder_traverse(root):
    if root:
        print(str(root.val))
        preorder_traverse(root.left)
        preorder_traverse(root.right)

def postorder_traverse(root):
    if root:
        postorder_traverse(root.left)
        postorder_traverse(root.right)
        print(str(root.val))

root = root_node(1)
root.left = root_node(2)
root.right = root_node(3)
root.left.left = root_node(4)
root.left.right = root_node(5)

print('inorder traverse')
inorder_traverse(root)
print('\npreorder traverse')
preorder_traverse(root)
print('\npostorder traverse')
postorder_traverse(root)           
