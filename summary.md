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