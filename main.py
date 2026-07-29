import argparse
import os
from src.kmer import count_kmers, k_mer_freqs
from src.gc_content import gc_content, sliding_gc_content, gc_skew, cumulative_gc_skew
from src.k_mer_plot import plot_kmer_freqs, plot_sliding_gc, plot_cumulative_skew
from src.read_fasta import read_fasta

script_dir = os.path.dirname(os.path.abspath(__file__))
default_output = os.path.join(script_dir, "kmer_gc_output")



def build_parser():

    parser = argparse.ArgumentParser(description="Analyse k-mer and GC content from a FASTA file")
    parser.add_argument("--fasta", required = True, help = "Path to input fasta file")
    parser.add_argument("--k", type = int, default = 4, help = "k-mer length (default: 4)")
    parser.add_argument("--window", type = int, default = 250, help = "Window size (default:250)")
    parser.add_argument("--step", type = int, default = 125, help = "Step size (default: 125)")
    parser.add_argument("--output_path", "-o", type = str, default = default_output, help = "Path where output is saved (default: kmer_gc_output/ next to main.py)")

    return parser





def run(args):
    
    os.makedirs(args.output_path, exist_ok = True) 

    records = read_fasta(args.fasta)

    for seq_id, seq in records:

        print(f"\n== {seq_id} ({len(seq)} bp) ==")

        base_name = f"{seq_id}"
        
        # gc content 
        
        overall_gc = gc_content(seq)
        overall_skew = gc_skew(seq)
        print(f"GC content = {overall_gc:.2f} \nGC skew = { 'N/A' if overall_skew is None else f'{overall_skew:.2f}'}")
        
        # k-mer freq and its plot
    
        
        freqs = k_mer_freqs(seq, args.k)
        plot_kmer_freqs(freqs, output_path = os.path.join(args.output_path, f"{base_name}_kmer_freq.png"))


        # sliding gc content plot
       
        current_slide = sliding_gc_content(seq, args.window, args.step)

        plot_sliding_gc(current_slide, output_path = os.path.join(args.output_path, f"{base_name}_sliding_gc.png"))

        #cumulative GC and its plot

        cumulative_data = cumulative_gc_skew(seq)

        plot_cumulative_skew(cumulative_data, output_path = os.path.join(args.output_path, f"{base_name}_cumulative_skew.png"))




if __name__ == "__main__":

    parser =  build_parser()
    args = parser.parse_args()
    run(args)
