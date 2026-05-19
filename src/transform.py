from pathlib import Path
import sys

import pandas as pd


def add_date(input_path: Path) -> None:
    output_path = Path("data/transformed/events.csv")

    df = pd.read_csv(input_path)

    df["date"] = pd.to_datetime(
        df["timestamp"]
    ).dt.strftime("%Y-%m-%d")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    input_csv = Path(sys.argv[1])

    add_date(input_csv)