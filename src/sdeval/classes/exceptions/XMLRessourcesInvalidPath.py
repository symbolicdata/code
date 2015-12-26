class XMLRessourcesInvalidPath(Exception):
    """
    If the given path for the XMLRessources is not valid, this exception is raised.

    .. moduleauthor::  Albert Heinle <albert.heinle@rwth-aachen.de>
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
