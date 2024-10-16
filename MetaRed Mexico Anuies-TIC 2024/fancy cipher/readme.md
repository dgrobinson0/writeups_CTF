# Reto - Fancy Cipher

Este reto consiste en aplicar técnicas de criptografía para encontrar la flag.

El reto contaba con la siguiente descripción: *Cesar no es el único que puede crear buenos cifrados, el mío es más elegante*, además se adjuntaba un fichero **fancy-cipher.py** que contenía el siguiente código:
```
from hidden import flag, shift

def encode(data, shift):
	enc = ''
	for _ in data:
		enc += chr((ord(_)+shift) % 0xff)
	return enc

assert encode(flag, shift) == '-3(.4?B,5*9@7;065&0:&:6&-(5*@D'
```

Al analizar el código encontramos aspectos interesantes:
- El fichero contaba con dos elementos importantes ocultos: **flag** y **shift**.
- La función **encode** toma una cadena (data) y un valor de desplazamiento (shift), y para cada carácter, convierte su valor ASCII con ord(_), le suma el valor shift y luego aplica mod 255 para mantener el resultado dentro de un rango de valores ASCII.
- La cadena cifrada que da el código es **'-3(.4?B,5*9@7;065&0:&:6&-(5*@D'**, y sabemos que si logramos decodificarlo correctamente, obtendremos la flag.

Para descifrar la cadena, invertimos el proceso de cifrado, deduciendo **shift** a partir del texto cifrado dado y aplicando un desplazamiento inverso. Para ello creamos un script que probara diferentes valores de shift y descifrara la cadena:
```
ciphertext = '-3(.4?B,5*9@7;065&0:&:6&-(5*@D'

def decode(data, shift):
    dec = ''
    for _ in data:
        dec += chr((ord(_) - shift) % 0xff)
    return dec

for shift in range(256):
    decoded = decode(ciphertext, shift)
    print(f"Shift: {shift} -> {decoded}")
```

Al correr el script obtenemos la flag del reto buscando de manera visual en el output mostrado en la consola.

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/reto1-1.png" /> </p>

**Flag del reto:** ```flagmx{encryption_is_so_fancy}```
