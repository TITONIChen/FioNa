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
print('\r')

#9. remove
y = [0, 1, 2, 3, 4, 5]
y.remove(5)
print(y)
z = ['Fiora', 'Sejuani', 'Xayah', 'Irelia']
z.remove('Xayah')
print(z)
print('\r')

#10. reverse
m = ['Fiora', 'Sejuani', 'Xayah', 'Irelia']
m.reverse()
print(m)

n = ['Fiora', 'Sejuani', 'Xayah', 'Irelia']
list(reversed(n))
print(n)
print('\r')

#11.sort
p = [4, 6, 2, 1, 7, 9]
q = sorted(p)
print(q)
print(p)

i = [4, 6, 2, 1, 7, 9]
j = i.copy()
j.sort()
print(j)
print(i)
print('\r')

#12. 高级排序
legend1 = ['Fiora', 'Sejuani', 'Xayah', 'Irelia']
legend1.sort(key=len)
print(legend1)

l2 = [4, 6, 2, 1, 7, 9]
l2.sort(reverse=True)
print(l2)
