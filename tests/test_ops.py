"""Tests for small_project.ops."""

from small_project.ops import multiply


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_negative_numbers():
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12


def test_multiply_by_zero():
    assert multiply(7, 0) == 0
    assert multiply(0, 7) == 0


def test_multiply_floats():
    assert multiply(1.5, 2.0) == 3.0
