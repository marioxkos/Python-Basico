from enemigo import Enemigo


class Zombie(Enemigo):
    def _int_(self, puntos_energia=10, ataque=1):
        super()._init_(tipo_enemigo='Zombie', puntos_energia=puntos_energia,ataque=ataque)


        def habla(self):
            print("Hummmm...*")


        def propagar_enfermedad(self):
            print("El Zombie esta tratando de propagar la enfermedad!!")