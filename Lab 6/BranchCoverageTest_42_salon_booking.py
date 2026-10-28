
import pytest
from salon_booking import extra_time_charge, can_book, arrival_status


# Tests for extra_time_charge()

def test_unknown_service():
    with pytest.raises(ValueError, match="unknown service"):
        extra_time_charge("nails", 30, "junior", False)


def test_negative_duration():
    with pytest.raises(ValueError, match="invalid duration"):
        extra_time_charge("haircut", -1, "junior", False)


def test_within_included_time():
    assert extra_time_charge("haircut", 20, "junior", False) == 0


def test_member_haircut_extra_time():
    # Members get 15 additional included minutes for haircut.
    assert extra_time_charge("haircut", 40, "junior", True) == 0


def test_member_spa_no_extra_included_time():
    # Spa does not receive the member's extra 15 minutes.
    assert extra_time_charge("spa", 100, "junior", True) == 100


def test_junior_extra_time():
    assert extra_time_charge("haircut", 40, "junior", False) == 100


def test_non_junior_extra_time():
    assert extra_time_charge("haircut", 40, "senior", False) == 180



def test_extra_time_over_60_minutes_junior():
    assert extra_time_charge("haircut", 100, "junior", False) == 1260


def test_extra_time_over_60_minutes_senior():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100



# Tests for can_book()

def test_walk_in_allowed():
    assert can_book(2, 1, True) is True


def test_walk_in_too_large():
    assert can_book(3, 1, True) is False


def test_regular_booking_party_too_large():
    assert can_book(5, 1, False) is False


def test_regular_booking_too_many_services():
    assert can_book(3, 3, False) is False


def test_regular_booking_allowed():
    assert can_book(4, 2, False) is True


# Tests for arrival_status()

def test_arrival_open():
    assert arrival_status(10, False, False) == "open"


def test_arrival_late():
    assert arrival_status(0, False, False) == "late"


def test_arrival_closed():
    assert arrival_status(-11, False, False) == "closed"


def test_colour_weekend_cutoff():
    assert arrival_status(20, True, True) == "open"
