import spacy
nlp = spacy.load('en')

doc1=nlp(u'this is a document similarity calculation')
doc2=nlp(u'this is a python document similarity calculation')
doc3=nlp(u'hi there')

print(doc1.similarity(doc2))
print(doc2.similarity(doc3))
print(doc1.similarity(doc3))
