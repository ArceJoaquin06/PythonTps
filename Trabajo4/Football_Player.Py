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
        

jugador1 = Jugador("Phil Foden", 23, "Extremo", "Manchester City", "Inglaterra", 47, 87, 288, 56, 8, 1, {"Inglaterra":'Campeón del Mundo SUB-17',"Manchester City":'Campeón de la Supercopa de Inglaterra', "Manchester City":'Campeón de la Supercopa de Inglaterra', "Manchester City":'Campeón de la Copa de la Liga de Inglaterra', "Manchester City":'Campeón de la Copa de la Liga de Inglaterra', "Manchester City":'Campeón de la Copa de la Liga de Inglaterra', "Manchester City":'Campeón de la Copa de la Liga de Inglaterra', "Manchester City":'Campeón de la FA Cup de Inglaterra', "Manchester City":'Campeón de la FA Cup de Inglaterra', "Manchester City":'Campeón de la Supercopa de Europa', "Manchester City":'Campeón de Inglaterra', "Manchester City":'Campeón de Inglaterra', "Manchester City":'Campeón de Inglaterra', "Manchester City":'Campeón de Inglaterra', "Manchester City":'Campeón de Inglaterra', "Manchester City":'Campeón del Mundial de Clubes', "Manchester City":'Campeón de la Liga de Campeones'})
jugador1.actualizar_info()
jugador1.goles_partido()
jugador1.es_goleador()


jugador2 = Jugador("Jérémy Doku", 21, "Extremo", "Manchester City", "Bélgica", 11, 29, 186, 30, 11, 2, {"Manchester City":'Campeón del Mundial de Clubes'})
jugador2.actualizar_info()
jugador2.goles_partido()
jugador2.es_goleador()
