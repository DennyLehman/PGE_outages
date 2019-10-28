import os
import requests
import json

class Fetcher(object):
	"""docstring for Fetcher"""
	def __init__(self):
		super(Fetcher, self).__init__()

	def call_api(self, url):
		response = requests.get(url)
		json_data = json.loads(response.content)

		return	json_data

	def make_url(self):
		# add any html config here
		return r'https://apim.pge.com/cocoutage/outages/getOutagesRegions?regionType=city&expand=true'

	def handle_request(self, response):
		# add handle code here
		return response

	def run(self):

		try:
			url = self.make_url()
			payload = self.handle_request(self.call_api(url))
		except Exception as e:
			raise e
		return payload
		


if __name__ == '__main__':
	print('hello world')
	my_fetcher = Fetcher()
	print('Fetcher made')
	payload = my_fetcher.run()
	print(payload)