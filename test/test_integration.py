import unittest
from videotheque.videotheque import Videotheque
from videotheque.film import Film

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        videotheque = Videotheque()
        film1 = Film("Inception", "Christopher Nolan", 2010)
        film2 = Film("Interstellar", "Christopher Nolan", 2014)

        videotheque.ajouter_film(film1)
        videotheque.ajouter_film(film2)

        self.assertTrue(videotheque.prêter_film("Inception"))
        self.assertTrue(film1.emprunté)
        self.assertFalse(videotheque.prêter_film("Inception"))

        self.assertTrue(videotheque.retourner_film("Inception"))
        self.assertFalse(film1.emprunté)
        self.assertFalse(videotheque.retourner_film("Inception"))

        self.assertIn(film1, videotheque.rechercher_film("Inception"))
        self.assertIn(film2, videotheque.rechercher_film("Interstellar"))

if __name__ == "__main__":
    unittest.main()
