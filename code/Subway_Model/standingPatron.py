from patron import patron

class standingPatron(patron):
    '''This is a standing patron'''
    def __init__(self, speed=0):
        self.speed = speed
        print("initialize a standing patron at " + str(self.speed)+" feet per second")


