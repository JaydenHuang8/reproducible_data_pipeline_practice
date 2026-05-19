import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from pathlib import Path

    return Path, pd


@app.cell
def _(Path, pd):
    csv_path = Path("../data/raw/events.csv")

    df = pd.read_csv(csv_path)

    #
    df = df.dropna()

    # remove invalid event type
    df = df[df["event_type"] != "unknown"]

    # rm non positive duration
    df = df[df["duration_seconds"] > 0]

    # convert to ISO 8601 string format
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed").dt.strftime("%Y-%m-%dT%H:%M:%S")

    #Transforming
    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

    df
    return


@app.cell
def _(Path, pd):
    df2 = pd.read_csv(Path("../data/transformed/events.csv"))

    df2["duration_minutes"] = df2["duration_seconds"] / 60

    df2["weekday"] = pd.to_datetime(df2["date"]).dt.day_name()

    df2
    return


if __name__ == "__main__":
    app.run()
