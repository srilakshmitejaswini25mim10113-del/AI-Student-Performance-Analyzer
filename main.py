from student_details import get_student_details
from performance_analysis import analyze_performance
from prediction import predict_performance
from report import display_report
from utils import display_title


def main():

    display_title()

    # Module 1: Student Details
    name, reg_no, attendance, assignment, internal, study_hours = \
        get_student_details()

    # Module 2: Performance Analysis
    print("\n--- PERFORMANCE ANALYSIS ---")

    average_marks, performance = analyze_performance(
        attendance, assignment, internal
    )

    # Module 3: Performance Prediction
    print("\n--- PERFORMANCE PREDICTION ---")

    prediction = predict_performance(
        study_hours, attendance, average_marks
    )

    # Module 4: Report Generation
    display_report(
        name,
        reg_no,
        attendance,
        assignment,
        internal,
        study_hours,
        average_marks,
        performance,
        prediction
    )


if __name__ == "__main__":
    main()