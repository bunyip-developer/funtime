"""
Example of Classes in Python.
Used to compare and contrast with other languages.
Follows the style guide of http://google.github.io/styleguide/pyguide.html
"""


class Superhero(object):
    """Superhero Class.

    More information on the Superhero class....

    Note: Inheriting from object is needed to make properties work properly in Python 2 and can protect your code from
    potential incompatibility with Python 3. It also defines special methods that implement the default semantics of
    objects including __new__, __init__, __delattr__, __getattribute__, __setattr__, __hash__, __repr__, and __str__.

    Attributes:
        name: A string of the name of the superhero.
        has_innate_superpowers: A boolean indicating if the superhero is superpowers
        is_alive: A boolean describing  whether the superhero is alive or dead.
    """

    def __init__(self, name, has_innate_superpowers, is_alive=True):
        """Inits Superhero class"""
        self.name = name
        self.has_innate_superpowers = has_innate_superpowers
        self.is_alive = is_alive

    def public_method(self):
        """Performs operation blah."""


if __name__ == '__main__':
    superman = Superhero(name='Superman', has_innate_superpowers=True)
    green_lantern = Superhero(name='Green Lantern', has_innate_superpowers=False)
