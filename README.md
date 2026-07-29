# k-mer GC Analyzer

---
A command-line tool for analyzing k-mer frequency and GC-content patterns
in FASTA sequences, including sliding-window GC content and cumulative
GC skew for locating replication origins.

## Features

- **$k$-mer analysis:**
	- Fast $k$-mer extraction and frequency counting.
	- Automatic filtering of non-standard bases (e.g., non-'Agct' ambiguous bases).
- **GC Content & Skew Metrics:**
	- Single $k$-mer or sequence GC content calculation.
	- **GC Skew** calculation: $\frac{G - C}{G + C}$
	- **Cumulative GC Skew:** tracking across entire sequences (useful for identifying origins of replication, e.g., *oriC*).
	- **Sliding Window Analysis:** Measure localized GC dynamics using cutomisable 'window_size' and 'step_size'.
- **Graphical Visualisations:**
	- **$k$-mer Frequency Plot:** Bar charts of $k$-mers.
	- **Sliding GC plot:** GC percentage distribution along sequence coordinates.
	- **Cumulative Skew Plot:** Visualising peak/valley inflection points across a genome.

---

## Prerequisites & Installation

### Requirements

- **Python 3.8+**
- **matplotlib** for generating graphs

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/booleanbrain/kmer_gc_analyzer.git
   cd kmer_gc_analyzer
	```
2. **Setup a virtual environment**
	```bash
   python3 -m venv venv
	```
3. **Activate the virtual environment**
    ```bash
    source venv/bin/activate	# macOS/Linux
    venv\Scripts\activate		# Windows
    ```
4. **Install the dependencies**
    ```bash
    pip install matplotlib
    ```

## Usage
  ```bash
    python3 main.py --fasta FASTA_FILE_PATH [--window WINDOW_SIZE] [--step STEP_LENGTH] [--output_path/-o OUTPUT_PATH] [--k K-MER_LENGTH]
  ```
- **Usage example:**
  ```bash
  python3 main.py --fasta tests/test.fasta --window 4 --step 2
  ```

## Output

- `<seq_id>_kmer_freq.png` - A bar graph depicting $k$-mer frequency
- `<seq_id>_sliding_gc.png` - A graph showing the GC content at different positions on the sequence
- `<seq_id>_cumulative_skew.png`- A graph showing cumulative skew along the sequence with max and min skew position marked

By default, the graphs are saved at  `kmer_gc_output/` folder, located in the same folder as main.py.

In addition, a short summary is printed in the terminal displaying GC content and GC skew


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
