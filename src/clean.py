from pathlib import Path
import sys

import pandas as pd


def clean_events(input_path: Path) -> None:
    output_path = Path("data/clean/events.csv")

    # read raw data
    df = pd.read_csv(input_path)

    # remove missing rows
    df = df.dropna()

    # remove invalid event type
    df = df[df["event_type"].isin(["click", "login", "scroll", "view", "purchase"])]

    # remove non-positive durations
    df = df[df["duration_seconds"] > 0]

    # normalize timestamps to ISO 8601
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        format="mixed",
    ).dt.strftime("%Y-%m-%dT%H:%M:%S")

    # ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # save cleaned data
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    input_csv = Path(sys.argv[1])

    clean_events(input_csv)