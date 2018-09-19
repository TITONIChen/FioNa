
#1. center
a = "Fiora, Sejuani, XaYah and Irelia are my favorite heros!".center(65, "*")
print(a)

#2. find
b = "Fiora, Sejuani, and Irelia are my favorite heros!"
print(b.find('Irelia'))
print(b.find('Xayah'))
print(b.find('Irelia', 0, 20))

#3. join
sep = '+'
seq = '1', '2', '3', '4', '5'
print(sep.join(seq))

#6. split
a = '1+2+3+4+5'
print(a.split('+'))
b = 'Fiora Sejuani Xayah Irelia'
print(b.split())


#4. lower
name = 'Xayah'
names = ['fiora', 'sejuani', 'irelia', 'xayah']
if name.lower() in names: print('Found it')

#5. replace
names = 'fiora Sejuani Irelia Xayah'
print(names.replace('fiora', 'Fiora'))

#7. strip
names = ['Fiora', 'Sejuani', 'Irelia', 'Xayah']
name = 'Sejuani '
if name in names: print('Found it!')
else: print('Error!')
if name.strip() in names: print('Found it!')
else: print('Error!')

tup = '***  SPAM * for * everyone!!! ***'
print(tup.strip('#!S'))
print(tup.strip('*!S'))
print(tup.strip(' *!S'))

#8. translate
table = str.maketrans('cs', 'kz')
print(table)
tup = 'this is an incredible test!'
print(tup.translate(table))

table2 = str.maketrans('cs', 'kz', ' ')
print(tup.translate(table2))

#9. 判断字符串是否满足特定的条件
