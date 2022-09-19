import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/find-duplicate-file-in-system/
# TC: O(paths * split paths)
# SC: O(paths * split paths)
# This solution uses a map to store the content as key and a list of
# files (dir + file path) with the same content.
def find_duplicate(paths: List[str]) -> List[List[str]]:
    fs_map = {}

    for path in paths:
        dir_files = path.split(" ")
        dir = dir_files[0]
        for idx in range(1, len(dir_files)):
            file_cont = dir_files[idx].split("(")
            file_cont[1] = file_cont[1].replace(")", "")

            lst_files = fs_map.get(file_cont[1], [])
            lst_files.append(dir + "/" + file_cont[0])

            fs_map[file_cont[1]] = lst_files

    output = []
    for items in fs_map.values():
        if len(items) > 1:
            output.append(items)

    return output


class FindDuplicateFileInSystem(unittest.TestCase):
    def test_01(self):
        self.assertEqual([["root/a/1.txt", "root/c/3.txt"], ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]],
                         find_duplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)",
                                         "root 4.txt(efgh)"]))

    def test_02(self):
        self.assertEqual([["root/a/1.txt", "root/c/3.txt"], ["root/a/2.txt", "root/c/d/4.txt"]], find_duplicate(
            ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]))
