from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter1(object):
	""" CRUD operations for Animal collection in MongoDB """



	def __init__(self,username,password):
		# Initializing the MongoClient. This helps to 
		# access the MongoDB databases and collections.

		self.client = MongoClient('mongodb://%s:%s@localhost:37442' % (username, password), authSource="AAC")
		self.database = self.client['AAC']

# Complete theis create method to implement the C in CRUD.
	def create(self,data):
		
		
		if data is not None:
			self.database.animals.insert(data)	# data should be dictionary
			data = data
		else:
			raise Exception("Nothing to save, because data parameter is empty")
			data = false
		return data

# Complete this read method to implement the R in CRUD.
	def read(self,data):
		
		
		if data is not None:
			dataResult = self.database.animals.find(data,{"_id":False})	# data should be dictionary
			
		else:
			raise Exception("Nothing to save, because data parameter is empty")
			dataResult = false
		return dataResult

# Complete this read all method to implement the R in CRUD.
	def readAll(self,data):
		
		
		if data is not None:
			data = self.database.animals.find(data)	# data should be dictionary
			
		else:
			raise Exception("Nothing to save, because data parameter is empty")
			data = false
		return data

# Complete this update method to implement the U in CRUD.
	def update(self,data,dataUpdate):
		
		
		if data is not None:
			data = self.database.animals.update(data,dataUpdate)	# data should be dictionary
			
		else:
			raise Exception("Nothing to save, because data parameter is empty")
			data = false
		return data

# Complete this delete method to implement the D in CRUD.
	def delete(self,data):
		
		
		if data is not None:
			data = self.database.animals.remove(data)	# data should be dictionary
			
		else:
			raise Exception("Nothing to save, because data parameter is empty")
			data = false
		return data