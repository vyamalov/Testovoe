import requests
urls=['https://www.google.com', 'https://ru.investing.com']
def get_result(url_list):
	for url in url_list:
		r = requests.get(url)
		with open(f'{url.replace("/", "|")}.html', 'w') as result:
			result.write(r.text)
get_result(urls)