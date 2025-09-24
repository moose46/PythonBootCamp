# https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9388534#overview
# 9/23/2025 R. W. Curtiss
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(mylist[0])
anotherlist = ['four', 'five', 'six', 'seven', 'eight', 'nine']
print(anotherlist[4])
anotherlist[2] = 'eight'
print(anotherlist)
print(anotherlist[2])
print(anotherlist[-1])
new_list = anotherlist + mylist
print(new_list)
new_list[1] = new_list[1].upper()
print(new_list)

new_list.append('boo boo')
print(f'append to new list = {new_list}')
new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)
print(new_list)
print(new_list.pop(0))
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)

