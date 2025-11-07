class VehiculeError(Exception):
    """Base class for vehicle-related exceptions."""
    pass


class VitesseNegativeError(VehiculeError):
    """Raised when the vehicle's speed is negative."""
    def __init__(self, vitesse):
        super().__init__(f"Vitesse négative détectée : {vitesse} m/s")


class PositionInvalideError(VehiculeError):
    """Raised when the vehicle's position is invalid."""
    def __init__(self, position):
        super().__init__(f"Position invalide détectée : {position} m")

class RouteError(Exception):
    """Classe de base pour les exceptions liées à une route."""
    pass


class RoutePleineError(RouteError):
    """Exception levée quand la route atteint sa capacité maximale."""
    def __init__(self, nom):
        super().__init__(f"La route '{nom}' est pleine.")


class VehiculeDejaPresentError(RouteError):
    """Exception levée quand un véhicule est déjà présent sur la route."""
    def __init__(self, vehicule_id, nom):
        super().__init__(f"Le véhicule '{vehicule_id}' est déjà sur la route '{nom}'.")

class VehiculePasPresentError(RouteError):
    """Exception levée quand un véhicule n est présent sur la route et on veut la supprimer."""
    def __init__(self, vehicule_id, nom):
        super().__init__(f"Le véhicule '{vehicule_id}' n est pas presente sur la route '{nom}'.")

class SimulateurError(Exception):
    """Classe de base pour les exceptions du simulateur."""
    pass


class FichierConfigError(SimulateurError):
    """Erreur liée à la lecture du fichier de configuration."""
    def __init__(self, path, message="Erreur de lecture du fichier de configuration"):
        super().__init__(f"{message} : {path}")


class IterationInvalideError(SimulateurError):
    """nombre d'itérations est invalide."""
    def __init__(self, n_tours):
        super().__init__(f"Nombre d'itérations invalide : {n_tours}. Il doit être supérieur à 0.")

class AnalyseurError(Exception):
    """erreurs liées à l'analyse."""
    pass


class DonneesManquantesError(AnalyseurError):
    """données d'analyse manquantes."""
    def __init__(self, element):
        super().__init__(f"Données manquantes pour : {element}")


class DivisionParZeroError(AnalyseurError):
    """tentative de division par zéro."""
    def __init__(self, message="Division par zéro détectée lors d'un calcul statistique"):
        super().__init__(message)
