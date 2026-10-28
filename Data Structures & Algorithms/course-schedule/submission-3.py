class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Dictionary comprehension
        preReqMap = {courseNumber: [] for courseNumber in range(numCourses)}
        for course, prereq in prerequisites:
            preReqMap[course].append(prereq)
        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False
            if preReqMap[course] == []:
                return True
            
            visitSet.add(course)
            for prereq in preReqMap[course]:
                if not dfs(prereq): return False
            # this course is valid
            visitSet.remove(course)
            preReqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True
        
        