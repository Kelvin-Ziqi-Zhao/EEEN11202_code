import pathlib
from os.path import join as pjoin

import numpy as np
import polars as pl

# Set file to load
script_folder = pathlib.Path(__file__).parent.resolve()
data_dir_from_script_folder = pjoin(script_folder, "../", "data")
xls_fname = pjoin(data_dir_from_script_folder, "choices.xlsx")

# Load data
df = pl.read_excel(xls_fname)

# What did student mchabc80 select as their 3rd choice?
stu = df.filter(pl.col("Username") == "mchabc80").select(pl.col("Answer 3"))
print(stu)

# What was the most popular first choice project?
mode1 = df.select(pl.col("Answer 1").mode().first())
print(mode1)

# What was the most popular first choice project for students on the MEng course?
df2 = df.filter(pl.col("Course").str.starts_with("M"))
mode2 = df2.select(pl.col("Answer 5").mode().first())
print(mode2)

# What was the most popular overall project (i.e. counting all choices)?
df3 = df.unpivot(
    on=["Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"], index="Username"
)
mode3 = df3.select(pl.col("value").mode().first())
print(mode3)

# If the minimum project ID is 1 and the maximum is 208, which projects were not selected by any student?
unique_choices = df3.select(pl.col("value")).unique().to_numpy()
all_choices = np.arange(1, 209)
print(all_choices[~np.isin(all_choices, unique_choices)])

# How many (and which) submitted the form more than once?
df4 = df.filter(df.is_duplicated())
print(df4.select(pl.col("Username")).unique())
print(df4.select(pl.col("Username")).unique().height)
