# Reto - Details

Este reto consiste en aplicar técnicas de decoding para encontrar la flag.

El reto contaba con la siguiente descripción: Espera lo inesperado. Además se adjunta un archivo **Ciberseguridad.pptx**

Primeramente lo que hicimos fue cambiar la extensión del archivo **Ciberseguridad.pptx** a .zip y descomprimirlo para acceder a su contenido. Al descomprimirlo obtuvimos los siguientes archivos:

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoDetails-1.png" /> </p>

Revisando los directorios en busca de información, encontramos imágenes en el directorio **ppt/media/**. Sin embargo, una de las imágenes tenía el nombre de **file.png** lo cual era un poco sospechoso.

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoDetails-2.png" /> </p>

Utilizamos la herramienta **exiftool** para observar los metadatos de la imagen y obtenemos que la extensión del archivo es txt.
```
exiftool file.png
```
<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoDetails-3.png" /> </p>

Convertimos el archivo **file.png** a **file.txt** y mostramos el contenido. 
```
mv file.png file.txt
cat file.txt
```
<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoDetails-4.png" /> </p>

El contenido del fichero **file.txt** se encontraba codificado en base64. Lo decodificamos y escribimos la salida en el fichero **file_decoding.txt**
```
cat file.txt | base64 -d > file_decoding.txt
```

Posterirmente mostramos la primera línea del fichero **file_decoding.txt** y obtenemos que el fichero decodificado es una imagen.
```
cat file_decoding.txt | head -n 1
```

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoDetails-5.png" /> </p>

Convertimos el archivo **file_decoding.txt** a **imagen.png** y visualizamos la imagen. 
```
mv file_decoding.txt imagen.png
```
<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoDetails-6.png" /> </p>

**Flag del reto:** ```flagmx{the_details_are_important}```
