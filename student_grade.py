student_scores={
    "hosong":80,
    "mororong":77,
    "songja":35,
    "gwang_dae":10,

}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="perfect"
    elif score>80:
        student_grades[student]="nice"
    elif score>70:
        student_grades[student]="not bad"
    else:
        student_grades[student]="bad"
print(f"result:\n{student_grades}")