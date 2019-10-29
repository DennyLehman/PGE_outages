import os
import json
import time

class Parser(object):
	"""docstring for Parser"""
	def __init__(self, data=None, file=None):
		super(Parser, self).__init__()
		print('Parser constructor')
		self.app_folder = self.get_app_dir()
		self.data = self.load_data(file, data)
		


	def load_data(self, file, data):
		try:
			if file:
				data = self.load_payload_to_memory(file_name=file)
				return data

			elif data:
			# get data from memory or json payload
				return data
			else:
				print('data incorrectly passed to parser. Add error handling here...')
		except Exception as e:
			raise e

		print('error in data loading')
		return None

	def make_file_path(self, file_name, sub_directory=''):
				
		folder_path = os.path.join(self.app_folder, 'raw_data', sub_directory)

		self.setup_directories(folder_path)

		file_path = os.path.join(folder_path, file_name)

		return file_path

	def load_payload_to_memory(self, file_name, sub_directory=''):
		
		file_name = self.make_file_path(file_name=file_name, sub_directory=sub_directory)
		
		with open(file_name) as json_file:
		
			data = json.load(json_file)	
		
		return data

	def setup_directories(self, folder_path):

		path_existed = True

		if not os.path.exists(folder_path):
			
			os.makedirs(folder_path)
			
			print('new folder path created: ', folder_path)

			path_existed = False
		
		return path_existed
	
	def get_app_dir(self):
		
		return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	def parse_outages(self,outage):
		_cause = outage['customersAffected']
		_crewCurrentStatus = outage['id']
		_estCustAffected = outage['estCustAffected']
		_hazardFlag = outage['hazardFlag']
		_lastUpdateTime = outage['lastUpdateTime']
		_latitude = outage['latitude']
		_longitude = ['longitude']
		_outageNumber = outage['outageNumber']
		_outageStartTime = outage['outageStartTime']

		pass

	# load data and initialize
		#from file, from memory
	#parsing setps
	# 1 get outagesRegions (a list of dictionaries) 
	#{"validationErrorMap":{},"validationErrors":[],"outagesRegions":[{"id":"2264165077","regionName":"Millville","numOutages":"6","customersAffected":"995","latitude":"40.61727","longitude":"-121.9334","outages":[{"outageNumber":"684042","outageStartTime":"1572139320","crewCurrentStatus":"PG&E has assigned a crew to assess the outage.","cause":"To protect public safety, power in your area has been turned off due to extreme weather conditions with high fire danger. Power will be restored as soon as it is safe to do so.","estCustAffected":"168","lastUpdateTime":"1572294637","hazardFlag":"0","latitude":"40.61727","longitude":"-121.9334","outageDevices":[{"latitude":"40.5831","longitude":"-121.93309"},
	# 2 parse data
	# 3 parse outages, a list of outages
	# 4 make relationship in sql between outages regions and outages

	def parse_regions(self):
		outagesRegions = self.data["outagesRegions"]
		d = {}
		d['time_stamp'] = time.time()
		d['data'] = {}
		i = 0 
		for outreg in outagesRegions:
			# outreg a dictionary
			_id = outreg['id']
			_regionName = outreg['regionName']
			_numOutages = outreg['numOutages']
			_customersAffected = outreg['customersAffected']
			_latitude = outreg['latitude']
			_longitude = outreg['longitude']
			_outages = outreg['outages']

			#this is redundant, I know, but it'll be important if we put this in a database instead
			d['data']['id'] = _id
			d['data']['regoionName'] = _regionName
			d['data']['numOutages'] = _numOutages
			d['data']['customersAffected'] = _customersAffected
			d['data']['latitude'] = _latitude
			d['data']['longitude'] = _longitude
			#d[i]['id'] = 
			#print(d)
			i = i+1

			if i >= 0:
				return d

		pass

	def make_sql_string(self):
		pass

if __name__ == '__main__':
	file_path = r'C:\Users\slin2\Documents\GitHub\PGE_outtages\raw_data\data_from_1572300640.9877114.txt'
	my_parser = Parser(file=file_path)
	#print(my_parser.data)
	print(my_parser.get_app_dir())
	print(my_parser.parse_regions())