import threading ,queue,urllib3
from urllib3.contrib.socks import SOCKSProxyManager


def test_http_proxy(proxy,time):
	pr = urllib3.ProxyManager('http://'+proxy)
	pr.request('GET', 'https://www.youtube.com', timeout=time)

def test_socks_proxy(proxy,time):	
	prs = SOCKSProxyManager('socks5://'+proxy)
	prs.request('GET', 'https://www.youtube.com', timeout=time)


def thread_function(proxy,q,time):
	try:
		test_http_proxy(proxy,time)
	except:
		try:
			test_socks_proxy(proxy,time)
		except:
			pass
		else:
			q.put(proxy)
	else:
		q.put(proxy)

def setup():
	global num_thread
	global all_proxies
	global output_file
	global source_file
	global delay

	all_proxies = int(input("Start from? (default 0) set to: "))
	num_thread = int(input("number of thread?: "))
	delay = int(input("max delay?: "))
	output_file = input("output file name: ")
	source_file = input("name of file with proxis: ")

num_thread=10
all_proxies=0
output_file = ""
source_file = ""
delay = 30
proxies = []

setup()
num_lines = sum(1 for line in open(source_file))
urllib3.disable_warnings()

with open(source_file) as f:
	content = f.readlines()
	content = [x.strip() for x in content] 
	for c in content:
		proxies.append(c)

while all_proxies < num_lines:
	print("new set!")
	threads = []
	q = queue.Queue()
	good_proxies = 0

	for num in range(num_thread):
		t= threading.Thread(target=thread_function,args=(str(proxies[all_proxies]),q,delay))
		t.start()
		threads.append(t)
		all_proxies +=  1
		
	for t in threads:
		t.join()

	output = open(output_file,"a")	
	while not q.empty():
		final_proxy = q.get() + "\n"
		output.write(final_proxy)
		good_proxies +=1
		
	print("good: " + str(good_proxies))
	print("done: " + str(all_proxies))
	output.close()

	num_th_handler = num_lines-all_proxies
	if not num_th_handler - num_thread > 0:
		num_thread = num_th_handler 