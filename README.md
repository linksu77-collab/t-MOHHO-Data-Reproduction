# t-MOHHO-Data-Reproduction

This repository contains the dataset augmentation scripts and the original benchmark instances for the paper:  
**"t-MOHHO: An Adaptive Multi-Objective Harris Hawks Optimization Algorithm for Flexible Job Shop Scheduling"**

## 1. Overview
The Flexible Job Shop Scheduling Problem (FJSP) traditionally focuses on minimizing the makespan. In our research, we extend the classical MK benchmark instances (MK01–MK10) by incorporating economic (Processing Cost) and temporal (Due Date) objectives to evaluate our proposed t-MOHHO algorithm in a multi-objective manufacturing context.

## 2. Repository Structure
- `data/`: Contains the 10 original MK benchmark files (`mk01.txt` to `mk10.txt`) derived from Brandimarte (1993).
- `augmented_data/`: Contains the pre-generated augmented datasets (`.npy` format) used in our study for immediate use.
- `main_data_gen.py`: The core Python script used to transform original benchmarks into multi-objective datasets.
- `README.md`: This instruction file.

## 3. Data Augmentation Logic
To ensure strict reproducibility and fairness across all compared algorithms, the augmentation follows the deterministic logic described in Section 4.1 of the manuscript:

- **Random Seed**: Fixed at `np.random.seed(42)` for all stochastic processes.
- **Processing Cost**: Generated based on machine-specific unit cost factors ($\alpha \in [1.5, 3.0]$) and processing time.
- **Due Date**: Assigned using the Total Work Content (TWK) rule with a relaxation factor $\beta = 3$.

## 4. Usage
### Prerequisites
- Python 3.9+   
- NumPy

### Re-generating Data
To verify the data generation process, simply run:
```bash
python main_data_gen.py