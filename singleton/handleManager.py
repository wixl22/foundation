from src.foundation.singleton.singleton import Singleton


class HandleManager(Singleton):
	"""
	HandleManager is Singleton class that store data by key
	"""
	def singleton_init(self):
		self.handlers = {}

	def get(self, name):
		self.handlers.get(name, None)

	def add(self, name, obj):
		self.handlers[name] = obj
