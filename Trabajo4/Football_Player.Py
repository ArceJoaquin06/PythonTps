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

    def goles_partido(self):
        self.promedio = self.goles / self.partidos
        print(f'El promedio de gol por partido de {self.nombre} es = {self.promedio}')

    def es_goleador(self):
        if self.promedio >= 0.8:
            print(f'{self.nombre} se consideraria un goleador')
        else:
            print(f'{self.nombre} no se consideraria un goleador')

jugador1 = Jugador("Phil Foden", 23, "Extremo", "Manchester City", "Inglaterra", 47, 87, 288, 56, 8, 1, 17)
jugador1.goles_partido()
jugador1.es_goleador()

jugador2 = Jugador("Jérémy Doku", 21, "Extremo", "Manchester City", "Bélgica", 11, 29, 186, 30, 11, 2, 1)
jugador2.goles_partido()
jugador2.es_goleador()