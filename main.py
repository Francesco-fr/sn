from http.client import HTTPException
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def sn():
    return render_template("sn.html")


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    return render_template("error.html", ), 500


@app.route("/result/<name>", methods=['GET'])
def result(name):
    if request.method == 'GET':
        found: str = "Aucun résultat trouvé"

        if name == "aire":
            width = float(request.args['width'])
            length = float(request.args['length'])
            found = str(f"A=L*l soit A={width}*{length}={width * length}")
        elif name == "pui":
            u = float(request.args['u'])
            i = float(request.args['i'])
            found = str(f"P=UxI soit P={u}*{i}={u*i} Watts")

        return render_template("sn.html", resultinfo=found)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
