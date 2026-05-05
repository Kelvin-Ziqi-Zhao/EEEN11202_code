import pathlib
from os.path import join as pjoin

import numpy as np
import polars as pl


def load_data():
    # Get the path to the .csv file
    # This uses pathlib to automatically get the folder where this script is located and navigates from there
    script_folder = pathlib.Path(__file__).parent.resolve()
    data_dir = pjoin(script_folder, "../", "data")
    csv_fname = pjoin(data_dir, "lab_f.csv")

    # Load data
    df = pl.read_csv(csv_fname)
    return df
    # Add code here


if __name__ == "__main__":
    # Add code here
    # The average mark for the overall unit (combining the assignments and exam) to 1 decimal place.
    df = load_data()
    assignment_cols = df.columns[1:21]

    overall_mark = df.select(
        (
            ((pl.sum_horizontal(*assignment_cols) + pl.col("Exam mark")) / 2)
            .mean()
            .round(1)
        )
    ).item()

    # The median exam mark for students whose name starts with the same letter as the first letter in your University of Manchester email address.
    x = df.filter(pl.col("Student name").str.starts_with("z"))
    median = x.select(pl.col("Exam mark").median().round(1)).item()

    # The name of the student with the highest exam mark to 1 decimal place.
    max = (
        df.sort("Exam mark", descending=True)
        .select(pl.col("Student name"))
        .head(1)
        .item()
    )

    # The assignment which students did the best in, on average.
    arr = df.select(assignment_cols).to_numpy()

    means = np.mean(arr, axis=0)
    best_idx = np.argmax(means)

    best_assignment = assignment_cols[best_idx]

    import json

    result = {
        "Overall mark": overall_mark,
        "First letter mark": median,
        "Best exam": max,
        "Best assignment": best_assignment,
    }

    print(json.dumps(result, indent=2))
