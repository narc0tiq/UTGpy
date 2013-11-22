import world

def test_empty_world():
    w = world.World()
    assert w.northmost == world.Coordinates()
    assert w.southmost == world.Coordinates(63, 63)
    assert w.eastmost == world.Coordinates(63, 0)
    assert w.westmost == world.Coordinates(0, 63)
