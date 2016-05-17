from owlready import *
from shutil import copyfile

class Ontology(object):
	"""docstring for Ontology"""
	def __init__(self, filepath, filename):
		super(Ontology, self).__init__()
		onto_path.append(filepath)
		self.filepath = filepath
		self.filename = filename
		

	def getOntology(self):
		
		onto = get_ontology("http://self.zac/" + self.filename + '.owl')
		return onto.load()

	def getOntologyCopy(self):
		copyfile(self.filepath + self.filename + '.owl', self.filepath + self.filename + '_copy.owl')
		onto = get_ontology("http://self.zac/" + self.filename + '_copy.owl')
		return onto.load()



if __name__ == '__main__':
	# onto = Ontology("/home/kiwi/Downloads/","pizzaowl.owl")
	onto = getOntology();
	print (onto.classes)
