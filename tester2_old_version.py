import threading ,queue,urllib3
from urllib3.contrib.socks import SOCKSProxyManager

def test_http_proxy(proxy):
	pr = urllib3.ProxyManager('http://'+proxy)
	pr.request('GET', 'https://www.youtube.com')

def test_socks_proxy(proxy):	
	pr = SOCKSProxyManager('socks5://'+proxy)
	pr.request('GET', 'https://www.youtube.com')


def thread_function(proxy,q):
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
	
good_proxies = 0
all_proxies = 0
num_lines = sum(1 for line in open('proxy.txt'))
proxies = []
urllib3.disable_warnings()

with open("testp.txt") as f:
	content = f.readlines()
	content = [x.strip() for x in content] 
	for c in content:
		proxies.append(c)

while all_proxies < num_lines:
	print("new set!")
    pool = ThreadPool(processes=1)

    async_result = pool.apply_async(thread_function, str(proxies[all_proxies+=1])
    return_val = async_result.get() 

print(return_val)

	num_th_handler = num_lines-all_proxies
	if not num_th_handler - num_thread > 0:
		num_thread = num_th_handler 