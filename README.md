# Next Book Prediction on Goodreads

CSE 158 (Fall 2026) Assignment 2 · Woosik, Shriya, Chase, Aung

Given the ordered sequence of books a user has interacted with, predict which book they will interact with next.

## Contents

| File | What it is |
|---|---|
| `assignment2.ipynb` | Main notebook: shared data pipeline, EDA, models, evaluation, related work |
| `requirements.txt` | Python packages needed to run the notebook |

## Setup

1. Install packages: `pip install -r requirements.txt`
2. Put `task_5_train.csv` (from the CSE 158 Assignment 1 data) in this folder. Data files are not committed.
3. Run `assignment2.ipynb` top to bottom (about 12 minutes on a laptop).

## Notebook sections

| Section | Owner |
|---|---|
| 0. Shared data pipeline and evaluation helpers | Woosik |
| 1. Predictive task, evaluation plan, baselines | Shriya |
| 2. Exploratory analysis and preprocessing | Chase |
| 3. Modeling | Woosik |
| 4. Evaluation | Aung |
| 5. Related work | Shriya |

Section 0 defines the train / validation / test split and the evaluation functions every model uses. Please do not change it without telling the team.

## Current results (test)

| Model | Pairwise accuracy | HR@10 | NDCG@10 |
|---|---|---|---|
| Popularity | 0.525 | 0.142 | 0.068 |
| Markov transition | 0.577 | 0.274 | 0.197 |
| BPR (64 factors) | 0.855 | 0.634 | 0.400 |
| Combined (learning to rank) | 0.920 | 0.755 | 0.556 |

## Working together

* Pull before you start: `git pull`
* Edit only your own section, then commit and push
* Clear large outputs if the notebook gets too big (`Kernel > Restart & Clear Output`), and rerun before the final export
