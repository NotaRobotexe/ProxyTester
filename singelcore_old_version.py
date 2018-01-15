import threading ,queue,urllib3

def thread_function(test):
	proxy = urllib3.ProxyManager('http://'+test)
	r=proxy.request('GET', 'https://www.youtube.com')
    
proxies = []
urllib3.disable_warnings()
num_thread=3

with open("proxy.txt") as f:
	content = f.readlines()
	content = [x.strip() for x in content] 
	for c in content:
		proxies.append(c)

for num in range(num_thread):
    try:
        thread_function(proxies[num])
    except:
        print("dead")
    else:
        print("ok")