from circum_functions import *


def test_compute_circumference():
    assert round(compute_circumference(10), 3) == 62.832


def test_compute_area():
    assert round(compute_area(10),3) == 314.159



