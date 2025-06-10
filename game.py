from flask import Flask, render_template, request

app = Flask(__name__)

gravitasi = {
    "Merkurius": 0.38,
    "Venus": 0.91,
    "Bumi": 1.00,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturnus": 1.06,
    "Uranus": 0.92,
    "Neptunus": 1.19,
    "Pluto": 0.06
}

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    if request.method == "POST":
        try:
            berat = float(request.form["berat"])
            planet = request.form["planet"]
            berat_di_planet = berat * gravitasi[planet]
            hasil = f"Beratmu di {planet}: {berat_di_planet:.2f} kg 🌟"
        except:
            hasil = "⚠️ Masukkan angka yang valid!"
    return render_template("index.html", hasil=hasil, planets=gravitasi.keys())

if __name__ == "__main__":
    app.run(debug=True)
