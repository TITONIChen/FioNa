# 字典方法
'''
#1. clear
d = {}
d['name'] = 'Fiora'
d['age'] = 23
print(d)
d.clear()
print(d)

x = {}
x['name'] = 'Sejuani'
y = x
print(x)
print(y)
x = {}
print(x)
print(y)
print('\r')

x = {}
x['name'] = 'Xayah'
y = x
print(x)
print(y)
x.clear()
print(x)
print(y)

#2. copy
#浅复制
a = {'h1': 'Fiora', 'h2': ['Sejuani', 'Xayah'], 'h3': 'Irelia'}
b = a.copy()
b['h3'] = 'Xayah'
b['h2'].remove('Xayah')
print(a)
print(b)
print('\r')

#深复制
from copy import deepcopy
a = {}
a['h1'] = ['Fiora', 'Sejuani']
print(a)
b = a.copy()
c = deepcopy(a)
a['h1'].append('Irelia')
print(b)
print(c)
#当替换副本中的值时（即为键赋予新的值），原件不受影响；然而，如果修改副本中的值（即值为一个元组，要修改其中某一项）时，原件也将发生变化。

#3. fromkeys
a = {}
a.fromkeys(['name', 'age'])
print(a)

b = {}
b.fromkeys(['name', 'age'], 'Unknown')
print(b)

c = {}.fromkeys(['name', 'age'])
print(c)

#4. get
a = {'h1': 'Fiora', 'h2': 'Sejuani'}
print(a.get('h3', 'N/A'))

#5. items
a = {'h1': 'Fiora', 'h2': ['Sejuani', 'Xayah'], 'h3': 'Irelia'}
print(a.items())
print(a)
print(len(a))
print(('h1', 'Fiora') in a)
it = a.items()
print(('h1', 'Fiora') in it)

#6. keys
a = {'h1': 'Fiora', 'h2': ['Sejuani', 'Xayah'], 'h3': 'Irelia'}
print(a.keys())

#11. values
a = {'h1': 'Fiora', 'h2': ['Sejuani', 'Xayah'], 'h3': 'Irelia'}
print(a.values())

#7. pop
a = {'h1': 'Fiora', 'h2': ['Sejuani', 'Xayah'], 'h3': 'Irelia'}
a.pop('h1')
print(a)

#8. popitem	随机地弹出一个字典项
a = {'h1': 'Fiora', 'h2': ['Sejuani', 'Xayah'], 'h3': 'Irelia'}
a.popitem()
print(a)

#9. setdefault
a = {}
print(a.setdefault('name', 'N/A'))
print(a)
a['name'] = 'Sejuani'
print(a.setdefault('name', 'N/A'))

a = {}
print(a.setdefault('name'))	#值没有指定，默认为none
'''
#10. update
a = {'h1': 'Fiora', 'h2': 'Sejuani', 'h3': 'Irelia'}
b = {'h4': 'Xayah'}
a.update(b)
print(a)
