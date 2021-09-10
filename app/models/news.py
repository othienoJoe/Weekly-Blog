class News:
	"""
	This News class file defines News Objects
	"""
	def __init__(self,id,title,overview,poster):
		self.id = id
		self.title = title
		self.overview = overview
		self.poster = 'file:///home/moringa/Pictures/Maguire.png'+ poster
		