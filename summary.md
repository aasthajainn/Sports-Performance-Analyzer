<img width="958" height="805" alt="GRAPH-2" src="https://github.com/user-attachments/assets/c08e4d56-9d61-4695-8ea6-eecb833b2db1" />
# Project Summary: Sports Performance Analyzer

## Overview
The **Sports Performance Analyzer** is a Python 3 console-based data analysis application designed to process, clean, evaluate, and visualize players' match scores stored in a CSV dataset (`scores.csv`). It fulfills the requirements of **Project No. 20** for the Bachelor of Technology (Computer Science and Engineering) curriculum at Rungta International Skills University.

---

## Problem Statement & Objectives
Raw sports performance records often contain missing fields, malformed text, or invalid numerical values. The objective of this project is to build an automated pipeline that:
1. Ingests match score records (`Player`, `Match`, `Score`) using **Pandas**.
2. Filters out corrupted or invalid entries while reporting row-level skip diagnostics.
3. Computes individual player metrics (`groupby()`) and overall statistical summaries (**NumPy**).
4. Visualizes match-wise progression and player comparisons using **Matplotlib**.

---

## System Architecture & Workflow

```text
[scores.csv] ──► Data Cleaning (Pandas) ──► Statistical Engine (NumPy & GroupBy) ──► Console Report & Charts (Matplotlib)
[GRAPHS.pdf](https://github.com/user-attachments/files/34952467/GRAPHS.pdf)
[TEST CASES.pdf](https://github.com/user-attachments/files/34952459/TEST.CASES.pdf)

