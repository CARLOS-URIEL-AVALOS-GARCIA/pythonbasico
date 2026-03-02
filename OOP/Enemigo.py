class Enemigo:
    tipo_Enemigo:str
    puntos_de_energia: int = 10
    ataque = 1

    def _int_(self,tipo_enemigo, puntos_energia=10, ataque=1):
        self.__tipo_enemigo = tipo_enemigo
        self.puntos_energia = puntos_energia
        self.ataque = ataque

        def get_tipo_enemigo(self):
            return self.__tipo_enemigo
        
        def habla(self):
            print(f"yo soy {self.__tipo_Enemigo}. preparando para pelear")

            def camina(self):
                print(f"{self.__tipo_enemigo} se mueve cerca de ti")
                
                def atacar(self):
                    print(f"{self.__tipo_Enemigo} ataca con un {self.ataque} de daño")

                    def ataque_especial(self):
                        print("enemigo nno tiene ataque especial")