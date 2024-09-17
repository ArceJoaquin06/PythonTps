from PIL import Image
import os
import time

def busqueda_en_imagen(image_path, tono):
   with Image.open(image_path) as im:
      image = im.convert("L")
      pixeles = image.load()
      ancho, alto = image.size
      tonos = {}
      for x in range(ancho):
         for y in range(alto):
            color = pixeles[x, y]
            if color == tono:
               if color not in tonos:
                  tonos[color] = []
               tonos[color].append((x, y))
      if tonos:      
         return tonos
      else:
         return "No se encuentra este tono"

tono_buscado = int(input("Ingresa un número entero y buscaremos ese tono: "))

start_time = time.time()
rest = busqueda_en_imagen("image.jpg", tono_buscado)
finish_time = time.time()
time_rest = finish_time - start_time

print(rest)
print(f"Tiempo de ejecución: {time_rest:.4f} segundos")