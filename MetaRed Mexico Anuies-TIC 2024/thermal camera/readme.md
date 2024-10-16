# Reto - Thermal Camera

El reto contaba con la siguiente descripción: El personal de seguridad del banco ha interceptado una fotografía tomada con una cámara térmica de un empleado sospechoso merodeando cerca de una caja fuerte. Se está llevando a cabo una investigación para determinar si esta persona pudo obtener el código de la caja fuerte. La investigación de El teclado de la caja fuerte revela que solo acepta códigos de cuatro dígitos. Además se adjunta la fotografía interceptada la cual se muestra a continuación:

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoThermal_camera-1.png" /> </p>

La imagen térmica contiene un patrón de colores más cálidos (naranja y rojo) en el teclado que indicaba las teclas que probablemente fueron presionadas recientemente, ya que estos colores representan las zonas de mayor temperatura.

De acuerdo a la imagen, las teclas más calientes podrían corresponder a las que fueron presionadas para ingresar el código.

- Primeramente identificamos las teclas más calientes observando las zonas de color rojo brillante: ```3570```
- Luego determinamos el orden de las pulsaciones basándonos en el criterio de que las teclas con el color más cálido podrían haber sido presionadas más recientemente: ```3750``` 
- Posteriormente enviamos la flag en el formato flagmx{XXXX}, donde XXXX representa el código de cuatro dígitos.

**Flag del reto:** ```flagmx{3750}```
