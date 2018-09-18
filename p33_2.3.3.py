#列表方法
#object.method(arguments)

#1. append
lst = [1, 2, 3]
lst.append(4)
print(lst)
print('\r')

#2. clear
lst = [1, 2, 3]
lst.clear()
print(lst)
print('\r')

#3, copy
a = [1, 2, 3]
b = a
b[1] = 5
print(a)

a = [1, 2, 3]
b = a.copy()    #b = a[:]   #b = list(a)
b[1] = 5
print(a)
print(b)
print('\r')

#4. court
LOL = ['Fiora', 'Sejuani', 1, 2, [1, 2]]
print(LOL.count(1))
print('\r')

#5. extend
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
print(lst1)

lst1 = [1, 2, 3]
print(lst1+lst2)
print(lst1)

#6. index
lol = ['Fiora', 'Sejuani', 'Irelia', 'Xayah']
print(lol.index('Xayah'))
print('\r')

#7. insert
num1 = [0, 1, 2, 3, 5]
num1.insert(4, 'four')
print(num1)

num2 = [0, 1, 2, 3, 5]
num2[4:4] = [4]
print(num2)
print('\r')

#8. pop
x = [0, 1, 2, 3, 4, 5 ,6]
x.pop()
print(x)
#x,pop()
#print(x)
x.pop(0)
print(x)
