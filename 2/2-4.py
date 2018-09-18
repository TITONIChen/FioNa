database = [
    ['Fiora', '1234'],
    ['Sejuani', '1234'],
    ['Bjergsen', '1234']
]

username = input('input your name: ')
keyword = input('input your keyword: ')

if [username, keyword] in database: print('Access granted!')
