
import pytest
from hypothesis import given, strategies as st

from salon_booking import (
    parse_booking,
    duration_average,
    payable_bill
)


# Test 1: Fuzz testing parse_booking()
@given(st.one_of(st.text(), st.none()))
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except Exception as e:
        pytest.fail(f"parse_booking crashed with input {s!r}: {e}")


# Test 2: Fuzz testing duration_average()
@given(st.one_of(st.text(), st.none()))
def test_duration_average_no_crash(s):
    try:
        duration_average(s)
    except Exception as e:
        pytest.fail(f"duration_average crashed with input {s!r}: {e}")


# Test 3: Fuzz testing payable_bill()
@given(st.one_of(st.text(), st.none()))
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except Exception as e:
        pytest.fail(f"payable_bill crashed with input {s!r}: {e}")
