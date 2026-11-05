import pytest

from hotel_booking import booking_cost, cancellation_refund, room_upgrade


def test_booking_cost_for_deluxe_peak_stay_with_extra_guests():
    assert booking_cost("deluxe", 2, 4, True) == 10750


def test_booking_cost_applies_long_stay_discount():
    assert booking_cost("suite", 7, 2, False) == 37800


def test_booking_cost_rejects_unknown_room():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("presidential", 1, 2, False)


def test_booking_cost_rejects_non_positive_nights():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_cancellation_refund_for_partial_refund():
    assert cancellation_refund(1000, 3, False) == 500


def test_cancellation_refund_for_no_refund():
    assert cancellation_refund(1000, 1, False) == 0


def test_cancellation_refund_adds_member_bonus():
    assert cancellation_refund(1000, 3, True) == 750


def test_room_upgrade_for_member():
    assert room_upgrade("standard", True, 1) == "deluxe"


def test_room_upgrade_when_no_rooms_are_free():
    assert room_upgrade("standard", True, 0) == "standard"


def test_room_upgrade_for_non_member():
    assert room_upgrade("standard", False, 1) == "standard"
