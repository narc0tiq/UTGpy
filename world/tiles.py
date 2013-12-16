from collections import namedtuple

Tile = namedtuple('Tile', ['name', 'degrades_to'])

class Loader(object):
    """
    Loads a :py:class:`Tile` from some kind of serializable representation.

    Supported representations:
        - dictionary containing one tile (e.g. from json.loads('{"name":"blah"...}'))
        - list of dictionaries each containing one tile (e.g. from json.loads('[{...},{...}]'))
    """

    def tile_from_dict(self, d):
        """
        Load a :py:class:`Tile` from a dictionary.

        The dictionary **must** have a 'name' key and *may* also have a 'degrades_to' key.
        No validation is done to ensure the `degrades_to` tile actually exists.
        """

        degrade_name = None
        if d.has_key('degrades_to'):
            degrade_name = d['degrades_to']

        return Tile(d['name'], degrade_name)

    def tiles_from_list(self, l):
        """
        Load a list of :py:class:`.Tile` s from a list of dictionaries.

        See :py:meth:`.tile_from_dict` for the form of the dictionaries.
        """
        return [self.tile_from_dict(d) for d in l]
