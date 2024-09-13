![image](https://github.com/user-attachments/assets/572ba377-41d2-4eab-926d-14731b4d32bb)# Reto 5 - Mr. Robot
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

Listamos el contenido del fichero 
