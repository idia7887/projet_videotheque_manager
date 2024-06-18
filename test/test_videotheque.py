import unittest
from videotheque.videotheque import Videotheque
from videotheque.film import Film

class TestVideotheque(unittest.TestCase):
    def setUp(self):
        self.videotheque = Videotheque()
        self.film1 = Film("Inception", "Christopher Nolan", 2010)
        self.film2 = Film("Interstellar", "Christopher Nolan", 2014)
        self.videotheque.ajouter_film(self.film1)
        self.videotheque.ajouter_film(self.film2)

    def test_ajouter_film(self):
        self.assertIn(self.film1, self.videotheque.films)
        self.assertIn(self.film2, self.videotheque.films)

    def test_rechercher_film(self):
        result = self.videotheque.rechercher_film("Inception")
        self.assertEqual(result, [self.film1])

    def test_prêter_film(self):
        self.assertTrue(self.videotheque.prêter_film("Inception"))
        self.assertTrue(self.film1.emprunté)
        self.assertFalse(self.videotheque.prêter_film("Unknown"))

    def test_retourner_film(self):
        self.videotheque.prêter_film("Inception")
        self.assertTrue(self.film1.emprunté)
        self.assertTrue(self.videotheque.retourner_film("Inception"))
        self.assertFalse(self.film1.emprunté)
        self.assertFalse(self.videotheque.retourner_film("Unknown"))

if __name__ == "__main__":
    unittest.main()
