from random import choice

preguntas = ['¿Qué se encuentra una vez en un minuto, dos veces en un momento pero ninguno en cien años?',
             'Si me dejas caer, seguro que me parto. Dame una sonrisa, y siempre te devolveré otra. ¿Qué soy?',
             'Hablo sin boca y oigo sin oídos. No tengo cuerpo, pero cobro vida con el viento. ¿Qué soy?',
             'Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?']

preguntas_random = choice(preguntas)

print(preguntas_random)

respuestas = input("La respuesta es: ")

if preguntas_random == "¿Qué se encuentra una vez en un minuto, dos veces en un momento pero ninguno en cien años?" and respuestas == "La letra m":
  print('Correcto')

elif preguntas_random == "Si me dejas caer, seguro que me parto.  una sonrisa, y siempre te devolveré otra. ¿Qué soy?" and respuestas == "Un espejo":
  print('Correcto')

elif preguntas_random == "Hablo sin boca y oigo sin oídos. No tengo cuerpo, pero cobro vida con el viento. ¿Qué soy?" and respuestas == "El eco":
  print('Correcto')

elif preguntas_random == "Tengo ciudades, pero no casas. Tengo montañas, pero no árboles. Tengo agua, pero no peces. ¿Qué soy?" and respuestas == "Un mapa":
  print('Correcto')