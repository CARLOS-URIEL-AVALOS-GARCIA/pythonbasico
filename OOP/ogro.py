from Enemigo import *
class ogro (Enemigo):
    def _int_(self, puntos_energia =10,ataque =3):
         super().__init__(tipo_enemigo='ogro',puntos_energia=puntos_energia,ataque=ataque)
    
    def habla(self):
            print("ogro aplasta todo")
