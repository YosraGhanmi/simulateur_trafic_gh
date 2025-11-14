class FeuRouge:
    """
    Un feu rouge simple avec un cycle :
    - rouge
    - vert
    - orange
    Chaque état dure 'cycle' secondes (5 par defaut)
    """

    def __init__(self, cycle=5):
        self.cycle = cycle
        self.timer = 0
        self._etat = "rouge"   # état initial

    @property
    def etat(self):
        return self._etat

    def avancer_temps(self, dt):
        self.timer += dt

        if self.timer >= self.cycle:
            self.timer = 0

            # Changer d'état
            if self._etat == "rouge":
                self._etat = "vert"
            elif self._etat == "vert":
                self._etat = "orange"
            else:  # orange
                self._etat = "rouge"
