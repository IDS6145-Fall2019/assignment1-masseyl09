from patron import patron

class walkingPatron(patron):
    '''This is a walking patron'''

    def __init__(self,speed = 2):
        self.speed = speed
        print("initialize a walking patron at "+ str(self.speed) + " feet per second")