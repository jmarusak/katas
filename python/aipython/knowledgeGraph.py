# knowledgeGraph.py - Knowledge graph triple store

from display import Displayable

class TripleStore(Displayable):
    Q = '?'  # query position
    
    def __init__(self):
        self.index = {}

    def add(self, triple):
        (sb,vb,ob) = triple
        Q = self.Q      # make it easier to read
        add_to_index(self.index, (Q,Q,Q), triple)
        add_to_index(self.index, (Q,Q,ob), triple)
        add_to_index(self.index, (Q,vb,Q), triple)
        add_to_index(self.index, (Q,vb,ob), triple)
        add_to_index(self.index, (sb,Q,Q), triple)
        add_to_index(self.index, (sb,Q,ob), triple)
        add_to_index(self.index, (sb,vb,Q), triple)
        add_to_index(self.index, triple, triple)

    def __len__(self):
        """number of triples in the triple store"""
        return len(self.index[(Q,Q,Q)])

    def lookup(self, query):
        """pattern is a triple of the form (i,j,k) where 
           each i, j, k is either Q or a value for the 
           subject, verb and object respectively.
        returns all triples with the specified non-Q vars in corresponding position
        """
        if query in self.index:
            return self.index[query]
        else:
            return []

def add_to_index(dict, key, value):
    if key in dict:
        dict[key].append(value)
    else:
        dict[key] = [value]

# test cases:
sts = TripleStore()  # simple triple store
Q = TripleStore.Q  # makes it easier to read
sts.add(('/entity/Q262802','http://schema.org/name',"Christine Sinclair"))
sts.add(('/entity/Q262802', '/prop/direct/P27','/entity/Q16'))
sts.add(('/entity/Q16', 'http://schema.org/name', "Canada"))

# sts.lookup(('/entity/Q262802',Q,Q))
# sts.lookup((Q,'http://schema.org/name',Q))
# sts.lookup((Q,'http://schema.org/name',"Canada"))
# sts.lookup(('/entity/Q16', 'http://schema.org/name', "Canada"))
# sts.lookup(('/entity/Q262802', 'http://schema.org/name', "Canada"))
# sts.lookup((Q,Q,Q))

def test_kg(kg=sts, q=('/entity/Q262802',Q,Q), res=[('/entity/Q262802','http://schema.org/name',"Christine Sinclair"), ('/entity/Q262802', '/prop/direct/P27','/entity/Q16')]):
   """Knowledge graph unit test"""
   ans = kg.lookup(q)
   assert res==ans, f"test_kg answer {ans}"
   print("knowledge graph unit test passed")

if __name__ == "__main__":
    test_kg()
    
# before using do:
# pip install rdflib

def load_file(ts, filename, language_restriction=['en']):
    import rdflib  
    g = rdflib.Graph()
    g.parse(filename)
    for (s,v,o) in g:
        if language_restriction and isinstance(o,rdflib.term.Literal) and o._language and o._language not in language_restriction:
            pass
        else:
            ts.add((str(s),str(v),str(o)))
    print(f"{len(g)} triples read. Triple store has {len(ts)} triples.")

TripleStore.load_file = load_file

#### Test cases ####
ts = TripleStore()
#ts.load_file('http://www.wikidata.org/wiki/Special:EntityData/Q262802.nt')
q262802 ='http://www.wikidata.org/entity/Q262802'
#res=ts.lookup((q262802, 'http://www.wikidata.org/prop/P27',Q)) # country of citizenship
# The attributes of the object in the first answer to the above query:
#ts.lookup((res[0][2],Q,Q))
#ts.lookup((q262802, 'http://www.wikidata.org/prop/P54',Q)) # member of sports team
#ts.lookup((q262802,'http://schema.org/name',Q))

