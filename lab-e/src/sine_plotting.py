import math

import numpy as np
import plotly.express as px


def make_sine_wave(A, f, start, stop):
    """
    Make a sine wave signal
    TO DO: replace range with a numpy array

    Returns: t: time samples
    v_out: voltage samples
    """
    t = range(start, stop)  # interpret as representing 1 s, 2 s, 3 s, ...
    v_out = [A * math.sin(2 * math.pi * f * time) for time in t]
    return t, v_out


def make_sine_wave_numpy(A, f, start, stop):
    """
    Make a sine wave signal
    Returns: t: time samples
    v_out: voltage samples
    """
    step = 1 / (f * 30)
    t = np.arange(start, stop, step)  # interpret as representing 1 s, 2 s, 3 s, ...
    v_out = A * np.sin(2 * np.pi * f * t)
    return t, v_out


def do_plots(t, v_out):
    fig = px.line(x=t, y=v_out, labels={"x": "Time [s]", "y": "Voltage [V]"})
    fig.show()


if __name__ == "__main__":
    """
    # Put plotting code below here
    # Settings for both sine waves - both need the same time base
    start = 0
    stop = 1
    fs = 500  # sampling frequency in Hz
    time = np.arange(start, stop, 1 / fs)

    # Make sine wave 1
    A1 = 1
    f1 = 10
    v1 = A1 * np.sin(2 * np.pi * f1 * time)

    # Make sine wave 2
    A2 = 0.4
    f2 = 50
    v2 = A2 * np.sin(2 * np.pi * f2 * time)

    # Make final sine wave
    vo = v1 + v2
    do_plots(time, vo)

    noise_mean = 0
    noise_std = 0.2  # standard deviation of the noise, the peak-to-peak will be about 6 times this
    noise = np.random.normal(noise_mean, noise_std, size=vo.shape)
    vo_noisy = vo + noise
    do_plots(time, vo_noisy)
    """

    start = 0
    stop = 1
    fs = 500  # sampling frequency in Hz
    ts = np.arange(start, stop, 1 / fs)
