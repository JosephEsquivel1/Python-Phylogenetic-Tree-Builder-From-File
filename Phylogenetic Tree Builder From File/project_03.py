"""
CS/BIOS 112 - Project 03: the phylogenetic Tree of Life

File: project_03.py

   Describe
   Assignment 
   Here
   

@author:    <your name here>
UIC NetID:  <your NetID here>
Due Date:   <due date here>
"""

def build_dict(  ):
    '''describe function here'''
    pass

def list_ancestors( ):
    '''describe function here'''
    pass

def root( ):
    '''describe function here'''
    pass

def kids( ):
    '''describe function here'''
    pass

def common_ancestor( ):
    '''describe function here'''
    pass


"""
def c_ancestor( ):
    '''describe function here'''
    pass
"""

"""
# examples from project write-up
list_ancestors(’Pan troglodytes’, tax_dict)
#Out[1]: [’Pan troglodytes’, ’Hominoidea’, ’Simiiformes’, ’Haplorrhini’, ’Primates’]

common_ancestor([’Hominoidea’, ’Pan troglodytes’], tax_dict)
#Out[2]: ’Hominoidea’

common_ancestor([’Hominoidea’, ’Pan troglodytes’, ’Lorisiformes’], tax_dict)
#Out[3]: ’Primates’

common_ancestor([’Hominoidea’, ’Pongo abelii’], tax_dict)
#Out[4]: ’Hominoidea’

#c_ancestor([’Hominoidea’, ’P. abelii’], tax_dict)
#Out[5]: ’Hominoidea’

root(tax_dict)
#Out[6]: ’Primates’

kids(’Primates’, tax_dict)
#Out[7]: [’Haplorrhini’, ’Strepsirrhini’]
'''