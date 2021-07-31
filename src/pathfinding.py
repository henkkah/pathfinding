from data_for_app import data_for_app
from ui import ui


def main():
    """Reads base data for the app and starts ui for the user.
    
    Args:
        no arguments - uses base data for the app from csv files
    
    Returns:
        no return value - app closes when user decides to close it
    """
    
    cities, coordinates, speedlimits, adjlist = data_for_app()
    
    ui(cities, coordinates, speedlimits, adjlist)


main()


