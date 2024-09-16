### Exercise: DNA to Amino Acid Converter (`DNA_to_AA.py`)
#### Task:
Write a Python script, `DNA_to_AA.py`, that converts a DNA sequence to its corresponding Amino Acid sequence by performing the following steps:
1. Take user DNA input
2. Convert a DNA sequence to RNA.
3. Translate RNA to Amino Acids using the below dictionary.
4. Use functions to break down the process.
5. Output the Amino Acid sequence to the terminal.
6. Fold the protein! Use [ESMFold](https://esmatlas.com/resources?action=fold) web version.

RNA to AA dictionary:
```python
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
```

Our `mystery_protein.fa`:
```
>mystery_protein_seq
ATGGACAAGGACGAGGCGTGGAAGTGCGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATAGTGGACGCGACGGACAAGGACGAGGCGTGGAAGCAGGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATAGTGGACGCGACGGACAAGGACGAGGCGTGGAAGCAGGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATAGTGGACGCGACGGACAAGGACGAGGCGTGGAAGCAGGTGGAGCAGCTGAGGAGGGAGGGGGCGACGCAGATAGCGTACAGGAGCGACGACTGGAGGGACCTGAAGGAGGCGTGGAAGAAGGGGGCGGACATACTGATATGCGACGCGACGGGGCTGGAGCACCACCACCACCACCAC
```
Expected terminal output:
```terminal
python DNA_to_AA.py

Where is the path to the DNA sequence file? ./mystery_protein.fa

DNA -> RNA: (saved in ./output_RNA.fa)
AUGGACAAGGACGAG

RNA -> AA: (saved in ./output_AA.fa)
MDVDE
```
### For next class:
```bash
# Downlaod miniconda installer:
wget -O ./miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Then run the installer:
bash ./miniconda.sh
```