import cv2 #procesar imágenes y videos
import os #modulo para usar funciones dependientes del sistema operativo

def cambiarTamaño(archivo, tamaño):
  ruta=os.path.join("img entrada", archivo) #obtener la ruta de la img
  imgOriginal=cv2.imread(ruta) #guardar la imagen o leerla

  alto, ancho, canales=imgOriginal.shape #obtener las dimensiones de la img (alto y ancho)
  print(f"Tamaño original: {alto}x{ancho}")

  nuevaImg=cv2.resize(imgOriginal,tamaño) #cambiar el tamaño de la img
  alto2,ancho2=nuevaImg.shape[:2]#obtener las dimensiones de la img modificada (alto y ancho)
  print(f"Nuevo tamaño: {alto2}x{ancho2}")

  nombreImg=f"img salida/{nombreSinExtension}.jpg" #Se selecciona la ruta y nombre de la imagen
  cv2.imwrite(nombreImg,nuevaImg) #se guarda la imagen


ancho=512
alto=512
archivos = os.listdir("img entrada") #guardar todos los archivos de la carpeta img entrada
print(archivos)

for archivo in archivos:
   if archivo.endswith(".jpg"): #si termina en .jpg
    nombreSinExtension, extension = os.path.splitext(archivo) #separe el nombre del archivo de la extension
    cambiarTamaño(archivo, (ancho, alto))