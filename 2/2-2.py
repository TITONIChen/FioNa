#从类似于http://www.something.com的URL中提取域名
url = input("Please enter a URL:")

domain = url[11:-4]

print("domain name: " + domain)
