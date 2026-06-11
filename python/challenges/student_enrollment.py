courses_list = [
    "Python",
    "Databases",
]

enrollments_list = [
    ["Alice", "Bob"],
    ["Bob", "Cara"],
]

def build_student_enrollment_index(courses, enrollments) -> dict[str, dict[str, list, str, int]]:
    enrolled_students = {}
    index = 0

    for enrollment in enrollments:
        for student in enrollment:
            if not student:
                continue
            if student not in enrolled_students:
                enrolled_students[student] = {}
                enrolled_students[student]["courses"] = set([courses[index]])
            else:
                enrolled_students[student]["courses"].add(courses[index])
                
        index += 1

    for student in enrolled_students:
        enrolled_students[student]["courses"] = sorted(list(enrolled_students[student]["courses"]))
        enrolled_students[student]["count"] = len(enrolled_students[student]["courses"])

    return enrolled_students

print(build_student_enrollment_index(courses_list, enrollments_list))
