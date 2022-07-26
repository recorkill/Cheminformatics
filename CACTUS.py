from urllib.request import urlopen
from urllib.parse import quote
import pubchempy
from pubchempy import Compound, get_compounds

def PubChem_SMILES(name):
    for compound in get_compounds(name, 'name'):
        #print(compound.cid)
        #print(compound.isomeric_smiles)
        smiles = compound.isomeric_smiles
        return smiles

def CIRconvert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        try: #Catches names that aren't in CACTUS and are in PubChem
            ans2 = PubChem_SMILES(ids)
            return ans2
        except:
            return 'Did not work'

test_identifiers = ['isoproterenol', 'genistein', 'niflumic acid', 'glyburide', 'staurosporine', 'ivacaftor', 'lumacaftor']

for ids in test_identifiers :
    print(ids, CIRconvert(ids))

