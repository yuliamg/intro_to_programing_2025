'''
Input: DNA sequence file (fasta)

Algo:
0) Input handeling
    --> def get_DNA_seq_from_input_file( path_to_file -> str )
        return DNA_sequence -> String

1) convert DNA to RNA (DNA --> RNA)
    --> def DNA_to_RNA( DNA --> Str )
        return RNA --> str

2) RNA to Amino Acids
    --> def RNA_to_AA( RNA --> str)
        return AA --> str

Output:
1) RNA sequence to terminal and file
2) AA sequence to the terminal and file
'''

genetic_code = {
    'AUG': 'M', 
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}

def get_DNA_seq_from_input_file( path_to_file ):
    '''
    Function takes in path of DNA seq file
    Returns DNA seq

    Pseudocode:
    open path_to_file as a read-only file
    content = file.readcontent()

    DNA_seq = content[-1].strip()

    return DNA_seq
    '''

    with open( path_to_file , 'r' ) as file:
        content = file.readlines()
    
    DNA_seq = content[-1]

    DNA_seq = DNA_seq.strip()

    return DNA_seq



def DNA_to_RNA( DNA_seq ):
    '''
    Pseudocode:
    results = ''
    for every base in DNA:
        if bsae is T convert to U
            results+='U'
        else:
            results+= base


    ATGGACAAGG
    '''

    results = ''

    for base in DNA_seq:
        if base is 'T':
            results += 'U'
        else:
            results += base

    return results


def RNA_to_AA (RNA_seq , genetic_code):
    '''
    Psuedocode:
    load RNA seq
    AA = ''
    look at 3 bases at a time, up until the end of the RNA_seq
    if mathc found 3bases to key:
        AA += extract value
    
    return AA
    '''

    AA = ''

    print(len( RNA_seq ))
    print(list(range( 0, len( RNA_seq ), 3 )))

    for idx in range( 0, len( RNA_seq ), 3 ):

        working_codon = RNA_seq[idx : idx + 3]

        AA += genetic_code[ working_codon ]
    
    return AA



DNA_seq = get_DNA_seq_from_input_file('./mystery_protein.fa')

RNA_seq = DNA_to_RNA( DNA_seq )

AA = RNA_to_AA( RNA_seq, genetic_code )

print(AA)

# for num in list(range(1, 10, 3)):
#     print(num)


# print( list(range(10)) )

# print( len('AAA') )