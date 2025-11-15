import pytest
import json
from core.simulateur import Simulateur
from models.route import Route
from models.vehicule import Vehicule


class TestSimulateur:
    """Tests d'intégration pour la classe Simulateur"""
    
    def test_creation_simulateur_sans_config(self):
        """Test de la création d'un simulateur sans fichier de configuration"""
        simu = Simulateur()
        
        assert simu.reseau is not None
        assert len(simu.reseau.routes) == 0
        assert simu.analyseur is not None
        assert simu.affichage is not None
        assert simu.export is not None
    
    