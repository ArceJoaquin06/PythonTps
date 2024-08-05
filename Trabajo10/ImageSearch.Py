import cv2 as cv

img = cv.imread('Image_B&W.jpg', cv.IMREAD_GRAYSCALE)

def busqueda_en_imagen(image, tono):
   for lista in range(image):
      for j in range(lista):
          if lista[j] == tono:
             return "Las cordenadas son (" + lista + "," + j + ")"
          
busqueda_en_imagen()