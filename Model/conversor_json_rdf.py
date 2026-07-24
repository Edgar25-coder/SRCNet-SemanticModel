from rdflib import Graph

# create RDF graph
g = Graph()

# read JSON-LD
g.parse(
"srcnet_model_01.json",
format="json-ld"
)

# show number of triples
print(f"Triples generados: {len(g)}")

# save Turtle
g.serialize(
destination="srcnet_model_01.ttl",
format="turtle"
)
