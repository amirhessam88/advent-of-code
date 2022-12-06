import importlib.resources as pkg_resources

from assertpy import assert_that

from aoc.year_2022 import day1, day2, day3, day4, day5, day6
from tests.resources import inputs_2022
from tests.utils import _clean_test_data


def test_day_1() -> None:
    with pkg_resources.open_text(inputs_2022, "day1.txt") as f:
        data = _clean_test_data(f)
        assert_that(day1.part1(data)).is_equal_to(67016)
        assert_that(day1.part2(data)).is_equal_to(200116)


def test_day_2() -> None:
    with pkg_resources.open_text(inputs_2022, "day2.txt") as f:
        data = _clean_test_data(f)
        assert_that(day2.part1(data)).is_equal_to(10404)
        assert_that(day2.part2(data)).is_equal_to(10334)


def test_day_3() -> None:
    with pkg_resources.open_text(inputs_2022, "day3.txt") as f:
        data = _clean_test_data(f)
        assert_that(day3.part1(data)).is_equal_to(8240)
        assert_that(day3.part2(data)).is_equal_to(2587)


def test_day_4() -> None:
    with pkg_resources.open_text(inputs_2022, "day4.txt") as f:
        data = _clean_test_data(f)
        assert_that(day4.part1(data)).is_equal_to(464)
        assert_that(day4.part2(data)).is_equal_to(770)


def test_day_5() -> None:
    with pkg_resources.open_text(inputs_2022, "day5.txt") as f:
        data = _clean_test_data(f)
        assert_that(day5.part1(data)).is_equal_to("QPJPLMNNR")
        assert_that(day5.part2(data)).is_equal_to("BQDNWJPVJ")


def test_day_6() -> None:
    with pkg_resources.open_text(inputs_2022, "day6.txt") as f:
        data = _clean_test_data(f)
        assert_that(day6.part1(data)).is_equal_to(1142)
        assert_that(day6.part2(data)).is_equal_to(2803)
