def build_roster(registrations):
    """
    Given a list of (student, course) pairs, return a dictionary where each
    course maps to a sorted list of unique students registered for that course.

    Example:
    [("s1", "CS101"), ("s2", "CS101")] -> {"CS101": ["s1", "s2"]}
    """

    roster = {}

    for student, course in registrations:
        if course not in roster:
            roster[course] = []
        if student not in roster[course]:
            roster[course].append(student)

    # Sort each course's student list
    for course in roster:
        roster[course].sort()

    return roster


if __name__ == "__main__":
    # Optional test
    data = [("s1", "CS101"), ("s2", "CS101"), ("s1", "MATH200"), ("s2", "CS101")]
    print(build_roster(data))
