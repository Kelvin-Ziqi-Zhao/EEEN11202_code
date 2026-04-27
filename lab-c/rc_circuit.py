# Potential divider where z2 is a capacitor
import cmath
import math


def calculate(f_input):
    f = f_input  # Hz
    w = 2 * math.pi * f  # rad/s

    a = 5  # input amplitude in Volts
    v_in = a * cmath.exp(0j)  # phasor representation. 0 degree signal

    z1 = 1e3  # Ohms
    c = 1e-9  # Farads
    z2 = 1 / (1j * w * c)

    v_out = (z2 * v_in) / (z1 + z2)  # Volts

    vout_mag = abs(v_out)
    vout_phase = cmath.phase(v_out)

    vout_mag_db = 20 * math.log10(vout_mag / a)

    return vout_mag_db, vout_phase


def display_result(vout_mag, vout_phase):
    print(f"vout_mag: {vout_mag}")
    print(f"vout_phase: {vout_phase}")


if __name__ == "__main__":
    f = 16000
    vout_mag, vout_phase = calculate(f)
    display_result(vout_mag, vout_phase)
