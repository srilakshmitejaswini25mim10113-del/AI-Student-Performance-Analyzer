def predict_performance(study_hours, attendance, average_marks):

    if study_hours >= 4 and attendance >= 75 and average_marks >= 70:
        prediction = "High potential for strong academic performance"
    elif study_hours >= 2 and attendance >= 60 and average_marks >= 50:
        prediction = "Moderate potential for academic performance"
    else:
        
        prediction = "Student may need additional academic support"

    return prediction