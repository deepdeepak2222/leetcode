"""
Given a maze in the form of a binary rectangular matrix, find the length of the shortest path from a given source to a given destination. The path can only be constructed out of cells having value 1, and at any moment, you can only move one step in one of the four directions (Top, Left, Down, Right).

Input:

matrix = [
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
src  = (0, 0)
dest = (5, 7)

Output: 12

Explanation: The shortest path from (0, 0) to (5, 7) has length 12. The shortest path is marked below with x.

[
	[x, x, x, x, x, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, x, 1, 0, 1, 0, 1],
	[0, 0, 1, 0, x, x, x, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, x, x, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, x, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, x, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

Note: The solution should return -1 if no path is possible.
"""

from typing import List, Tuple


# class Solution:
#     def findShortestPath(self, mat: List[List[int]], src: Tuple[int], dest: Tuple[int]) -> int:
#         print(src)
#         path_dist = 0
#         row_range = range(0, len(mat))
#         col_range = range(0, len(mat[0]))
#         # src_tmp = src
#
#         if src[0] not in row_range or src[1] not in col_range:
#             return 0
#
#         # Top
#         src_tmp = (src[0] - 1, src[1])
#         if self.findShortestPath(mat, src_tmp, dest):
#             return
#
#         # Left
#         if src[0] in row_range and (src[1] - 1) in col_range and mat[src[0]][src[1] - 1] == 1:
#             src_tmp = (src[0], src[1] - 1)
#             path_dist += 1
#
#         # Right
#         if src[0] in row_range and (src[1] + 1) in col_range and mat[src[0]][src[1] + 1] == 1:
#             src_tmp = (src[0], src[1] + 1)
#             path_dist += 1
#
#         # Down
#         if (src[0] + 1) in row_range and src[1] in col_range and mat[src[0] + 1][src[1]] == 1:
#             src_tmp = (src[0] + 1, src[1])
#             path_dist += 1
#
#         if src == dest or src_tmp == src:
#             return path_dist
#         elif src_tmp != src:
#             return self.findShortestPath(mat, src_tmp, dest)
#         else:
#             return 0


class Solution:
    max_dist = 10000000000000000000

    def findShortestPath(self, mat: List[List[int]], src: Tuple[int], dest: Tuple[int], dist=0, visited=[]) -> int:
        import pdb
        pdb.set_trace()
        print(src)
        print(visited)
        row_range = range(0, len(mat))
        col_range = range(0, len(mat[0]))

        if src[0] not in row_range or src[1] not in col_range:
            return self.max_dist

        if src[0] == dest[0] and src[1] == dest[1]:
            return dist

        if src[0] == mat[len(row_range)-1] and src[1] == mat[len(col_range)-1]:
            return self.max_dist

        visited[src[0]][src[1]] = 1
        tmp_dist = dist
        tmp_dist = tmp_dist + 1

        min_dist = self.max_dist
        # Top
        if src[0] - 1 in row_range and mat[src[0]-1][src[1]] == 1 and visited[src[0]-1][src[1]] == 0:
            # cost of travelling top
            dist_top = self.findShortestPath(mat, (src[0] - 1, src[1]), dest, tmp_dist, visited)
            if isinstance(dist_top, int) and dist_top < min_dist:
                min_dist = dist_top
            # print("dist_top: ", dist_top)

        # Bottom
        if src[0] + 1 in row_range and mat[src[0] + 1][src[1]] == 1 and visited[src[0] + 1][src[1]] == 0:
            # cost of travelling bottom
            dist_bottom = self.findShortestPath(mat, (src[0] + 1, src[1]), dest, tmp_dist, visited)
            # print("dist_bottom: ", dist_bottom)
            if isinstance(dist_bottom, int) and dist_bottom < min_dist:
                min_dist = dist_bottom

        # Left
        if src[0] in row_range and mat[src[0]][src[1]-1] == 1 and visited[src[0]][src[1]-1] == 0:
            # cost of travelling left
            dist_left = self.findShortestPath(mat, (src[0], src[1]-1), dest, tmp_dist, visited)
            # print("dist_left: ", dist_left)
            if isinstance(dist_bottom, int) and dist_bottom < min_dist:
                min_dist = dist_bottom

        # Right
        if src[0] in row_range and mat[src[0]][src[1]+1] == 1 and visited[src[0]][src[1]+1] == 0:
            # cost of travelling right
            dist_right = self.findShortestPath(mat, (src[0], src[1]+1), dest, tmp_dist, visited)
            # print("dist_right: ", dist_right)

        # print("\n** min_dist: ", min_dist)









        # path_dist = 0
        # # src_tmp = src
        #
        # if src[0] not in row_range or src[1] not in col_range:
        #     return 0
        #
        # # Top
        # src_tmp = (src[0] - 1, src[1])
        # if self.findShortestPath(mat, src_tmp, dest):
        #     return
        #
        # # Left
        # if src[0] in row_range and (src[1] - 1) in col_range and mat[src[0]][src[1] - 1] == 1:
        #     src_tmp = (src[0], src[1] - 1)
        #     path_dist += 1
        #
        # # Right
        # if src[0] in row_range and (src[1] + 1) in col_range and mat[src[0]][src[1] + 1] == 1:
        #     src_tmp = (src[0], src[1] + 1)
        #     path_dist += 1
        #
        # # Down
        # if (src[0] + 1) in row_range and src[1] in col_range and mat[src[0] + 1][src[1]] == 1:
        #     src_tmp = (src[0] + 1, src[1])
        #     path_dist += 1
        #
        # if src == dest or src_tmp == src:
        #     return path_dist
        # elif src_tmp != src:
        #     return self.findShortestPath(mat, src_tmp, dest)
        # else:
        #     return 0


matrix = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
src = (0, 0)
dest = (5, 7)
visited = [[0 for j in range(0, len(matrix[0]))] for i in range(0, len(matrix))]
print(Solution().findShortestPath(matrix, src, dest, visited=visited))




v = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
]
