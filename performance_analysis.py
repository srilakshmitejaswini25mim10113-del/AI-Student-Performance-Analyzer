def analyze_performance(attendance, assignment, internal):
    average_marks = (assignment + internal) / 2

    if attendance >= 75 and average_marks >= 75:
        performance = "Excellent"
    elif attendance >= 65 and average_marks >= 60:
        performance = "Good"
    elif attendance >= 50 and average_marks >= 40:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    return average_marks, performance