def display_report(name, reg_no, attendance, assignment,
                   internal, study_hours, average_marks,
                   performance, prediction):

    print("\n" + "=" * 55)
    print("          STUDENT PERFORMANCE REPORT")
    print("=" * 55)

    print("Student Name       :", name)
    print("Registration No.   :", reg_no)
    print("Attendance         :", attendance, "%")
    print("Assignment Marks   :", assignment)
    print("Internal Marks     :", internal)
    print("Average Marks      :", round(average_marks, 2))
    print("Study Hours/Day    :", study_hours)
    print("Performance Level  :", performance)
    print("Prediction         :", prediction)

    print("=" * 55)
    print("       ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 55)