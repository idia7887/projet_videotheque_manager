class Film:
    def __init__(self, titre, réalisateur, année):
        self.titre = titre
        self.réalisateur = réalisateur
        self.année = année
        self.emprunté = False

    def prêter(self):
        if not self.emprunté:
            self.emprunté = True
            return True
        return False

    def retourner(self):
        if self.emprunté:
            self.emprunté = False
            return True
        return False
