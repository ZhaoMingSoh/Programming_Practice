from functools import cmp_to_key

def scheduleCourse(courses: list[list[int]]) -> int:
    # Sort the courses according to the time frame or the second elem
    def compare(o1,o2):
        # If the time frame is the same
        if o1[1] == o2[1]:
            # sort based on the first element (courses's duration)
			# 	 - If array1[0] < array2[0] -> negative val meaning array1 val should appear before array2 val
			# 	 - if array1[0] > array2[0] -> postive val meaning array1 val should appear after array2 val
            return o1[0] - o2[0]
        # If the time frame is not the same
        else:
            # sort based on the time frame
            return o1[1] - o2[1]

    #  Sort the added duration of a course in descending order
    courses.sort(key=cmp_to_key(compare))
    q = []

    time = 0
    for course in courses:
        # If the course can be completed within the given time frame
        if course[0] + time <= course[1]:
            time += course[0]
            q.append(course[0])
            q.sort(reverse=True)
        #  If the course cannot be completed within the given time frame
        else:
            # make sure the priority queue is not empty, if yes, then do nothing
            if len(q) != 0:
                #  check if current course's duration is smaller than the highest duration course in the priority queue
                if q[0] > course[0]:
                    #  remove it and replace it with the current course
                    time -= q.pop(0)
                    time += course[0]
                    q.append(course[0])
                    q.sort(reverse=True)

    return len(q)

if __name__ == "__main__":
    courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    print(f"The maximum number of courses that you can take from {courses} is {scheduleCourse(courses)}")