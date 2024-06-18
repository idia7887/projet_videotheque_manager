import unittest
from videotheque.film import Film

class TestFilm(unittest.TestCase):
    def test_prêter(self):
        film = Film("Inception", "Christopher Nolan", 2010)
        self.assertFalse(film.emprunté)
        self.assertTrue(film.prêter())
        self.assertTrue(film.emprunté)
        self.assertFalse(film.prêter())

    def test_retourner(self):
        film = Film("Inception", "Christopher Nolan", 2010)
        film.prêter()
        self.assertTrue(film.emprunté)
        self.assertTrue(film.retourner())
        self.assertFalse(film.emprunté)
        self.assertFalse(film.retourner())

if __name__ == "__main__":
    unittest.main()
