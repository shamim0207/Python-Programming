numbers=[5,6,2,4,10,8,7,5,20,30,15]
# sort() method
numbers.sort()
print("Sorted list using sort() method:",numbers)
#add one element at the end of the list using append() method
numbers.append(25)
print("List after appending 25 using append() method:",numbers)
#sort reversely using sort() method with reverse=True
numbers.sort(reverse=True)
print("List after sorting reversely:",numbers)
#insert element at specific position using insert() method
numbers.insert(3,12)
print("List after inserting 12 at index 3 using insert() method:",numbers) 
#remove element using remove() method
numbers.remove(4)
print("List after removing 4 using remove() method:",numbers) 
#pop() method to remove element at specific index
removed_element=numbers.pop(5)
print("List after popping element at index 5 using pop() method:",numbers)
print("Popped element:",removed_element)    