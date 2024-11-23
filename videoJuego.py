class Personajes():
    def __init__(self, poder, nombre, fuerza, vida=100):
        self._poder = poder
        self._nombre = nombre
        self._fuerza = fuerza
        self._vida = vida  # Añadir vida a los personajes

    def atacar(self, enemigo):
        # El daño se calcula en base a la fuerza
        daño = self._fuerza
        enemigo.recibir_daño(daño)
        return daño

    def recibir_daño(self, cantidad):
        self._vida -= cantidad

    def esta_muerto(self):
        return self._vida <= 0

    def get_nombre(self):
        return self._nombre


class Magos(Personajes):
    def __init__(self, poder, nombre, fuerza, ritual):
        super().__init__(poder, nombre, fuerza)
        self.__ritual = ritual
        self.__hechizos = []
        self.__nivel_magia = 1
        self.__exp_magia = 0
        self.__exp_requerida = 100

    def agregar_hechizo(self, hechizo):
        self.__hechizos.append(hechizo)

    # Método específico para lanzar hechizos, que también podría atacar
    def lanzar_hechizo(self, enemigo, hechizo):
        daño = self._fuerza * 2  # El daño de un hechizo es mayor
        enemigo.recibir_daño(daño)
        return daño


class Hechizero(Personajes):
    def __init__(self, poder, nombre, fuerza, nivel_magia, exp_magia):
        super().__init__(poder, nombre, fuerza)
        self.__nivel_magia = nivel_magia
        self.__exp_magia = exp_magia
        self.__exp_requerida = 100
        self.__hechizos = []
        self.__potencia_hechizo = 1
        self.__nivel_hechizo = 1
        self.__nivel_hechizo_actual = 1
        self.__nivel_hechizo_maximo = 10

    def lanzar_hechizo(self, enemigo):
        daño = self._fuerza * 1.5
        enemigo.recibir_daño(daño)
        return daño


class Arquero(Personajes):
    def __init__(self, poder, nombre, fuerza, arma, velocidad):
        super().__init__(poder, nombre, fuerza)
        self.__arma = arma
        self.__velocidad = velocidad
        self.__ataque_especial = False
        self.__nivel_armadura = 1
        self.__exp_armadura = 0
        self.__exp_requerida = 100

    def disparar_flecha(self, enemigo):
        daño = self._fuerza
        enemigo.recibir_daño(daño)
        return daño


# Función para elegir personaje
def elegir_personaje():
    print("Elige un personaje:")
    print("1. Mago")
    print("2. Hechizero")
    print("3. Arquero")
    opcion = input("Ingresa el número de tu elección: ")

    if opcion == '1':
        return Magos(poder="Fuego", nombre="Gandalf", fuerza=10, ritual="Ritual de Fuego")
    elif opcion == '2':
        return Hechizero(poder="Hielo", nombre="Merlin", fuerza=8, nivel_magia=1, exp_magia=0)
    elif opcion == '3':
        return Arquero(poder="Viento", nombre="Legolas", fuerza=9, arma="Arco", velocidad=10)
    else:
        print("Opción no válida.")
        return elegir_personaje()

# Simulación de combate
def combate(personaje1, personaje2):
    while True:
        # Alternar ataque
        daño = personaje1.atacar(personaje2)
        print(f"{personaje2.get_nombre()} ha recibido {daño} puntos de daño.")
        if personaje2.esta_muerto():
            print(f"{personaje1.get_nombre()} ha ganado el combate!")
            break

        daño = personaje2.atacar(personaje1)
        print(f"{personaje1.get_nombre()} ha recibido {daño} puntos de daño.")
        if personaje1.esta_muerto():
            print(f"{personaje2.get_nombre()} ha ganado el combate!")
            break

# Ejecución del juego
personaje_usuario = elegir_personaje()
personaje_enemigo = Arquero(poder="Tierra", nombre="Robin", fuerza=7, arma="Ballesta", velocidad=8)  # Enemigo de ejemplo
combate(personaje_usuario, personaje_enemigo)
