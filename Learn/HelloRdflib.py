from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF


# g = rdflib.Graph()
# result = g.parse("http://www.w3.org/People/Berners-Lee/card")

# print ("graph has %s statements." % len(g))

# for subj, pred, obj in g:
# 	if (subj, pred, obj) not in g:
# 		raise Exception("It better be!")

# s = g.serialize(format='n3')

g = Graph()
donna = BNode()

g.add((donna, RDF.type, FOAF.Person))
g.add((donna, FOAF.nick, Literal("donna", lang="foo")))
g.add((donna, FOAF.name, Literal("Donna Fales")))
g.add((donna, FOAF.mbox, URIRef("mailto:donna@example.com")))

print ("--- printing raw triples ---")
for s, p, o in g:
	print ((s,p,o))

print ("--- printing mboxes ---")
for person in g.subjects(RDF.type, FOAF.Person):
	for mbox in g.objects(person, FOAF.mbox):
		print(mbox)

g.bind("dc",DC)
g.bind("foaf", FOAF)

print (g.serialize(format='n3'))