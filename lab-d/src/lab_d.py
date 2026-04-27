"""
Calculate the output voltage magnitude and phase of an RC low-pass filter
"""

import cmath
import math


def calculate_circuit_output(f):
    """
    Calculate the output voltage magnitude and phase of an RC low-pass filter
    given an input frequency f in Hz.
    Returns: vout_mag: output voltage magnitude in Volts
             vout_phase: output voltage phase in radians
    """

    # Calculate input
    w = 2 * math.pi * f  # rad/s
    a = 5  # input amplitude in Volts
    v_in = a * cmath.exp(0j)  # phasor representation. 0 degree signal

    # Define the circuit
    z1 = 1000  # Ohms
    c = 1e-9  # Farads
    z2 = 1 / (1j * w * c)
    v_out = (z2 * v_in) / (z1 + z2)  # Volts

    # Calculate magnitude and phase
    vout_mag = abs(v_out)
    vout_mag_db = 20 * math.log10(
        vout_mag / a
    )  # remember to divide by the input amplitude
    vout_phase = cmath.phase(v_out)

    return vout_mag_db, vout_phase


def display_results(f, vout_mag, vout_phase):
    """Display the output voltage magnitude and phase using an f string"""
    print(
        f"Frequency: {f:.1f} Hz, Magnitude: {vout_mag:.3f} dB, Phase: {vout_phase:.3f} radians"
    )


def load_frequencies():
    """Load frequencies from a file and return them"""

    # Load data from file
    filename = "frequencies.txt"
    with open(filename, "r") as f:
        data = f.read().splitlines()

    # Extract number part of each string
    num = []  # preallocate
    for i in range(len(data)):
        num.append([int(x) for x in data[i].split() if x.isdigit()][0])

    # Put into output format - this is the part that needs changing for the optional challenge
    start = num[0]
    stop = num[1]
    step = num[2]

    return start, stop, step


if __name__ == "__main__":
    start, stop, step = load_frequencies()
    for f in range(start, stop + 1, step):
        vout_mag, vout_phase = calculate_circuit_output(f)
        display_results(f, vout_mag, vout_phase)
