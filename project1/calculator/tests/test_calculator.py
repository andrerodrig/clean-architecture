#!/usr/bin/env python

"""Tests for `calculator` package."""

import pytest
from calculator.calculator import Calc

def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)

    assert res == 9


def test_add_many_numbers():
    c = Calc()

    many = range(100)

    assert c.add(*many) == 4950



def test_sub_two_numbers():
    c = Calc()

    assert c.sub(4, 5) == -1


def  test_sub_many_numbers():
    c = Calc()

    many = range(-50,50)

    assert c.sub(*many) == -50


def test_mul_two_numbers():
    c = Calc()

    assert c.mul(3, 10) == 30


def test_mul_many_numbers():
    c = Calc()
    many = range(1, 6)

    assert c.mul(*many) == 120

def test_mul_by_0_raises_exception():
    c = Calc()

    with pytest.raises(ValueError):
        c.mul(3, 0)



def test_div_two_numbers_float():
    c = Calc()
    res = c.div(13, 2)

    assert res == 6.5


def test_div_by_0_returns_inf():
    c = Calc()

    res = c.div(20, 0)

    assert res == 'inf'



def test_avg_correct_average():
    c = Calc()

    res = c.avg([2, 5, 12, 98])

    assert res == 29.25


def test_avg_removes_upper_outiers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=90)
    assert res == pytest.approx(6.33333)

def test_avg_removes_lower_outiers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], lt=10)
    assert res == pytest.approx(55)

def test_avg_upper_threshold_is_included():
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=98, lt=2)
    assert res == 29.25

def test_avg_empty_list():
    c = Calc()
    res = c.avg([])
    assert res == 0


def test_avg_manages_empty_list_after_outlier_removal():
    c = Calc()
    res = c.avg([12, 98], lt=15, ut=90)
    assert res == 0

def test_avg_manages_empty_list_before_outlier_removal():
    c = Calc()
    res = c.avg([], lt=15, ut=90)
    assert res == 0
