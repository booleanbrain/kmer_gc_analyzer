def read_fasta_func(path): #to return list of (seq_id, sequence) tuples
    
    records = []
    current_id = None
    current_seq_parts = []

    with open(path) as f:
        for line in f:
            line = line.strip() #remove unwanted spaces

            if line.startswith('>'):
                if current_id is not None: # append previous record before starting a new one
                    full_seq = "".join(current_seq_parts).upper() # to join the read lines stored as items of the list  
                    records.append((current_id, full_seq)) #append the sequence to the tuple

                current_id = line[1:].split()[0] # extract seq_id from the FASTA file
                current_seq_parts = [] # store the read lines as list items

            else:
                if line: # to avoid blank lines
                    current_seq_parts.append(line) # append the seq if a blank space is present

        if current_id is not None: # to save the last record
            full_seq = "".join(current_seq_parts).upper()
            records.append((current_id, full_seq))

    return records




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




def gc_content(seq):
    
    seq = seq.upper()

    total_bases = 0
    total_gc = 0
    gc_percent = 0

    for i in range(len(seq)): 
        if seq[i] in 'AGCT': 
            total_bases += 1
            if seq[i] in'GC':
                total_gc += 1

    if total_bases == 0:
        return 0.0
    
    gc_percent = (total_gc/total_bases) * 100

    return gc_percent




def gc_skew(seq):

    seq = seq.upper()

    g = seq.count('G')
    c = seq.count('C')
    
    if g+c == 0:
        return None

    output = (g - c) / (g + c)

    return output




def sliding_gc_content(seq, window, step):
    
    seq = seq.upper()
    results = []
    last_start = len(seq) - window + 1

    for start in range(0,last_start,step):
        
        chunk = seq[start:start+window]
            
        
        gc = gc_content(chunk)
        
        results.append((start, gc))

    return results




def cumulative_gc_skew(seq):

    seq = seq.upper()

    cumulative = []
    skew = 0

    for i in seq:
        if i == "G":
            skew += 1
        elif i ==  "C":
            skew -= 1
        cumulative.append(skew)

    return cumulative
        



