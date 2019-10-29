import os
import requests
import json
import time

class Fetcher(object):
	"""docstring for Fetcher"""
	def __init__(self):
		super(Fetcher, self).__init__()
		self.app_folder = self.get_app_dir()

	def call_api(self, url):
		response = requests.get(url)
		json_data = json.loads(response.content)

		return	json_data

	def make_url(self):
		# add any html config here
		return r'https://apim.pge.com/cocoutage/outages/getOutagesRegions?regionType=city&expand=true'

	def handle_request(self, response):
		# add handle code here
		file_name = 'data_from_'+str(time.time())+'.txt'
		sub_directory = '' # one day, make subdirectory something to do with dates/months
		payload = self.write_payload(response, file_name, sub_directory)
		return response, payload

	def run(self):

		try:
			url = self.make_url()
			response, payload = self.handle_request(self.call_api(url))
		except Exception as e:
			raise e
		return [payload, response]

	def make_file_path(self, file_name, sub_directory=None):
				
		folder_path = os.path.join(self.app_folder, 'raw_data', sub_directory)

		self.setup_directories(folder_path)

		file_path = os.path.join(folder_path, file_name)

		return file_path

	def setup_directories(self, folder_path):

		path_existed = True

		if not os.path.exists(folder_path):
			
			os.makedirs(folder_path)
			
			print('new folder path created: ', folder_path)

			path_existed = False
		
		return path_existed

	def save_payload_to_file(self, file_directory, file_name):
		
		pass

	def verify_payload_not_empty(self, payload):
		
		empty_payload = False
		
		if not payload:
		
			print('Error: Empty Payload [write_payload method]')
		
			payload = 'Empty payload'

			empty_payload = True

		return payload, empty_payload
		

	def write_json_to_file(self, payload, file):

		with open(file, 'w+') as f:

			json.dump(payload, f)

		print('data succesfully written to file')

		return True
	
	def write_payload(self, payload, file_name, sub_directory):
		
		payload, empty_payload = self.verify_payload_not_empty(payload)

		file = self.make_file_path(file_name, sub_directory)
		
		clean_write = self.write_json_to_file(payload, file)
		
		return file

	def get_app_dir(self):
		
		return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
	print('hello world')
	my_fetcher = Fetcher()
	print('Fetcher made')
	filename, payload = my_fetcher.run()
	print(filename)