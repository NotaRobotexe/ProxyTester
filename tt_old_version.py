import threading ,queue,urllib3
import random
from urllib3.contrib.socks import SOCKSProxyManager

def test_http_proxy(proxy,time):
	pr = urllib3.ProxyManager('http://'+proxy)
	pr.request('GET', 'https://www.youtube.com', timeout=time)

def test_socks_proxy(proxy,time):	
	prs = SOCKSProxyManager('socks5://'+proxy)
	prs.request('GET', 'https://www.youtube.com', timeout=time)


def thread_function(proxy,q,time):
	try:
		print("test1")
		test_http_proxy(proxy,time)
	except:
		print("test1f")
		try:
			print("test2")
			test_socks_proxy(proxy,time)
		except:
			print("test2f")
		else:
			print("test2k")
			q.put(proxy)
	else:
		print("test1k")
		q.put(proxy)

num_thread=3
q = queue.Queue()
threads = []

proxies = []
urllib3.disable_warnings()

with open("proxy.txt") as f:
	content = f.readlines()
	content = [x.strip() for x in content] 
	for c in content:
		proxies.append(c)

for num in range(num_thread):
	t= threading.Thread(target=thread_function,args=(proxies[num],q,5))
	t.start()
	threads.append(t)

for t in threads:
	t.join()

while not q.empty():
	print(str(q.get()))