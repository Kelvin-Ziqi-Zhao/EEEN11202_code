from lib.my_lib import StudentMarksEEEN11202, display_student_info


def main():
    # Create instance of StudentMarksEEEN11202
    student1 = StudentMarksEEEN11202("Alex", "12345")
    student2 = StudentMarksEEEN11202("Casson", "67890")

    # Set  marks for student1
    student1.set_assignment_mark("A", 2)
    student1.set_assignment_mark("b", 5)
    student1.set_exam_mark(65)

    # Print contents
    for student in (student1, student2):
        display_student_info(student)


if __name__ == "__main__":
    main()
