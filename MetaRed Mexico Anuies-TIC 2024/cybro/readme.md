# Reto - Cybro

Este reto consiste en aplicar técnicas OSINT para encontrar la flag.

El reto contaba con la siguiente descripción: Hola, soy Cybro tu asistente de ciberseguridad, diseñado para ayudarte a explorar y aprender sobre este entorno. https://www.facebook.com/profile.php?id=61565721302958

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoCybro-1.png" /> </p>

Primeramente analizamos el perfil de facebook que se nos proporcionó y encontramos 2 cosas claves:
- En la información del perfil se identifica a la cuenta de Facebook de Telegram como una cuenta que le gusta a Cybro Xander.
- En el comentario de la actualización de la foto de perfil de la cuenta se muesta un mensaje interesante: ```This is for you: HIENXDVCOXFS```

Luego accedemos a Telegram y buscamos por el nombre de Cybro Xander y encontramos un bot de Telegram que coincide con el nombre proporcionado y con la foto de perfil de Facebook. Este bot contenía las funcionalidades de:
- tip: Security tip of the day
- tools: Getting to know security tools
- alerts: Stay informed about the latest vulnerabilities
- challenge: This is for you

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoCybro-2.png" /> </p>

Nótese que la funcionalidad challenge contiene como descripción el mismo mensaje que el comentario de la foto de perfil de Facebook de Cybro Xander. Al acceder a esta funcionalidad nos devuelve el siguiente mensaje:
```
This is for you: mtetja{rkhe_hqizs_ybdmpg_xsv_kmjrkgn} 
 Will you be able to solve the hidden message?
```

Nos piden que obtengamos el mensaje oculto que hay en: **mtetja{rkhe_hqizs_ybdmpg_xsv_kmjrkgn}**. Esta cadena contiene el formato de la flag del reto por tanto se deduce que pudiera estar cifrado con algún tipo de cifrado de sustitución.

Utilizamos la herramienta online **dcode** para identificar el tipo de cifrado que contiene la cadena y obtenemos que es posible que se halla usado el cifrado Vigenère. Este cifrado utiliza una llave para cifrar y decifrar.

URL herramienta: ```https://www.dcode.fr/identificador-cifrado```
<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoCybro-3.png" /> </p>

Utilizamos la herramienta online **CyberChef** para encontrar la flag proporcionando como llave la cadena que encontramos en el comentario de Facebook: **HIENXDVCOXFS**

URL herramienta: ```https://cyberchef.org/```
<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoCybro-4.png" /> </p>

**Flag del reto:** ```flagmx{with_cybro_learns_and_defends}```
