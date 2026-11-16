# Sports Performance Analyzer

A Python command-line application that loads players' match scores from a CSV file, cleans invalid or missing records, computes individual and overall statistical metrics, identifies the top performer, and visualizes score trends using Matplotlib.

---

## Features

* **Automated Data Cleaning:** Reads `scores.csv` using Pandas and validates every row, skipping entries with missing fields, non-numeric scores, negative scores, or invalid match numbers.
* **Player-Level Analytics:** Uses `groupby()` to calculate each player's average score, best score, and total score, and identifies the top performer.
* **Overall Statistical Summary:** Uses NumPy to compute population mean, median, standard deviation (`np.std` default), maximum score (with player and match details), minimum score, and match-wise averages.
* **Data Visualization:** Generates and exports two labeled Matplotlib charts:
  * `score_trend.png` — Line chart showing average score progression across matches.
  * `player_average.png` — Bar chart comparing average scores across players.
* **Built-in Test Case Loader:** Includes a menu option to generate and test all four validation scenarios directly from the console.

---

## Tech Stack

* **Language:** Python 3
* **Libraries:** `pandas`, `numpy`, `matplotlib`, `csv`

---

## Project Structure

```text
sports-performance-analyzer/
├── sports_analyzer.py    # Main application script
├── scores.csv            # Generated/input dataset (Player, Match, Score)
├── score_trend.png       # Generated line chart of match-wise score trends
├── player_average.png    # Generated bar chart of player average scores
└── README.md             # Project documentation
