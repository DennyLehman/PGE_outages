import os
import json
import time

class Parser(object):
	"""docstring for Parser"""
	def __init__(self, data=None, file=None):
		super(Parser, self).__init__()
		self.data = self.load_data(file, data)

	def load_data(self, file, data):
		try:
			if file:
				# get data from file
				with open(file) as f:
					data = json.load(f)
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

	def make_file_path(self, file_name, sub_directory=None):
				
		folder_path = os.path.join(self.app_folder, 'raw_data', self.company_name, self.equipment_company_name, sub_directory)

		self.setup_directories(folder_path)

		file_path = os.path.join(folder_path, file_name)

		return file_path

	def load_payload_to_memory(self, file_name, sub_directory=None):
		
		file_name = self.make_file_path(file_name=file_name, sub_directory=sub_directory)
		
		with open(file_name) as json_file:
		
			data = json.load(json_file)	
		
		return data

	
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

			d[i]['id'] = 
			print('hi')
			i = i+1

		pass

	def retrieve_data(self, tag):
		try:
			pass
		except Exception as e:
			raise e

		pass

	def make_sql_string(self):
		pass