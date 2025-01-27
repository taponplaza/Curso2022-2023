# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fthTgWnQbztAYsTFDVCqKcDEOZ-HhHtQ

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
from rdflib.plugins.sparql import prepareQuery
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person.
  }
  ''',
  initNs = {"rdfs":RDFS, "ns":ns}
)

# Visualize the results
for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO

q2 = prepareQuery('''
  SELECT DISTINCT ?person
  WHERE { 
    {?Subject rdfs:subClassOf ns:Person.
    ?person rdf:type ?Subject.}
    UNION
    {?person rdf:type ns:Person.}
  }
  
  ''',
  initNs = {"rdfs":RDFS, "rdf":RDF, "ns":ns}
)

# Visualize the results
for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
q3 = prepareQuery('''
  SELECT DISTINCT ?person ?prop ?value
  WHERE { 
    {?Subject rdfs:subClassOf ns:Person.
    ?person rdf:type ?Subject.}
    UNION
    {?person rdf:type ns:Person.}
    ?person ?prop ?value
  }
  
  ''',
  initNs = {"rdfs":RDFS, "rdf":RDF, "ns":ns}
)

# Visualize the results
for r in g.query(q3):
  print(r)