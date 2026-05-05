import pathlib
from os.path import join as pjoin

import polars as pl

# Set file to load
script_folder = pathlib.Path(__file__).parent.resolve()
data_dir_from_script_folder = pjoin(script_folder, "../", "data")
xls_fname = pjoin(data_dir_from_script_folder, "marks.xlsx")

# Load data
df = pl.read_excel(xls_fname)
