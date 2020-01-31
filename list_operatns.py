list = []
print("\n intial blank list:")
print(list)

list.append(1)
list.append(2)
list.append(4)
list.append(5)
print("\n list after addition of four elements:")
print(list)


for i in range(1,5):
    list.append(i)
print("\n list after the addition of elements from 1-4:")
print(list)



list.append((6,7))
print("\n list after the addtion of tuple:")
print(list)



list =[1,2,3,4,5]
print("initial list:")
print(list)

list.insert(2,6)
list.insert(5,'fruits')
print("\n list after performing insert operation:")
print(list)


list =[1,2,3,4]
print("initial list:")
print(list)

list.extend([8,'flowers'])
print("\n list perfom extend operation:")
print(list)

list =['peas','cake','ice','kite']
print("accessing index number from th list")
print(list[0])
print(list[1])
print(list[2])
print(list[3])

list= [['cake','kite'],['ice']]
print("acessing element from multi-dimension")
print(list[0][1])
print(list[1][0])

list =[1,2,3,'ice',5,'kite']
print("accessing elements using negetive index")
print(list[-1])
print(list[-3])



list =[1,2,3,4,5,6,7,8,9,10,11,12]
print("initial list:")      
print(list)

list.remove(7)
list.remove(8)
print("\n list after removing a range of elements:")
print(list)
 
for i in range(1,5):
    list.remove(i)      
print("\n list after removing range of elements:")
print(list)


list = [1,2,3,4,5]
list.pop()
print("\n list after poping element:")
print(list)


list.pop(3)
print("\n list after poping specific element:")
print(list)


      
