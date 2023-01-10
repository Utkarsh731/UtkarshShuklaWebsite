from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/poetry")
def poetry_page():
    return render_template('poetry.html')

if __name__=='__main__':
    app.run(debug=True)