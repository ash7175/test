import random
import collections
nucleotides = ['A', 'T', 'G', 'C']
def validate_seq(seq):
    temp_seq = seq.upper()
    for nuc in temp_seq:
        if nuc not in nucleotides:
            return 'Sequence is not valid'
            break
    return temp_seq
    
def count_nuc(seq):
    seq = seq.upper()
    validate_seq(seq)
    temp_freq_dict = {'A':0,
                      'T':0,
                      'G':0,
                      'C':0
                      }
    for nuc in seq:
        temp_freq_dict[nuc] += 1
    return temp_freq_dict
    #return dict(collections.Counter(seq))
    
    

sequence = ''.join([random.choice(nucleotides) for nuc in range(50)])
print(validate_seq(sequence))
result = count_nuc(sequence)
print(result)
print(' '.join([str(val) for val in result.values()]))