from typing import List

import pytest


class QuickFind:
    def __init__(self, length: int):
        self.length = length
        self.ids = self._create_list()

    def _create_list(self) -> List[int]:
        return [i for i in range(self.length)]

    def check_dots_connection(self, dot_one: int, dot_two: int) -> bool:
        return self.ids[dot_one] == self.ids[dot_two]

    def union_dots(self, dot_one: int, dot_two: int):
        id_one = self.ids[dot_one]
        id_two = self.ids[dot_two]

        if id_one != id_two:
            self.ids = [id_one if id == id_two else id for id in self.ids]


@pytest.mark.parametrize(
    "length, dot_sets, expected_ids",
    [
        [4, [(0, 1)], [0, 0, 2, 3]],
        [4, [(0, 2)], [0, 1, 0, 3]],
        [5, [(0, 2), (3, 2)], [3, 1, 3, 3, 4]],
    ],
)
def test_one_union(length, dot_sets, expected_ids):
    quick_find = QuickFind(length)
    for dots in dot_sets:
        dot_one, dot_two = dots
        if not quick_find.check_dots_connection(dot_one, dot_two):
            quick_find.union_dots(dot_one, dot_two)

    assert quick_find.ids == expected_ids
