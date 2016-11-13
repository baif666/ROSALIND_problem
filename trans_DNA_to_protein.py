#Use a dictionary to look up compared amino acid
d = {
        'TTT':'F','CTT':'L','ATT':'I','GTT':'V',
        'TTC':'F','CTC':'L','ATC':'I','GTC':'V',
        'TTA':'L','CTA':'L','ATA':'I','GTA':'V',
        'TTG':'L','CTG':'L','ATG':'M','GTG':'V',
        'TTT':'S','CCT':'P','ACT':'T','GCT':'A',
        'TTC':'S','CCC':'P','ACC':'T','GCC':'A',
        'TTA':'S','CCA':'P','ACA':'T','GCA':'A',
        'TTG':'S','CCG':'P','ACG':'T','GCG':'A',
        'TTT':'Y','CAT':'H','AAT':'N','GAT':'D',
        'TAC':'Y','CAC':'H','AAC':'N','GAC':'D',
        'TAA':'Stop','CAA':'Q','AAA':'K','GAA':'E',
        'TAG':'Stop','CAG':'Q','AAG':'K','GAG':'E',
        'TGT':'C','CGT':'R','AGT':'S','GGT':'G',
        'TGC':'C','CGC':'R','AGC':'S','GGC':'G',
        'TGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
        'TGG':'W','CGG':'R','AGG':'R','GGG':'G'
        }

def DtoP(x):
    '''Translate DNA to amino acid.'''

    if len(x) % 3 != 0:
        raise ValueError("Input length should be a multiple of three.")

    y = ''
    for i in list(range(int(len(x)/3))):
        y += d[x[i*3:i*3+3]]
    return y

if __name__ == '__main__':

    #Input your DNA sequences
    x = input("Please input your DNA sequences : ")

    print(DtoP(x))
