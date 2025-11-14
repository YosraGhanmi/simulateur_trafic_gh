from typing import Any



class Affichage:
    def afficher_console(self, tour: int, reseau: Any, vitesses_moyennes: dict):
        """Affiche l'état succinct de la simulation dans la console pour un tour donné"""
        print(f"--- Tour {tour} ---")
        for nom, v in vitesses_moyennes.items():
            nb_vehicules = len(reseau.routes[nom].vehicules)
            print(f"Route {nom}: vm = {v:.2f} m/s, #véhicules = {nb_vehicules}")

    def tracer_vitesse_moyenne(self, stats):
        """convertit les statistiques brutes en un DataFrame Pandas"""
       
        
