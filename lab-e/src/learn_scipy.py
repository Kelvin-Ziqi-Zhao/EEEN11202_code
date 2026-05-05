import pathlib
from os.path import join as pjoin

import numpy as np
import plotly.express as px
import scipy.io as sio
from scipy import signal


def load_signal_from_matfile():
    # Get the path to the .mat file
    # This uses pathlib to automatically get the folder where this script is located and navigates from there
    script_folder = pathlib.Path(__file__).parent.resolve()
    data_dir = pjoin(script_folder, "../", "data")
    mat_fname = pjoin(data_dir, "lab_e.mat")

    # Load data
    data = sio.loadmat(mat_fname, variable_names=["t", "v"])
    return data["t"].squeeze(), data["v"].squeeze()


if __name__ == "__main__":
    t, v = load_signal_from_matfile()

    fig = px.line(x=t, y=v, labels={"x": "Time [s]", "y": "Voltage [V]"})

    script_dir = pathlib.Path(__file__).parent.resolve()
    output_path = script_dir / "sine_plot.html"

    fig.write_html(
        output_path,
        include_plotlyjs="directory",
        auto_open=False,
    )

    print(f"Saved plot to: {output_path}")
