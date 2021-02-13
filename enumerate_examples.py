# Demonstrate how to return Index and Value information from lists using the enumerate function

courses = ["math", "english", "history", "politics", "art", "physics", "chemistry"]


def loop_index(target):
    for item in enumerate(target):
        print(item)

    print("\n")
    for count, item in enumerate(target):
        print(count, item)

    print("\n")
    for count, item in enumerate(target, 10):
        print(count, item)


loop_index(courses)

# list_index(courses)
# indexValue = find_index(courses, "history")
# print(indexValue)