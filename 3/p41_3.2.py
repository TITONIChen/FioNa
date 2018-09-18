#设置字符串的格式
from math import pi
a = "{name} is approximately {value:.2f}".format(value = pi, name = 'π')
print(a)

b = "{name1}, {name2}, {name3} and {name4} are my favorite heros!".format(name4 = 'Irelia', name3 = 'XaYah', name2 = 'Sejuani', name1 = 'Fiora')
print(b)
