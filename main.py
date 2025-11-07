from core.simulateur import Simulateur
import cProfile
import pstats

if __name__ == '__main__':
    with cProfile.Profile() as pr:
        from core.simulateur import Simulateur
        simulateur = Simulateur()
        simulateur.lancer_simulation()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME).print_stats(20)
"""  try:
        simu = Simulateur(fichier_config='data/config_reseau.json')
        simu.lancer_simulation(n_tours=60, delta_t=1, afficher=True, export_path='resultats.json')
        print('Simulation terminée. Résultats exportés dans resultats.json')
    except Exception as e:
        print(f"Erreur pendant la simulation : {e}")"""