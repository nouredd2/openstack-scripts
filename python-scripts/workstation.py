class Workstation(object) :
	def __init__(self, mid):
		self.__type = ''
		self.__replicates = 1
		self.__OStype = 'Ubuntu 16.04'
		self.__name = ''
		self.__id = mid
		self.__flavor = ''
	def setType(self, type):
		self.__type = type
	def setReplicates(self, replicates):
		self.__replicates = replicates
	def setOStype(self, OStype):
		self.__OStype = OStype
	def setName(self, name):
		self.__name = name
	def setflavor(self, flavor):
		self.__flavor = flavor
	def getType(self):
		return (self.__type)
	def getReplicates(self):
		return(self.__replicates)
	def getOStype(self):
		return(self.__OStype)
	def getName(self):
		return(self.__name)
	def getid(self):
		return(self.__id)
	def getFlavor(self):
		return(self.__flavor)
	def Print(self):
		print ('name= '+self.getName())
		print (self.getType())
		print (self.getReplicates())
		print (self.getOStype())
		print (self.getFlavor())

