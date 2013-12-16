from world import tiles

def test_degradable_tile_creation():
    t = tiles.Tile(name='grass', degrades_to='nothing')

    # Tiles have no behaviour; just assert things are where we expect

    assert t.name == 'grass'
    assert t.degrades_to == 'nothing'

def test_core_tile_creation():
    t = tiles.Tile(name='nothing', degrades_to=None)

    assert t.name == 'nothing'
    assert t.degrades_to is None

