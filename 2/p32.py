#删除元素
number = [0, 1, 2, 3, 4, 5, 6]
#del number[1:6]
number [1:6] = []
print(number)

#给切片赋值
number = [0, 6]
number[1:1] = [1, 2, 3, 4, 5]
print(number)

name = list('Pioneer')
print(name)
name[1:] = list('ython')
#name[1:] = ['y', 't', 'h', 'o', 'n']
print(name)
