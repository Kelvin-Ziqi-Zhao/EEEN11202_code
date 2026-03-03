import math

import plotly.express as px


def make_sine_wave():
    """
    Make a sine wave signal
    TO DO: replace range with a numpy array

    Returns: t: time samples
    v_out: voltage samples
    """
    sample_start = 0
    sample_stop = 100
    A = 1  # Volts
    f = 0.1  # Hz
    t = range(sample_start, sample_stop)  # interpret as representing 1 s, 2 s, 3 s, ...
    v_out = [A * math.sin(2 * math.pi * f * time) for time in t]
    return t, v_out


def plot_sine_wave(t, v_out):
    """Plot a sine wave using plotly and label the axes"""
    fig = px.line(x=t, y=v_out, labels={"x": "Time [s]", "y": "Voltage [V]"})
    fig.show()


if __name__ == "__main__":
    t, v_out = make_sine_wave()
    plot_sine_wave(t, v_out)
