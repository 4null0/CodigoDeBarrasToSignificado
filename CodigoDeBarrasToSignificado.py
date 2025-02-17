#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyzbar.pyzbar import decode
from PIL import Image
import argparse

miParser = argparse.ArgumentParser ()

miParser.add_argument('-o', '--origen', metavar="FICHERO ORIGEN", help="Fichero con contiene el código de barras", required=True, type=str)

args = miParser.parse_args()
#Decodificamos la imagen pasada.
Resultado = decode(Image.open(args.origen))

#El resultado es realmente una lista, por lo que se pasa a formato: sstring
#para su tratamiento.
Cadena = "".join(map(str,Resultado))

#Extraemos el significado del código de barras, para lo cuál debemos
#leer exclusivamente el contenido del campo: data

#Extraemos la posición del primer carácter '
inicio = Cadena.find ('\'')
#Extraemos la posición del segundo carácter '
fin = Cadena.find ('\'',14)
#Mostramos el contenido del campo: data
print "\n[+]El código de barras significa: "+Cadena[inicio+1:fin]+"\n"

