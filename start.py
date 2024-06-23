from flask import Flask, render_template

app = Flask(__name__)

print('Hi')

@app.route('/')
def startup():
    return render_template('startup.html')

if __name__ == '__main__':
    app.run(debug = True)