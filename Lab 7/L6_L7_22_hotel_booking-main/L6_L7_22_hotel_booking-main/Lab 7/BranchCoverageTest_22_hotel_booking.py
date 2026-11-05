import pytest

from hotel_booking import booking_cost, cancellation_refund, room_upgrade


@pytest.mark.parametrize(
    ("room", "nights", "guests", "is_peak_season", "expected"),
    [
        ("standard", 2, 2, False, 4000),
        ("deluxe", 2, 2, True, 8750),
        ("standard", 2, 3, False, 5000),
        ("suite", 7, 2, False, 37800),
        ("suite", 7, 3, True, 50400),
    ],
)
def test_booking_cost_branches(room, nights, guests, is_peak_season, expected):
    assert booking_cost(room, nights, guests, is_peak_season) == expected


@pytest.mark.parametrize(
    ("room", "nights", "message"),
    [
        ("unknown", 1, "unknown room"),
        ("standard", 0, "invalid nights"),
    ],
)
def test_booking_cost_validation_branches(room, nights, message):
    with pytest.raises(ValueError, match=message):
        booking_cost(room, nights, 2, False)


@pytest.mark.parametrize(
    ("days_before", "is_member", "expected"),
    [
        (7, False, 1000),
        (2, False, 500),
        (1, False, 0),
        (2, True, 750),
    ],
)
def test_cancellation_refund_branches(days_before, is_member, expected):
    assert cancellation_refund(1000, days_before, is_member) == expected


@pytest.mark.parametrize(
    ("room", "is_member", "rooms_free", "expected"),
    [
        ("standard", True, 0, "standard"),
        ("standard", True, 1, "deluxe"),
        ("deluxe", True, 1, "suite"),
        ("suite", True, 1, "suite"),
        ("standard", False, 1, "standard"),
    ],
)
def test_room_upgrade_branches(room, is_member, rooms_free, expected):
    assert room_upgrade(room, is_member, rooms_free) == expected
