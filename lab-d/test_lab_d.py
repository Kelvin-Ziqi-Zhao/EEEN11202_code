import pytest

# comment
from src.lab_d import *


def test_calculate_circuit_output():
    f = 1000000
    [vout_mag_db, vout_phase] = calculate_circuit_output(f)

    assert math.isclose(vout_mag_db, -16.072, rel_tol=1e-4)
    assert math.isclose(vout_phase, -1.413, rel_tol=1e-4)


def test_display_results(capsys):
    f = 12345
    vout_mag = 12.3456
    vout_phase = 123.4567
    display_results(f, vout_mag, vout_phase)

    captured = capsys.readouterr()

    # Expected output
    expected = "Frequency: 12345.0 Hz, Magnitude: 12.346 dB, Phase: 123.457 radians\n"

    # print(captured)
    # print(expected)

    assert captured.out == expected


def test_load_frequencies(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    with open("frequencies.txt", "w") as f:
        f.write("start frequency: 1000000\n")
        f.write("stop frequency: 100000000\n")
        f.write("steps: 10000000\n")

    captured = load_frequencies()

    assert captured[0] == 1000000
    assert captured[1] == 100000000
    assert captured[2] == 10000000
