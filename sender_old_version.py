import requests

def test_http_proxy(proxy):
	proxies = {
	  'http': 'http://'+proxy,
	  'https':'http://'+proxy,
	}
	try:
		r = requests.get("https://www.youtube.com",proxies = proxies)
	except:
		return 0
	else:
		return 1

def test_socks_proxy(proxy):
	proxies = {
	  'http': 'socks5://'+proxy,
	  'https':'socks5://'+proxy,
	}
	try:
		r = requests.get("https://www.youtube.com",proxies = proxies)
	except:
		return 0
	else:
		return 1