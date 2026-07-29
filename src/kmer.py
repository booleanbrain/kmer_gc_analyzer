
def count_kmers(seq, k):

    # k_mers = n - k + 1
    # n = k_mer length
    # k = k_mer size
    seq = seq.upper()
    counts = {}
    kmer_range = len(seq) - k + 1 # max number of k-mers

    bases = set("AGCT")



    for i in range(kmer_range):
        kmer = seq[i:i+k]               # cutting the seq into fragments of length k
        
        if not set(kmer).issubset(bases):
            continue
            

        counts[kmer] = counts.get(kmer, 0) + 1
            

    return counts




def k_mer_freqs(seq, k):

    counts = count_kmers(seq, k) #uses count_kmers function to return a dict containing k-mers and number of occurneces

    total = sum(counts.values()) # total number of k-mers

    freqs = {} # stores k-mer frequencies as a dict. k-mers are keys and freq of the k-mer is value

    for kmer, count in counts.items():
        freqs[kmer] = count / total # calculating the freq of the k-mer

    return freqs


