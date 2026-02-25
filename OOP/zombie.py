from Enemigo import *

class Zombie(Enemigo):
    def __int_(self,puntos_energia = 10, ataque=1):
        super().__init__(tipo_enemigo='Zombie',puntos_energia=puntos_energia,ataque=ataque)

    def habla(self):
            print("hhummmmmmm...*")

    def propagar_emfermedad(self):
         print("El zombie esta tratando de propagar ls enfermedad")