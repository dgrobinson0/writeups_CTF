from flask import Flask, request, render_template
import datetime, sqlite3, random, pyotp, sys

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
