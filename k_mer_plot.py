import matplotlib.pyplot as plt



def plot_kmer_freqs(freqs, output_path):
    

    kmers = list(freqs.keys())
    k_freqs = list(freqs.values())

    fig, ax = plt.subplots()

    ax.bar(kmers, k_freqs)
    ax.set_xlabel("k-mers")
    ax.set_ylabel("frequency")
    ax.set_title("k-mer frequencies")

    
    plt.savefig(output_path)

    plt.close(fig)




def plot_sliding_gc(data, output_path):


    # data = list of (position, gc) tuple

    pos, gc = zip(*data)
    

    fig, ax = plt.subplots()

    ax.plot(pos, gc)
    ax.set_xlabel("position on sequence")
    ax.set_ylabel("GC content (%)")
    ax.set_title("GC content")


    plt.savefig(output_path)
    plt.close(fig)




def plot_cumulative_skew(cumulative_data, output_path):

    fig, ax = plt.subplots()
    
    min_index = cumulative_data.index(min(cumulative_data))

    max_index = cumulative_data.index(max(cumulative_data))
    
    ax.axvline(x = min_index, color = "gray", linestyle="--")
    ax.axvline(x = max_index, color = "gray", linestyle="--")




    ax.plot(cumulative_data)
    ax.set_xlabel("Position on sequence")
    ax.set_ylabel("Cumulative GC skew")
    ax.set_title("Cumulative GC skew")


    plt.savefig(output_path)
    plt.close(fig)







