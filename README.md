# 🧬 DNA Splice Junction Classification using SVM

A machine learning project that classifies DNA splice junctions using a Support Vector Machine (SVM) with RBF kernel, trained on the UCI Molecular Biology dataset.

## 📋 Problem Description

Splice junctions are points in a DNA sequence where "non-coding" regions (introns) are removed and "coding" regions (exons) are joined together. This project classifies 60-nucleotide DNA sequences into three categories:

- **EI** — Exon/Intron boundary
- **IE** — Intron/Exon boundary
- **N** — Neither

## 📊 Dataset

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/69/molecular+biology+splice+junction+gene+sequences)
- **Samples:** 3,190 DNA sequences
- **Features:** 480 (60 positions × 8 possible nucleotides, one-hot encoded)
- **Classes:** EI (767), IE (768), N (1655)

## 🛠️ Tech Stack

- Python 3.10
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn

## 📁 Project Structure
```
dna-splice-junction-svm/
│
├── data/
│   ├── splice.data          # Raw dataset
│   └── splice_clean.csv     # Cleaned dataset
│
├── notebooks/
│   ├── 01_eda.ipynb         # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb  # Encoding + Train/Test split
│   └── 03_svm_model.ipynb   # SVM Training + Evaluation
│
├── utils.py                 # Shared constants and functions
├── requirements.txt         # Dependencies
└── README.md
```

## 🔬 Methodology

### Preprocessing
- One-hot encoding of nucleotides (A, T, G, C, N, D, R, S)
- 75/25 train/test split with stratification

### Model
- **Algorithm:** Support Vector Machine with RBF kernel
- **Hyperparameter tuning:** GridSearchCV with 5-fold cross validation
- **C values:** 2⁻⁵, 2⁻³, ..., 2⁷
- **γ values:** 2⁻¹⁵, 2⁻¹³, ..., 2³

### Best Parameters
- **C:** 0.5
- **γ:** 0.03125

## 📈 Results

| Metric | Score |
|--------|-------|
| Accuracy | 95.86% |
| F1 (EI) | 0.95 |
| F1 (IE) | 0.93 |
| F1 (N) | 0.98 |

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/VladDumitru22/dna-splice-junction-svm.git
cd dna-splice-junction-svm

# Create and activate environment
conda create -n splice-svm python=3.10
conda activate splice-svm

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```