from owlreadyutil.OntoImporter import Ontology


if __name__ == '__main__':
	# getOntology("/home/kiwi/Downloads/","pizzaowl.owl")
	# print (onto.classes)
	onto = Ontology("/home/kiwi/Downloads/","pizzaowl").getOntologyCopy()
	print (onto.properties)
	for p in onto.properties:
		print (get_relations(onto.classes[1], p))
