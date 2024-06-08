'''
print("using built in sort() method")
# Create a queue using a list
my_queue = []
# Enqueue elements into the queue
my_queue.append(5)
my_queue.append(1)
my_queue.append(3)
my_queue.append(2)
my_queue.append(4)
print("Original Queue:")
print(my_queue)
# Sort the queue
my_queue.sort()
print("Sorted Queue:")
print(my_queue)
'------------ OR (Merko nahi malum konsa sahi rahega) ----------------'
'''
'''
print("using a bubble sort algorithm")
def enqueue(queue, item):
    queue.append(item)
def bubble_sort(queue):
    n = len(queue)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if queue[j] > queue[j + 1]:
                queue[j], queue[j + 1] = queue[j + 1], queue[j]
    return queue
# Create an empty list to represent the queue
queue = []
# Add elements to the queue (enqueue)
enqueue(queue, 5)
enqueue(queue, 2)
enqueue(queue, 8)
enqueue(queue, 1)
# Sort the queue using bubble sort
sorted_queue = bubble_sort(queue)
# Print the sorted queue
print(sorted_queue)

'''
'''
print("using built-in sort() method")

# Create an empty queue
my_queue = []

# Take user input to enqueue elements into the queue
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    element = int(input("Enter element {} for the queue: ".format(i + 1)))
    my_queue.append(element)

print("Original Queue:")
print(my_queue)

# Sort the queue
my_queue.sort()

print("Sorted Queue:")
print(my_queue)
'''
'''
print("sortinng with the help of built in sorting queue method")
my_queue=[]
my_queue.append(5)
my_queue.append(2)
my_queue.append(8)
my_queue.append(4)
my_queue.append(9)
print("Original queue")
print(my_queue)
my_queue.sort()
print(my_queue)
'''
'''
def postfix_to_prefix(postfix_expression):
    stack = []
    operators = set("+-*/")
    for token in postfix_expression:
        if token not in operators:
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expression = token + operand1 + operand2
            stack.append(new_expression)
    # The final expression will be at the top of the stack
    return stack[0]

postfix_expression = "= mn*pq-+r+"
prefix_expression = postfix_to_prefix(postfix_expression[2:])  # Skip the "=" at the beginning
prefix_expression = "=" + prefix_expression  # Re-add the "=" symbol
print("Prefix expression:", prefix_expression)
'''
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"
# Example usage:
if __name__ == "__main__":
    date = Date(2023, 10, 18)
    print("Date:", date)





