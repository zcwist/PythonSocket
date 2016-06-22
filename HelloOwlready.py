from owlreadyutil.OntoImporter import Ontology

if __name__ == '__main__':
	# getOntology("/home/kiwi/Downloads/","pizzaowl.owl")
	# print (onto.classes)
	onto = Ontology("./","DomainOntology").getOntologyCopy()
	print (vars(onto.classes[0]))
	# for concept in onto.classes:
	# 	print (concept.annotation_properties)
