import pytest
from src.triangle import triangle_type

def test_triangle_is_equilateral():
    assert triangle_type(5,5,5) == 'Equilateral'

def test_triangle_is_isosceles():
    assert triangle_type(7,3,7) == 'Isosceles'

def test triangle_is_scalene():
    assert triangle_type(2,5,9) == 'Scalene'