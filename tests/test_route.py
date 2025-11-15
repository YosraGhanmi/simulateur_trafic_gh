import pytest
from models.route import Route
from models.vehicule import Vehicule


class TestRoute:
    """Tests unitaires pour la classe Route"""
    
    def test_creation_route(self):
        """Test de la création d'une route"""
        route = Route("A1", longueur=1000, limite_vitesse=30)
        assert route.nom == "A1"
        assert route.longueur == 1000.0
        assert route.limite_vitesse == 30.0
        assert len(route.vehicules) == 0
    
   