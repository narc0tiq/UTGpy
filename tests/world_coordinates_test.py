import pytest
import world

def test_empty_coordinates():
    coords = world.Coordinates()
    assert coords.x == 0
    assert coords.y == 0

def test_specific_coordinates():
    coords = world.Coordinates(3, 4)
    assert coords.x == 3
    assert coords.y == 4

def test_coordinates_with_kwargs():
    coords = world.Coordinates(x=1, y=2)
    assert coords.x == 1
    assert coords.y == 2

def test_coordinates_offset():
    initial = world.Coordinates(x=1, y=2)
    final = initial.offset_by(dx=3, dy=4)
    assert initial.x == 1
    assert initial.y == 2
    assert final.x == (1 + 3)
    assert final.y == (2 + 4)

def test_manhattan_distance_from_origin():
    initial = world.Coordinates()
    final = world.Coordinates(3, 4)
    assert initial.manhattan_distance_to(final) == (3 + 4)

def test_manhattan_distance_arbitrary():
    initial = world.Coordinates(10, 10)
    final = world.Coordinates(13, 14)
    assert initial.manhattan_distance_to(final) == (3 + 4)

def test_manhattan_distance_inverse():
    initial = world.Coordinates(3, 4)
    final = world.Coordinates()
    assert initial.manhattan_distance_to(final) == (3 + 4)

def test_real_distance_from_origin():
    initial = world.Coordinates()
    final = world.Coordinates(3,4)
    assert initial.distance_to(final) == 5 # because Pythagoras

def test_real_distance_arbitrary():
    initial = world.Coordinates(10, 10)
    final = world.Coordinates(13, 14)
    assert initial.distance_to(final) == 5

def test_real_distance_inverse():
    initial = world.Coordinates(3, 4)
    final = world.Coordinates()
    assert initial.distance_to(final) == 5

def test_coordinate_equality():
    initial = world.Coordinates(3, 4)
    final = world.Coordinates(3, 4)
    assert initial == final

def test_coordinate_inequality():
    initial = world.Coordinates()
    final = world.Coordinates(3, 4)
    assert initial != final

def test_non_coordinate_equality():
    initial = world.Coordinates()
    final = object()
    with pytest.raises(AttributeError):
        initial == final

def test_non_coordinate_inequality():
    initial = world.Coordinates()
    final = object()
    with pytest.raises(AttributeError):
        initial != final
