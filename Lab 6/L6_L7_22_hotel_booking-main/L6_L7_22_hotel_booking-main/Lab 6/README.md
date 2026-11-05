# L6_L7_22_hotel_booking — Hotel Booking

Lab 6: Code and Branch Coverage

## About

A small Python module that works out hotel booking costs by room, season and guests, calculates cancellation refunds and handles room upgrades.

## Files

| File | Description |
|------|-------------|
| `hotel_booking.py` | The module under test |
| `test_hotel_booking.py` | Starter test file |
| `CodeCoverageTest_22_hotel_booking.py` | Tests used for line/code coverage |
| `BranchCoverageTest_22_hotel_booking.py` | Tests used for branch coverage |

Refer to the lab handout for instructions.

## Coverage commands

From this directory, run the line-coverage test suite:

```bash
python -m coverage erase
python -m coverage run -m pytest CodeCoverageTest_22_hotel_booking.py
python -m coverage report -m hotel_booking.py
```

Run the branch-coverage test suite:

```bash
python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_22_hotel_booking.py
python -m coverage report -m hotel_booking.py
```
