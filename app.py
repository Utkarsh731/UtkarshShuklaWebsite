from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)



@app.route("/poetry")
def poetry_page():
    return render_template('poetry.html')


@app.route("/")
def index_page():
    return render_template('index.html')

# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index_page'))


if __name__=='__main__':
    app.run(debug=True)
