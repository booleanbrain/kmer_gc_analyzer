def read_fasta(path): #to return list of (seq_id, sequence) tuples

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


