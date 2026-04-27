def calculate_overall_mark_a(student, EXAM_WEIGHTING, COURSEWORK_WEIGHTING):
    final_mark = (student["exam_mark"] * EXAM_WEIGHTING) + (
        student["coursework_mark"] * COURSEWORK_WEIGHTING
    )
    return final_mark


def calculate_overall_mark_b(student, EXAM_WEIGHTING, COURSEWORK_WEIGHTING):
    final_mark = (student["exam_mark"] * EXAM_WEIGHTING) + (
        student["coursework_mark"] * COURSEWORK_WEIGHTING
    )
    return final_mark


def check_whether_passed(marks):
    for student in marks:
        if marks[student] < 40:
            pass_status = "failed"
        elif marks[student] >= 40:
            pass_status = "passed"
        else:
            raise Exception("Something must have gone wrong!")

        print(f"{student} has {pass_status} with {marks[student]} marks.")

    return pass_status


def main():
    # Student information
    # Probably read from a file or database in practice
    student1 = {"exam_mark": 80, "coursework_mark": 75}
    student2 = {"exam_mark": 65, "coursework_mark": 70}

    # Constants for weightings
    EXAM_WEIGHTING = 0.8
    COURSEWORK_WEIGHTING = 0.2

    # Calculate final marks
    final_mark1 = calculate_overall_mark_a(
        student1, EXAM_WEIGHTING, COURSEWORK_WEIGHTING
    )
    final_mark2 = calculate_overall_mark_a(
        student2, EXAM_WEIGHTING, COURSEWORK_WEIGHTING
    )
    print(f"Final mark for student 1: {final_mark1}")
    print(f"Final mark for student 2: {final_mark2}")

    # Check whether passed or failed
    overall_marks = {"student1": final_mark1, "student2": final_mark2}
    check_whether_passed(overall_marks)


def make_sine_wave():
    import math

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


if __name__ == "__main__":
    main()
