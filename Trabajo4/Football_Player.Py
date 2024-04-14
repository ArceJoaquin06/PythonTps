class Jugador:
    def __init__(self, nombre, edad, posición, club, país, número, goles, partidos, asistencias, amarillas, rojas, premios):
        self.nombre = nombre
        self.edad = edad
        self.posición = posición
        self.club = club
        self.país = país
        self.número = número
        self.goles = goles
        self.partidos = partidos
        self.asistencias = asistencias
        self.amarillas = amarillas
        self.rojas = rojas
        self.premios = premios

    def agregar_futbolista(self):
        self.nombre += input("Escribe el nombre que quieres para tu jugador: ")
        self.edad += int(input("Escribe la edad de tu jugador: "))
        self.posición += input("Escribe la posición de tu jugador: ")
        self.club += input("Escribe el club de tu jugador: ")
        self.país += input("Escribe el país de tu jugador: ")
        self.número += int(input("Escribe el número de tu jugador: "))
        self.goles += int(input("Escribe la cantidad de goles de tu jugador: "))
        self.partidos += int(input("Escribe la cantidad de partidos de tu jugador: "))
        self.asistencias += int(input("Escribe el número de asistencias de tu jugador: "))
        self.amarillas += int(input("Escribe el número de tarjetas amarillas de tu jugador: "))
        self.rojas += int(input("Escribe el número de tarjetas rojas de tu jugador: "))
        self.premios = {}
        trofeos = int(input("Escribe la cantidad de trofeos de tu jugador: "))
        for _ in range(trofeos):
            equipo = input("Escribe el equipo con quien ganó: ")
            premio = input("Escribe el premio que ganó: ")
            if equipo not in self.premios:
                self.premios[equipo] = []
            self.premios[equipo].append(premio)
        print(f'Los datos de tu jugador son: {self.nombre} de {self.edad} años, juega de {self.posición} en {self.club}, y en {self.país}, usa el {self.número}. Marcó {self.goles} goles y {self.asistencias} asistencias en {self.partidos}, le sacaron {self.amarillas} amarillas y {self.rojas} rojas. Ganó estos premios {self.premios}')

    def actualizar_info(self):
        self.partidos += 1
        self.goles += int(input("¿Cuántos goles hizo?: "))
        self.asistencias += int(input("¿Cuántas asistencias hizo?: "))
        self.amarillas += int(input("¿Cuántas amarillas le sacaron?: "))
        self.rojas += int(input("¿Cuántas rojas le sacaron?: "))
        print(f'Datos actualizados: Cantidad de goles actual: {self.goles}, Cantidad de asistencias: {self.asistencias}, Cantidad de amarillas: {self.amarillas}, Cantidad de rojas: {self.rojas}, Jugo un total de {self.partidos} partidos.')

    def goles_partido(self):
        self.promedio = self.goles / self.partidos
        print(f'El promedio de gol por partido de {self.nombre} es = {self.promedio}')

    def es_goleador(self):
        if self.promedio >= 0.8:
            print(f'{self.nombre} se consideraria un goleador')
        else:
            print(f'{self.nombre} no se consideraria un goleador')

    def agregar_premio(self):
        preg = input("¿Consiguió algún premio?. Escribe(s/n): ")
        if preg == 's':
            self.premios[input("Escibe el equipo con quien ganó: ")].append(input("Escribe el premio que ganó: "))
            print(f'Los premios que {self.nombre} ganó son: {self.premios} actualizados')
        elif preg == 'n':
            print(f'Los premios que {self.nombre} ganó son: {self.premios}')
        elif preg != 's' and preg != 'n':
            print("Usted escribió una respuesta distinta")
            Jugador.agregar_premio(self)


jugadorI = Jugador(" ", 0, " ", " ", " ", 0, 0, 0, 0, 0, 0 , {})
jugadorI.agregar_futbolista()

jugador1 = Jugador("Phil Foden", 23, "Extremo", "Manchester City", "Inglaterra", 47, 87, 288, 56, 8, 1, {"Inglaterra":['Campeón del Mundo SUB-17'],"Manchester City":['Campeón de la Supercopa de Inglaterra', 'Campeón de la Supercopa de Inglaterra', 'Campeón de la Copa de la Liga de Inglaterra', 'Campeón de la Copa de la Liga de Inglaterra', 'Campeón de la Copa de la Liga de Inglaterra', 'Campeón de la Copa de la Liga de Inglaterra', 'Campeón de la FA Cup de Inglaterra', 'Campeón de la FA Cup de Inglaterra', 'Campeón de la Supercopa de Europa', 'Campeón de Inglaterra', 'Campeón de Inglaterra', 'Campeón de Inglaterra', 'Campeón de Inglaterra', 'Campeón de Inglaterra', 'Campeón del Mundial de Clubes', 'Campeón de la Liga de Campeones']})
jugador1.actualizar_info()
jugador1.goles_partido()
jugador1.es_goleador()
jugador1.agregar_premio()

jugador2 = Jugador("Jérémy Doku", 21, "Extremo", "Manchester City", "Bélgica", 11, 29, 186, 30, 11, 2, {"Manchester City":['Campeón del Mundial de Clubes']})
jugador2.actualizar_info()
jugador2.goles_partido()
jugador2.es_goleador()
jugador2.agregar_premio()