from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',navn='Louis',alder=17,favorittspråk='norsk',skole='kuben',poeng=50)

@app.route('/profil')
def profil():
    return 'louis'

@app.route('/kontakt')
def kontakt():
    return 'kontakt oss'

@app.route('/prosjekter')
def pros():
    return 'dette er mitt prosjekt'

@app.route('/om')
def om():
    return render_template('om.html')

@app.route('/spill')
def spill():
    spillliste=['deadlock','terraria','umamusume','nubbys number factory','disco elysium']
    return render_template('spill.html',spill=spillliste)

@app.route("/registrering", methods=["GET", "POST"])
def registrering():
    
    if request.method == "POST":
        navn = request.form["navn"]
        favfag = request.form["favfag"]
        epost = request.form["epost"]
        kommentar = request.form["kommentar"]
        alder= request.form["alder"]
        return render_template("resultat.html", navn=navn, favfag=favfag,epost=epost,kom=kommentar,alder=alder)
    return render_template("registrering.html")

@app.route('/kurs')
def kurs():
    kursliste = ["Python", "Flask", "JavaScript", "Linux",'gdscript']
    return render_template('kurs.html',kursliste=kursliste)
    kurs= request.form["kurs"]
    

if __name__ == '__main__':
    app.run(debug=True)