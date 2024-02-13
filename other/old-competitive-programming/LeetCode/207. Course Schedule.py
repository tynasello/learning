
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # {course: [prereq courses]}
        prereqsMap = defaultdict(lambda: [])
        coursesVisitedInCurrentDfs = set()

        for prereq in prerequisites:
            prereqsMap[prereq[0]].append(prereq[1])

        # dfs

        def canEnrollInClass(currCourse):
            if currCourse in coursesVisitedInCurrentDfs:
                # cycle detected - can't continue
                return False

            if prereqsMap[currCourse] == []:
                # no prereqs
                return True

            coursesVisitedInCurrentDfs.add(currCourse)

            for prereq in prereqsMap[currCourse]:
                if not canEnrollInClass(prereq):
                    return False

            prereqsMap[currCourse] = []
            coursesVisitedInCurrentDfs.remove(currCourse)

            return True

        for course in range(numCourses):
            if not canEnrollInClass(course):
                return False

        return True
