"""
CS/BIOS 112 - Project 03: the phylogenetic Tree of Life

File: project_03.py

Builds a phylogenetic tree dictionary from input read off of a CSV file,
and then uses this dictionary to assess taxon ancestry, the taxon root of the 
tree, any immediate taxon offpsring, and any common ancestors.


@author:    Joseph Esquivel
UIC NetID:  Jesqui20
Due Date:   12-4-2020 (1 Day-Late Pass Used: Submitted 12-5-2020)
"""

def build_dict(File_Name):
    '''Generates a dictionary that maintains the taxon-parent association,
    therefore mapping keys to taxons, and then mapping their associated
    parent/ancestor with a value (if one exists). The pattern then repeats for
    the newly mapped ancestor. This is a phylogenetic tree in dictionary form.
    '''
    import csv
    Data = []
    Life_Tree_Dict = {}
    with open(File_Name, 'r', newline = '') as f:
        data_reader = csv.reader(f)
        Data = []
        for row in data_reader:
            Data.append(row)
        
      
        for x in Data:
            Life_Tree_Dict[x[0]] = x[1]
        
        
    return Life_Tree_Dict
    


def list_ancestors(Taxon_Name, Life_Tree_Dict):
    '''Appends specified Taxon from argument, then traces and appends each
    preceding ancestor (parent) to a list and returns this built list. The 
    ancestors are traced using the phylogenetic tree specified in the argument
    '''
    Ancestor_List = []
    
    while Taxon_Name != 0:
        Ancestor_List.append(Taxon_Name)
        Taxon_Name = Life_Tree_Dict.get(Taxon_Name, 0)
    return Ancestor_List



def root(Phylogenetic_Tree):
    ''' Traces the root of the tree, i.e. the ancestral taxon at the base
    of the tree, given a phylogenetic tree. Not having parents, the ancestor 
    is not a key and this is the method of search.'''
    Root = ''
    for Value in Phylogenetic_Tree.values():
        if Value not in Phylogenetic_Tree.keys():
            Root += Value
            return Root
    return Root




def kids(Taxon_Name,Phylogenetic_Tree):
    '''Given a phylogenetic tree mapping the association of offspring to
    ancestor, this function returns any immediate offspring for the specified
    taxon, using its provided, relevant phylogenetic tree.'''
    Kids = []
    for Key in Phylogenetic_Tree.keys():
        if Phylogenetic_Tree[Key] == Taxon_Name:
            Kids.append(Key)
    return Kids
    
    
    

def common_ancestor(Taxon_List, Phylogenetic_Tree):
    '''Utilizes the list_ancestor function for each taxa listed in the first
    argument, and uses the provided dictionary from the second argument to 
    search each ancestor until the first common ancestor is found and returned.
    '''
    
    Shortest_Ancestor_List = []
    Common_Ancestor_Boolean = False
    Ancestry_List = []
    
    
    for Taxon in Taxon_List:
        Ancestry_List.append(list_ancestors(Taxon,Phylogenetic_Tree))
        
    Shortest_Ancestor_List = Ancestry_List[0]
   
    for Ancestor_List in Ancestry_List:
        if len(Ancestor_List) < len(Shortest_Ancestor_List):
            Shortest_Ancestor_List = Ancestor_List
            
 
        for Taxon in Shortest_Ancestor_List:
            for Ancestor_List in Ancestry_List:
                if Taxon in Ancestor_List:
                    Common_Ancestor_Boolean = True
                else:
                    Common_Ancestor_Boolean = False
            if Common_Ancestor_Boolean == True:
                return Taxon
            
#Below is an example of how to test that the functions work adequately:
#print(common_ancestor(['Hominoidea', 'Pan troglodytes', 'Lorisiformes'], build_dict('tax_dict.csv')))            
              

'''
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