
D6_DICE_FACE_DEFAULT: int = 6


class D6Dice(object): 
    face: int = D6_DICE_FACE_DEFAULT # number of faces/sides on the dice. 

    def __init__(self, face: int = D6_DICE_FACE_DEFAULT): 
        self.face = face

    def __str__(self):
        return 'd{}'.format(self.face)


