test = "test string"
courses = ["math", "english", "history", "politics", "art", "physics", "chemistry"]


def list_index(target):
    course_list = enumerate(target)
    print(list(course_list))
    print(type(course_list), "\n")

    course_list2 = enumerate(target, 10)
    print(list(course_list2))


def find_index(target, search_pattern):
    """
    ▐ Find the index value of a search value.
    ▐ Assign the value of each item in target to 'value'
    ▐ check if that value matches the search pattern.
    ▐ if it does, return the enumerated index value as i.

      enumerate returns [(0,'val1'),(1,'val2'),(2,'val3')]
    """
    for i, value in enumerate(target, start=0):
        if value == search_pattern:
            return i

    return -1
