def get_student_details():
    print("\n--- STUDENT DETAILS ---")

    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    attendance = float(input("Enter attendance percentage: "))
    assignment = float(input("Enter assignment marks (out of 100): "))
    internal = float(input("Enter internal marks (out of 100): "))
    study_hours = float(input("Enter average study hours per day: "))

    return name, reg_no, attendance, assignment, internal, study_hours