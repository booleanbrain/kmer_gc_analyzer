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

