class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # For every course, we want to map it to an empty list and will contain courses that it's a prequisite for
        preReqMap = { i: [] for i in range(numCourses)}
        # Then we updaqte the map with each course having a list of courses that it's a prereq for
        for course,prereq in prerequisites:
            preReqMap[course].append(prereq)
        # This contains all of the courses that it's seen so far
        visitSet = set()

        def dfs(course):
            # If the new course that we see is a course that we've already seen before, FALSE
            if course in visitSet:
                return False
            # The course that we see is a final course, it is not a prerequisite for any other class
            if preReqMap[course] == []:
                return True
            # We can add the new course that we see to a visited set list 
            visitSet.add(course)

            # We check for the base cases (visited already, empty list), keep adding all of the courses to the set of visited courses, and if we ever reach a false case then it's false, 
            for prereq in preReqMap[course]:
                if not dfs(prereq): return False
            visitSet.remove(course)
            preReqMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True
        
        