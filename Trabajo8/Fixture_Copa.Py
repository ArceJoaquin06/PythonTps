import csv

def leer_fixture(archivo_csv):
    partidos = []
    with open(archivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            partidos.append(row)
    return partidos

def inicializar_equipos(partidos):
    equipos = {}
    for partido in partidos:
        if partido['Home Team'] not in equipos:
            equipos[partido['Home Team']] = {
                'Puntos': 0, 'PJ': 0, 'PG': 0, 'PE': 0,
                'PP': 0, 'Goles a Favor': 0, 'Goles en Contra': 0, 'Diferencia de Goles': 0
            }
        if partido['Away Team'] not in equipos:
            equipos[partido['Away Team']] = {
                'Puntos': 0, 'PJ': 0, 'PG': 0, 'PE': 0,
                'PP': 0, 'Goles a Favor': 0, 'Goles en Contra': 0, 'Diferencia de Goles': 0
            }
    return equipos

def actualizar_resultados(archivo_csv_resultados, equipos, partidos):
    with open(archivo_csv_resultados, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            actualizar_partido(row, equipos, partidos)

def actualizar_partido(resultado, equipos, partidos):
    partido_num = int(resultado['Match Number'])
    goles_local = int(resultado['Home Team Goals'])
    goles_visitante = int(resultado['Away Team Goals'])
    
    for partido in partidos:
        if int(partido['Match Number']) == partido_num:
            partido['Result'] = f"{goles_local}-{goles_visitante}"
            actualizar_estadisticas(partido, goles_local, goles_visitante, equipos)
            break

def actualizar_estadisticas(partido, goles_local, goles_visitante, equipos):
    equipo_local = partido['Home Team']
    equipo_visitante = partido['Away Team']
    
    equipos[equipo_local]['PJ'] += 1
    equipos[equipo_visitante]['PJ'] += 1
    equipos[equipo_local]['Goles a Favor'] += goles_local
    equipos[equipo_visitante]['Goles a Favor'] += goles_visitante
    equipos[equipo_local]['Goles en Contra'] += goles_visitante
    equipos[equipo_visitante]['Goles en Contra'] += goles_local
    equipos[equipo_local]['Diferencia de Goles'] += (goles_local - goles_visitante)
    equipos[equipo_visitante]['Diferencia de Goles'] += (goles_visitante - goles_local)
    
    if goles_local > goles_visitante:
        equipos[equipo_local]['PG'] += 1
        equipos[equipo_local]['Puntos'] += 3
        equipos[equipo_visitante]['PP'] += 1
    elif goles_local < goles_visitante:
        equipos[equipo_visitante]['PG'] += 1
        equipos[equipo_visitante]['Puntos'] += 3
        equipos[equipo_local]['PP'] += 1
    else:
        equipos[equipo_local]['PE'] += 1
        equipos[equipo_visitante]['PE'] += 1
        equipos[equipo_local]['Puntos'] += 1
        equipos[equipo_visitante]['Puntos'] += 1

def calcular_posiciones(equipos):
    posiciones = sorted(equipos.items(), key=lambda item: (
        item[1]['Puntos'], item[1]['Diferencia de Goles'], item[1]['Goles a Favor']), reverse=True)
    return posiciones

def generar_informe_final(posiciones, archivo_salida):
    with open(archivo_salida, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Grupo', 'Equipo', 'Puntos', 'PJ', 'PG', 'PE', 'PP', 'Goles a Favor', 'Goles en Contra', 'Diferencia de Goles'])
        for equipo, stats in posiciones:
            writer.writerow(['Grupo X', equipo, stats['Puntos'], stats['PJ'], stats['PG'], stats['PE'], stats['PP'], stats['Goles a Favor'], stats['Goles en Contra'], stats['Diferencia de Goles']])

def mostrar_menu():
    print("Menú de Opciones:")
    print("1. Ver el Fixture")
    print("2. Actualizar los Resultados")
    print("3. Calcular las Posiciones")
    print("4. Generar el Informe")
    print("5. Salir")

def main():
    archivo_fixture = 'copa-america-2024-UTC.csv'
    archivo_resultados = 'resultado.csv'
    archivo_informe = 'posicion_final.csv'
    
    partidos = []
    equipos = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            partidos = leer_fixture(archivo_fixture)
            equipos = inicializar_equipos(partidos)
            for partido in partidos[:10]:
                print(partido)
                
        elif opcion == '2':
            if not partidos:
                print("Aún no has cargado el fixture.")
            else:
                actualizar_resultados(archivo_resultados, equipos, partidos)
                print("Los resultados están actualizados.")
                
        elif opcion == '3':
            if not equipos:
                print("Primero tenes que cargar el fixture y actualizar los resultados.")
            else:
                posiciones = calcular_posiciones(equipos)
                for equipo, stats in posiciones:
                    print(equipo, stats)
                    
        elif opcion == '4':
            if not equipos:
                print("Primero tenes que cargar el fixture y actualizar los resultados.")
            else:
                posiciones = calcular_posiciones(equipos)
                generar_informe_final(posiciones, archivo_informe)
                print(f"Informe generado en {archivo_informe}.")
                
        elif opcion == '5':
            print("Has salido")
            break
            
        else:
            print("Error, intenta de nuevo.")

if __name__ == '__main__':
    main()