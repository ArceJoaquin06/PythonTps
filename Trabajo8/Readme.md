# Trabajo Práctico N°8 - Fixture Copa América 2024 CSV - Arce Joaquín

## Objetivo

Desarrollar una aplicación en Python que gestione el fixture de la Copa América 2024 utilizando archivos CSV. La aplicación debe cargar datos de los equipos y partidos, actualizar los resultados y calcular las posiciones de los equipos en cada grupo.

## Requerimientos

### Lectura de Archivos

- Leer el archivo CSV `copa-america-2024-UTC.csv` con el fixture de la Copa América 2024.
- Formato del archivo CSV: Match Number, Round Number, Date, Location, Home Team, Away Team, Group, Result.

### Cálculo de Posiciones

Implementar un método para calcular las posiciones de los equipos en cada grupo basándose en los resultados actualizados.

#### Criterios para determinar las posiciones:

1. **Puntos:** Se asignan 3 puntos por cada victoria, 1 punto por cada empate y 0 puntos por cada derrota.
2. **Diferencia de Goles:** Se considera la diferencia entre goles a favor y goles en contra.
3. **Goles a Favor:** Total de goles anotados por el equipo.
4. **Resultado entre equipos empatados:** En caso de empate en puntos, diferencia de goles y goles a favor, se considera el resultado directo entre los equipos empatados.

### Salida de Datos

Generar un informe final que muestre la tabla de posiciones de cada grupo en formato CSV.

#### Formato del archivo de salida:

Grupo, Equipo, Puntos, Partidos Jugados, Victorias, Empates, Derrotas, GolesAFavor, GolesEnContra, DiferenciaDeGoles.