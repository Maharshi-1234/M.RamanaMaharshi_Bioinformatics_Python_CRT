my_set = {10,20,30,40,50,60,70}
print(type(my_set))
print(10 in my_set)
my_set.add('45')#only 1 value
my_set.update(['apple','orange'])#many values
my_set.remove(10)
my_set.discard(30) #does not raise error if the value is not in the set
my_set.pop() # removes only 1 value from the set
my_set.clear() #removes all the elements
print(my_set)