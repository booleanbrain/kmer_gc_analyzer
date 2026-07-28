# k-mer GC Analyzer
---

## Features

- **$k$-mer analysis:**
	- Fast $k$-mer exraction and frequency counting.
	- Automatic filtering of non-standard bases (e.g., non-'Agct" ambigous bases).
- **GC Content & Skew Metrics:**
	- Single $k$-mer or sequence GC content calculation.
	- **GC Skew** calculation: $\frac{G - C}{G + C}$
	- **Cumulative GC Skew:** tracking acrossentire sequences (useful for identifying origins of replication, e.g., *oriC*).
	- **Sliding Window Analysis:** Measure localized GC dynamics using cutomisable 'window_size' and 'step_size'.
-**Graphical Visualisations:**
	- **$k$-mer Frequency Plot:** Bar charts of $k$-mers.
	- **Sliding GC plot:** GC percentage distribution along sequence coordinates.
	- **Cumulative Skew Plot:** Visualising peak/valley inflection points across a genome.

---

## Prerequisites & Installation

## Requirments

--**Python 3.8+**
--**'matplotlib** for generatiing graphs

## Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/booleanbrain/kmer_gc_analyzer.git](https://github.com/booleanbrain/kmer_gc_analyzer.git)
   cd kmer_gc_analyzer
