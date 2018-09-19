people = {
	'Fiora': {
		'phone number': '1234',
		'addr': '1号床'
	},
	
	'Sejuani': {
		'phone number': '2234',
		'addr': '2号床'
	},
	
	'Irelia': {
		'phone number': '3234',
		'addr': '3号床'
	},
	
	'Xayah': {
		'phone number': '4234',
		'addr': '4号床'
	}
}

'''labels = {
	'phone': 'phone number',
	'addr': 'address'
}
'''
name = input('please input your name: ')

request = input('require phone(p) or address(a)')
if request == 'p': key = 'phone number'
if request == 'a': key = 'addr'

print("{}'s {} is {}".format(name, key, people[name][key]))
