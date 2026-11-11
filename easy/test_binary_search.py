import pytest
from binary_search import loop_binary_search


@pytest.mark.parametrize(
    "num_list, target, result",
    [([], 2, -1), ([3], 3, 0), ([9, 2, 1, 4], 4, 3), ([1, 2, 3], 5, -1)],
)
def test_loop_binary(num_list, target, result):
    assert loop_binary_search(num_list, target) == result
