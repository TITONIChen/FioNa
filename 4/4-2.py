#一个使用get()的简单数据库

people = {
	'Fiora': {
		'phone': '2341',
		'addr': 'Foo drive 23'
	},
	
	'Sejuani': {
		'phone': '9102',
		'addr': 'Bar street 42'
	},
	
	'Irelia': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}
}

labels = {
	'phone': 'phone number',
	'addr': 'address'
}

name = input('Please input your name: ')
request = input('phone number(p) or address(a): ')

key = request	#先把request的值赋给key，如果request的输入不是p或a，key把其他值传给label和result
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

person = people.get(name, {})	#person输出为某个人的phone和addr
label = labels.get(key, key)	#如果key不是phone或addr，label就把原request的值输出
results = person.get(key, 'not available')

print("{}'s {} is {}".format(name, label, results))	#这个方法既可以判断输入的人名是否在labels字典里，又可以检测request的格式是否规范(p&&a)
