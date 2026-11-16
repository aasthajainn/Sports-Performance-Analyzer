import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


# ---------------- Test case data (from the problem statement) ----------------
test_cases = {
    "1": [["Aman", 1, 40], ["Aman", 2, 60], ["Riya", 1, 30], ["Riya", 2, 50]],   # Normal input
    "2": [["Karan", 1, 25]],                                                     # Boundary / minimum input
    "3": [["Aman", 1, "abc"], ["Riya", 1, -10]],                                 # Invalid input
    "4": [["Aman", 1, 40], ["Aman", 2, 60], ["Riya", 1, 30], ["Riya", 2, 50]],   # Different valid scenario
}


def create_csv(case):
    """Write scores.csv for the chosen test case."""
    with open("scores.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Match", "Score"])
        for row in test_cases[case]:
            writer.writerow(row)


def load_data():
    """Load scores.csv with Pandas and clean invalid / missing scores."""
    raw = pd.read_csv("scores.csv", dtype=str, keep_default_na=False)
    clean_rows = []

    for i in range(len(raw)):
        row_no = i + 1
        player = raw.loc[i, "Player"].strip()
        match = raw.loc[i, "Match"].strip()
        score = raw.loc[i, "Score"].strip()

        if player == "" or score == "":
            print("Row", row_no, "skipped: missing data.")
            continue

        try:
            score_value = float(score)
        except ValueError:
            print("Row", row_no, "skipped: invalid Score '" + score + "'.")
            continue

        if score_value < 0:
            print("Row", row_no, "skipped: Score cannot be negative.")
            continue

        try:
            match_value = int(match)
        except ValueError:
            print("Row", row_no, "skipped: invalid Match.")
            continue

        clean_rows.append([player, match_value, score_value])

    return pd.DataFrame(clean_rows, columns=["Player", "Match", "Score"])


# Start with Test Case 1 loaded
create_csv("1")
df = load_data()


while True:
    print("\n====== SPORTS PERFORMANCE ANALYZER ======")
    print("1. Player stats")
    print("2. Statistics and trend")
    print("3. Load a test case (1-4)")
    print("4. Exit")

    choice = input("Menu option: ")

    if choice == "1":
        if df.empty:
            print("No valid data to analyse.")
            continue

        # groupby() to get average, best score and total of each player
        stats = df.groupby("Player")["Score"].agg(["mean", "max", "sum"])

        for player in stats.index:
            avg = stats.loc[player, "mean"]
            best = stats.loc[player, "max"]
            total = stats.loc[player, "sum"]
            if len(df) == 1:
                std = np.std(df["Score"])
                print(f"{player}: Avg {avg:.2f} | Best {best:g} | Std Dev: {std:.2f}")
            else:
                print(f"{player}: Avg {avg:.2f} | Best {best:g} | Total {total:g}")

        top = stats["mean"].idxmax()
        if len(stats) == 1:
            print("Top performer:", top)
        else:
            print(f"Top performer: {top} (Avg {stats['mean'].max():.2f})")

    elif choice == "2":
        if df.empty:
            print("No valid data to analyse.")
            continue

        scores = df["Score"].to_numpy()
        max_val = np.max(scores)
        max_row = df.loc[df["Score"].idxmax()]
        max_player = max_row["Player"]
        max_match = max_row["Match"]

        print(
            f"Mean: {np.mean(scores):.2f} | Median: {np.median(scores):.2f} | "
            f"Std Dev: {np.std(scores):.2f} | Max: {max_val:g} ({max_player}, Match {max_match})"
        )
        print(f"Min: {np.min(scores):g}")

        match_avg = df.groupby("Match")["Score"].mean()
        text = "Match-wise average: "
        for m in match_avg.index:
            text += f"Match {m}: {match_avg[m]:.2f} | "
        print(text[:-3])

        # 1. Line chart - score trend
        plt.figure()
        plt.plot(match_avg.index, match_avg.values, marker="o")
        plt.xticks(match_avg.index)
        plt.xlabel("Match")
        plt.ylabel("Average Score")
        plt.title("Score Trend")
        plt.savefig("score_trend.png")
        print("Line chart 'Score Trend' displayed")

        # 2. Bar chart - average score of each player
        plt.figure()
        avg_player = df.groupby("Player")["Score"].mean()
        plt.bar(avg_player.index, avg_player.values)
        plt.xlabel("Player")
        plt.ylabel("Average Score")
        plt.title("Average Score by Player")
        plt.savefig("player_average.png")
        print("Bar chart 'Average Score by Player' displayed")

        plt.show()

    elif choice == "3":
        case = input("Enter test case number (1-4): ").strip()
        if case in test_cases:
            create_csv(case)
            print("scores.csv created for Test Case", case)
            df = load_data()
            if case in ("1", "2", "3"):
                print("Now choose menu option 1 (Player stats).")
            else:
                print("Now choose menu option 2 (Statistics and trend).")
        else:
            print("Invalid test case number")

    elif choice == "4":
        print("Program exited successfully")
        break

    else:
        print("Invalid choice")