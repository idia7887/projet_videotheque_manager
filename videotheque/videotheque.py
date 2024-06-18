from .film import Film

class Videotheque:
    def __init__(self):
        self.films = []

    def ajouter_film(self, film):
        self.films.append(film)

    def rechercher_film(self, titre):
        return [film for film in self.films if titre.lower() in film.titre.lower()]

    def prêter_film(self, titre):
        for film in self.films:
            if film.titre == titre:
                return film.prêter()
        return False

    def retourner_film(self, titre):
        for film in self.films:
            if film.titre == titre:
                return film.retourner()
        return False
