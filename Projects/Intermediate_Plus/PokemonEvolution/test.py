import unittest
from pokemon import *

class TestPokemonEvolution(unittest.TestCase):

    pokemon = Pokemon()

    def setUp(self):
        pass

    def test_EvolutionDictionary(self):
        self.assertDictEqual(self.pokemon.Evolution("caterpie"),{'name': 'caterpie', 'chain': [{'name': 'metapod', 'chain': [{'name': 'butterfree', 'chain': []}]}]})

    def test_EvolutionList(self):
        self.assertListEqual(self.pokemon.EvolutionNames("caterpie"),['caterpie', 'metapod', 'butterfree'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
