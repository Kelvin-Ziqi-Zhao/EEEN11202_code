import matplotlib.pyplot as plt
import numpy as np
import scienceplots
import seaborn as sns


def make_example_signal(A, tau):
    """
    Make an example signal that rises exponentially
    Returns: t: time samples
    v: voltage samples
    """
    fs = 100  # sampling frequency in Hz
    t = np.arange(0, 1, 1 / fs)
    v = A * (1 - np.exp(-t / tau))
    return t, v


def get_student_marks():
    """Some example student marks for two courses"""
    marks_course_1 = np.array(
        [
            81.0,
            47.5,
            76.1,
            77.1,
            84.5,
            77.0,
            67.2,
            55.0,
            99.0,
            84.5,
            77.3,
            72.4,
            69.2,
            66.2,
            58.4,
            58.5,
            61.6,
            66.0,
            55.1,
            61.5,
            81.0,
            38.6,
            68.9,
            51.7,
            62.7,
            26.3,
            86.0,
            78.1,
            81.1,
            34.7,
            50.6,
            69.0,
            43.0,
            52.3,
            49.9,
            29.1,
            08.1,
            93.1,
            92.1,
            55.2,
            56.1,
            45.2,
            49.6,
            87.8,
            65.0,
            85.6,
            40.4,
            58.9,
            89.6,
            59.8,
            75.4,
            62.6,
            81.1,
            58.9,
            73.7,
            56.8,
            77.6,
            53.5,
            38.2,
            56.5,
            80.5,
            78.1,
            73.6,
            73.6,
            67.8,
            60.4,
            81.2,
            61.2,
            70.0,
            35.1,
            65.5,
            85.6,
            65.5,
            26.9,
            75.6,
            65.1,
            54.4,
            72.9,
            44.9,
            92.9,
            49.2,
            59.2,
            45.6,
            32.5,
            89.5,
            57.4,
            73.2,
            80.9,
            68.1,
            71.8,
            54.2,
            55.0,
            69.8,
            31.1,
            70.7,
            81.1,
            74.1,
            48.2,
            65.7,
            80.4,
        ]
    )

    marks_course_2 = np.array(
        [
            15.3,
            45.2,
            100.0,
            57.9,
            71.7,
            93.4,
            38.4,
            86.4,
            43.3,
            52.2,
            56.8,
            82.5,
            51.8,
            52.8,
            76.2,
            08.1,
            70.3,
            25.5,
            27.1,
            83.8,
            49.6,
            52.5,
            27.7,
            82.9,
            42.3,
            62.7,
            63.8,
            83.0,
            37.4,
            51.0,
            20.9,
            21.8,
            68.8,
            95.1,
            76.5,
            27.6,
            61.5,
            53.0,
            04.3,
            100.0,
            100.0,
            20.5,
            00.0,
            31.6,
            12.6,
            48.1,
            44.0,
            11.6,
            45.1,
            12.1,
            82.9,
            48.7,
            73.7,
            35.2,
            58.7,
            32.7,
            09.7,
            32.1,
            52.0,
            69.0,
            72.2,
            91.4,
            72.3,
            57.6,
            41.0,
            82.6,
            43.5,
            40.2,
            11.6,
            32.9,
            41.0,
            76.6,
            74.6,
            49.9,
            60.7,
            29.0,
            48.3,
            58.8,
            46.0,
            40.4,
            49.0,
            02.5,
            77.6,
            86.8,
            75.3,
            00.0,
            89.0,
            75.9,
            60.3,
            90.2,
            88.8,
            03.0,
            38.0,
            43.0,
            59.3,
            30.8,
            96.0,
            42.5,
            57.8,
            74.9,
        ]
    )

    return marks_course_1, marks_course_2


if __name__ == "__main__":
    # Set style defaults
    fsize = 12
    """plt.rcParams.update(
        {
            "axes.labelsize": fsize,
            "font.family": "sans-serif",
            "font.size": fsize,
            "figure.constrained_layout.use": True,
            "figure.dpi": 600,
            "figure.figsize": [3.5, 2.16],  # ieee single column is 3.5 inches wide
            "legend.fontsize": fsize,
            "pdf.fonttype": 42,  # for vector fonts in plots
            "ps.fonttype": 42,  # for vector fonts in plots
            "text.usetex": False,
            "xtick.labelsize": fsize - 2,
            "ytick.labelsize": fsize - 2,
        }
    )"""
    plt.close("all")  # close any open figures

    # Make first line
    t, v = make_example_signal(A=5, tau=0.2)

    # Plot first line
    fig0, ax0 = plt.subplots()  # make a new figure, no. 0
    ax0.plot(t, v)
    ax0.set(xlabel="Time [s]")
    ax0.set(ylabel="Voltage [V]")
    ax0.set(xlim=(0, 1))  # set the default zoom
    ax0.set(ylim=(0, 5.2))

    t1, v1 = make_example_signal(A=5, tau=0.1)
    ax0.plot(t1, v1, linestyle="--")
    ax0.legend([r"$\tau$ = 0.2 s", r"$\tau$ = 0.1 s"])

    # Put this at the end of the code - further examples below should be above this
    with plt.style.context("science", "ieee"):
        fig0.savefig("signal.png", dpi=300, bbox_inches="tight")
    print("hello")
