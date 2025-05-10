from flask import, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    datos = {
        'usuarios': 120,
        'ventanas': 4520,
        'visitas': 3080
    }´
    return render_template('dashboard.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
    