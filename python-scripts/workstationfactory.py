import workstation as ws

class WorkstationFactory:
	def __init__ (self):
		self.current_id = 0
		self.map = dict()
	def createWorkstation(self):
		w = ws.Workstation(self.current_id)
		self.current_id = self.current_id + 1
		return w
	def addWorkstation(self, w):
		if type(w) is ws.Workstation:
			self.map[w.getName()] = w
		else:
			print ('ERROR: variable must be workstation type')
	def searchWorkstation(self, name):
		if name in self.map:
			return self.map[name]
		else:
			print('Error: '+name+'is not a defined workstation')
			return None
