import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from pathlib import Path

    return Path, pd, plt


@app.cell
def _(Path, pd, plt):
    csv_path = Path("../data/features/events.csv")

    df = pd.read_csv(csv_path)

    plt.hist(df['duration_minutes'])

    plt.xlabel("Minutes")
    plt.ylabel("Frequency")
    plt.title("Duration of Events")

    plt.show()
    return


if __name__ == "__main__":
    app.run()
