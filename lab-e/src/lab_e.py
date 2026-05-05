import pathlib
from os.path import join as pjoin

import numpy as np

# import plotly.express as px
import scipy.io as sio
from scipy import signal
from scipy.optimize import curve_fit


def load_signal_from_matfile():
    # Get the path to the .mat file
    # This uses pathlib to automatically get the folder where this script is located and navigates from there
    script_folder = pathlib.Path(__file__).parent.resolve()
    data_dir = pjoin(script_folder, "../", "data")
    mat_fname = pjoin(data_dir, "lab_e.mat")

    # Load data
    data = sio.loadmat(mat_fname, variable_names=["t", "v"])
    return data["t"].squeeze(), data["v"].squeeze()


def fit_func(xdata, ydata):
    # reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

    def func(x, a, b, c):
        return a * (1 - np.exp(-x / b)) + c

    popt, pcov = curve_fit(func, xdata, ydata)
    return popt


if __name__ == "__main__":
    t, v = load_signal_from_matfile()
    result = fit_func(t, v)
    # Add code here

    with open("tau.txt", "w") as f:
        f.write(str(result[1]))
