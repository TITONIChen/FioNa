#以数指定年、月、日的日期打印出来
y = input("please input a year:")
m = input("please input a mouth:")
d =  input("please input a day:")

month = [0, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day = [0, '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11st', '12nd', '13rd', '14th',
       '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th',
       '28th', '29th', '30th', '31st']

month_number = int(m)
day_number = int(d)

print(month[month_number] + ' ' + day[day_number] + ", " + y)
