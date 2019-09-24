from standingPatron import standingPatron
from walkingPatron import walkingPatron
from escalator import escalator

''' main '''

def stationCreate():
    standingPatron()
    walkingPatron()
    escalator()
    print("initialized a station")

def main():
    stationCreate()

if __name__ == "__main__":
    main()