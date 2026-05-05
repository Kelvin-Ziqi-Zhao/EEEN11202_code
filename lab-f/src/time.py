from datetime import time, timedelta

import numpy as np
import plotly.express as px
import polars as pl

# %% This is us making a simulated time series.
# Could imagine loading this in from a file instead, or downloading from the Internet

# Make sine waves in numpy
fs = 1000  # sampling frequency in Hz
f = 25  # Frequency of the sine wave
start = 0  # start time in seconds
stop = 10  # stop time in seconds
t = np.arange(start, stop + 1 / fs, 1 / fs)
v = np.sin(2 * np.pi * f * t)
v_noise = v + np.random.normal(0, 0.5, t.shape)

# Make time base
t = pl.time_range(
    start=time(second=start),
    end=time(second=stop),
    interval=timedelta(seconds=1 / fs),
    eager=True,
).alias("time")

# Make dataframe
df = pl.DataFrame([t, pl.Series("clean", v), pl.Series("noisy", v_noise)])
print(df)

# Plot
fig = px.line(df, x="time", y="clean").update_layout(yaxis_title="Voltage [V]")
fig.add_scatter(x=df["time"], y=df["noisy"], mode="lines", line=dict(dash="dash"))
fig.data[1].showlegend = False
fig.show()

df = df.with_columns(pl.col("noisy").rolling_mean(window_size=11).alias("filtered"))

# Plot
fig.add_scatter(x=df["time"], y=df["filtered"], mode="lines", line=dict(dash="dot"))
fig.data[2].showlegend = False
fig.show()
