import pytest


def asteroid_collision(asteroids):
    survivors = []
    for asteroid in asteroids:
        while len(survivors) and asteroid < 0 and survivors[-1] > 0:
            if -asteroid == survivors[-1]:
                survivors.pop(-1)
                break
            elif -asteroid < survivors[-1]:
                break
            elif -asteroid > survivors[-1]:
                survivors.pop(-1)
                continue
        else:
            survivors.append(asteroid)
    return survivors


testdata = [([1, 1], [1, 1]), ([-1, -1], [-1, -1]), ([1, 2, -5], [-5]), ([1, -1], [])]


@pytest.mark.parametrize("asteroids, expected", testdata)
def test_asteroid_collision(asteroids, expected):
    actual = asteroid_collision(asteroids)
    assert actual == expected
