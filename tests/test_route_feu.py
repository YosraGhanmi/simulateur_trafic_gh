from models.feu_rouge import *
from models.route import *
def test_arret_au_feu_rouge():
    route = Route("N",30,longueur=200)
    feu = FeuRouge(cycle=5)
    route.ajouter_feu_rouge(feu, position=50)

    v = Vehicule(id="V1", position=45, vitesse=10)
    route.vehicules.append(v)

    # Feu rouge, le véhicule doit s'arrêter à < 50
    route.update(dt=1)
    assert v.position == 45  # pas avancé car feu rouge