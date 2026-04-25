DATA_PATH = r'../data/splice.data'
CLEAN_DATA_PATH = r'../data/splice_clean.csv'
COLUMNS = ["class", "name", "sequence"]
ENCODING = {
    'A': [1,0,0,0,0,0,0,0],
    'T': [0,1,0,0,0,0,0,0],
    'G': [0,0,1,0,0,0,0,0],
    'C': [0,0,0,1,0,0,0,0],
    'N': [0,0,0,0,1,0,0,0],
    'D': [0,0,0,0,0,1,0,0],
    'R': [0,0,0,0,0,0,1,0],
    'S': [0,0,0,0,0,0,0,1]
}

def encode_sequence(sequence):
    vector = []
    for nucleotide in sequence:
        vector += ENCODING[nucleotide]
    return vector