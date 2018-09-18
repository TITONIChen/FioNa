'''
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
'''
#6. split
a = '1+2+3+4+5'
print(a.split('+'))
b = 'Fiora Sejuani Xayah Irelia'
print(b.split())
