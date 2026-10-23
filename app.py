from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/calculate", methods=['POST'])
def calculate():
    units = int(request.form['units'])
    bill = units * 5
    if units <= 100:
        message = 'GREAT ! YOU ARE A GOOD SAVER'
    elif units <= 200:
        message = 'TRY SAVING MORE !'
    else:
        message = 'YOU ARE A SON OF RICH FATHER !HUH!'
    return render_template('index.html', message=message, units=units,bill=bill)

if __name__ == '__main__':
    app.run(debug=True)       