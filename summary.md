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
[scores.csv] ──► Data Cleaning (Pandas) ──► Statistical Engine (NumPy & GroupBy) ──► Console Report & Charts (Matplotlib)<img width="958" height="805" alt="GRAPH-2" src="https://github.com/user-attachments/assets/da0c7d79-1721-4f6a-90c0-db2edd56a6b8" />
<img width="952" height="807" alt="GRAPH-1" src="https://github.com/user-attachments/assets/e35fcf74-60f8-4443-acde-71065471e7cc" />
<img width="876" height="559" alt="TEST CASE-4" src="https://github.com/user-attachments/assets/879839c5-4816-4e18-8f99-eaed3ad87f4b" />
<img width="627" height="321" alt="TEST CASE-3" src="https://github.com/user-attachments/assets/6fe08c2c-81ce-4766-b652-85d7623ea9d9" />
<img width="766" height="235" alt="TEST CASE-2" src="https://github.com/user-attachments/assets/5d1af3aa-2e50-4c27-85db-a05bcd2672ac" />
<img width="561" height="523" alt="TEST CASE-1" src="https://github.com/user-attachments/assets/75780365-41f8-4f58-91b1-249358f39284" />
