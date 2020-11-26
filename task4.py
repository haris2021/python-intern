l1=list(range(10))                  #create a list of 10 items
l1.append(12)                       #appends an item at the end
l1.insert(8,11)                     #insert the given item at the specified index
del l1[0]                           #deletes the item at the specified index
l1.remove(11)                       #deletes the specified item
large=max(l1)                       #returns the largest no. from the list
small=min(l1)                       #returns the smallest no. from the list
print(l1)
print(large,small)

t1=tuple(range(1,11))               #create a tuple of 10 items
t2=t1[::-1]                         #reverse the tuple
print(t2)

t3=(1,"777",1.77)                   
l3=list(t3)                         #converting tuple to list
print(l3)
