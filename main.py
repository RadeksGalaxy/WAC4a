import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

class clovek:
    def __init__(self, jmeno, plave, kamos, trida):
        """
        Konstruktor pro cloveka.
        """
        self.kamos = kamos
        self.jmeno = jmeno
        self.plave = plave
        self.trida = trida

    def validace(self):
        """
        Kontrola pro ulozeni cloveka. Jestli splnuje vse co ma.
        """
        if self.plave == 0:
            return False
        if len(self.jmeno) < 2 or len(self.jmeno) > 20:
            return False
        if len(self.trida) < 0 or len(self.jmeno) > 5:
            return False
        if len(self.kamos) == 0:
            return True
        elif len(self.kamos) > 2 and len(self.kamos) < 20:
            return True
        else:
            return False


"""
Automaticke nacteni lidi co maji byt v tabulce.
"""
lidi = []
f = open("friends.txt", "r")
for line in f:
    data = line.split(',')
    c = clovek(data[0], data[1], data[2], data[3])
    lidi.append(c)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Nacteni uvodni strany.
    """
    return render_template('index.html', muzici=lidi), 200


@app.route('/registrace', methods=['GET', 'POST'])
def registrace():
    """
    Nacteni strany pro registraci.
    """
    return render_template('registrace.html'), 200


@app.route('/restapi/odeslano', methods=['GET', 'POST'])
def odesli():
    if request.method == "POST":
        qtc_data = request.get_json()
        cetnost = False
        c = clovek(str(qtc_data["jmeno"]), int(qtc_data["plave"]), str(qtc_data["kamarad"]), str(qtc_data["trida"]))
        for a in lidi:
            if str(qtc_data["jmeno"]) == a.jmeno:
                cetnost = True

        if cetnost:
            results = {'processed': 'Nezapsan'}
        else:
            if c.validace():
                f = open("friends.txt", "a")
                f.write(str(qtc_data["jmeno"]) + "," + str(qtc_data["plave"]) + "," + str(qtc_data["kamarad"]) + "," + str(qtc_data["trida"])+ "\n")
                f.close()
                lidi.append(c)
                results = {'processed': 'Zapsano'}
            else:
                results = {'processed': 'Nezapsan'}

    return jsonify(results)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
