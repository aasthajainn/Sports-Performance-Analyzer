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

<img width="561" height="523" alt="TEST CASE-1" src="https://github.com/user-attachments/assets/7f592604-c30b-40db-bc18-2144cc3d7a80" />
<img width="766" height="235" alt="TEST CASE-2" src="https://github.com/user-attachments/assets/2049ca17-3926-4cc4-b765-3875d0401892" />
<img width="627" height="321" alt="TEST CASE-3" src="https://github.com/user-attachments/assets/ddf028fb-930f-4a7b-956a-4aef3e945541" />
<img width="876" height="559" alt="TEST CASE-4" src="https://github.com/user-attachments/assets/f473b505-713c-434c-920c-c7ca4d01b8d9" />
<img width="952" height="807" alt="GRAPH-1" src="https://github.com/user-attachments/assets/33283b1f-4609-439b-b28c-6ec814d45d81" />
<img width="958" height="805" alt="GRAPH-2" src="https://github.com/user-attachments/assets/7a779caa-c781-4ca4-9f11-496dd9d806ad" />
