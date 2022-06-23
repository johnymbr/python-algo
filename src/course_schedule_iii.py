import unittest
from heapq import heappush, heappop
from typing import List


# LeetCode link: https://leetcode.com/problems/course-schedule-iii/
# Time complexity for this algorithm is O(n log n) because we sort the list of courses.
# Space complexity is O(n) because we use a heap to store values.
def schedule_course(courses: List[List[int]]) -> int:
    courses.sort(key=lambda x: x[1])  # O(n log n)
    heap = []
    max_time = 0
    for time, end_time in courses:  # O(n)
        if max_time + time <= end_time:
            heappush(heap, -time)  # O(log n)
            max_time += time
        elif len(heap) > 0 and (-heap[0]) > time:
            max_time += time - (-heappop(heap))  # O(1)
            heappush(heap, -time)

    return len(heap)


class CourseScheduleIII(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, schedule_course(courses=[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))

    def test_02(self):
        self.assertEqual(1, schedule_course(courses=[[1, 2]]))

    def test_03(self):
        self.assertEqual(0, schedule_course(courses=[[3, 2], [4, 3]]))

    def test_04(self):
        self.assertEqual(4, schedule_course(courses=[[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]]))
