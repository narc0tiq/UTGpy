from world import tiles

NOTHING_DICT = { 'name': 'nothing' }
GRASS_DICT = { 'name': 'grass', 'degrades_to': 'nothing' }

NOTHING_TILE = tiles.Tile(name='nothing', degrades_to=None)
GRASS_TILE = tiles.Tile(name='grass', degrades_to='nothing')

TILES_LIST = [ NOTHING_DICT, GRASS_DICT ]

def test_degradable_from_dict():
    loader = tiles.Loader()

    t = loader.tile_from_dict(GRASS_DICT)

    assert t == GRASS_TILE

def test_core_from_dict():
    loader = tiles.Loader()

    t = loader.tile_from_dict(NOTHING_DICT)

    assert t == NOTHING_TILE

def test_tiles_from_list():
    loader = tiles.Loader()

    tilelist = loader.tiles_from_list(TILES_LIST)

    assert tilelist[0] == NOTHING_TILE
    assert tilelist[1] == GRASS_TILE
