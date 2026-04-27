import pytest

from src.lab_part2 import *

# Constants for weightings
EXAM_WEIGHTING = 0.8
COURSEWORK_WEIGHTING = 0.2


def test_function_a():
    student1 = {"exam_mark": 65, "coursework_mark": 34}
    correct_mark1 = 58.8
    mark1 = calculate_overall_mark_a(student1, EXAM_WEIGHTING, COURSEWORK_WEIGHTING)
    assert mark1 == correct_mark1

    student2 = {"exam_mark": 15, "coursework_mark": 70}
    correct_mark2 = 26.0
    mark2 = calculate_overall_mark_a(student2, EXAM_WEIGHTING, COURSEWORK_WEIGHTING)
    assert mark2 == correct_mark2

    student3 = {"exam_mark": 80, "coursework_mark": 90}
    correct_mark3 = 82.0
    mark3 = calculate_overall_mark_a(student3, EXAM_WEIGHTING, COURSEWORK_WEIGHTING)
    assert mark3 == correct_mark3


def test_function_b():
    student1 = {"exam_mark": 65, "coursework_mark": 34}
    correct_mark1 = 58.8
    mark1 = calculate_overall_mark_b(student1, EXAM_WEIGHTING, COURSEWORK_WEIGHTING)
    assert mark1 == correct_mark1

    student2 = {"exam_mark": 15, "coursework_mark": 70}
    correct_mark2 = 26.0
    mark2 = calculate_overall_mark_b(student2, EXAM_WEIGHTING, COURSEWORK_WEIGHTING)
    assert mark2 == correct_mark2

    student3 = {"exam_mark": 80, "coursework_mark": 90}
    correct_mark3 = 82.0
    mark3 = calculate_overall_mark_b(student3, EXAM_WEIGHTING, COURSEWORK_WEIGHTING)
    assert mark3 == correct_mark3


def test_check_whether_passed():
    for i in range(0, 101):
        # Simulated mark
        marks = {"student": i}

        # Expected pass status
        if i < 40:
            expected_status = "failed"
        else:
            expected_status = "passed"

        # Run function
        pass_status = check_whether_passed(marks)

        # Run check
        assert pass_status == expected_status


import math


def test_make_sine_wave():
    t, v_out = make_sine_wave()

    # Check first few values
    expected_v_out = [0.0, 0.587785, 0.9510565]
    for i in range(len(expected_v_out)):
        assert math.isclose(v_out[i], expected_v_out[i], rel_tol=1e-5)
