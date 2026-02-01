from flask import Flask, render_template_string
import random

app = Flask(__name__)

foods = {
    "proteine": [
        {"codice": "63710", "nome": "Antipasto di mare", "prezzo": 6.88},
        {"codice": "63607", "nome": "Cotolette di pollo", "prezzo": 20.69},
        {"codice": "63889", "nome": "Merluzzo con verdure", "prezzo": 4.72},
        {"codice": "63896", "nome": "Merluzzo con patate", "prezzo": 4.72},
        {"codice": "63654", "nome": "Petto di pollo grigliato", "prezzo": 4.62},
        {"codice": "63711", "nome": "Polipo e patate", "prezzo": 7.05},
        {"codice": "63779", "nome": "Polpette di carne", "prezzo": 4.52},
        {"codice": "63835", "nome": "Polpette di mare", "prezzo": 4.13},
        {"codice": "63816", "nome": "Polpettone con patate", "prezzo": 4.62},
        {"codice": "63761", "nome": "Spezzatino di carne", "prezzo": 4.28},
        {"codice": "63778", "nome": "Scaloppine di pollo", "prezzo": 4.13},
        {"codice": "63778", "nome": "Seppie con piselli", "prezzo": 4.81},
        {"codice": "63750", "nome": "Spiedini di pesce", "prezzo": 3.05}
    ],
    "primi": [
        {"codice": "63833", "nome": "Cannelloni di carne", "prezzo": 3.93},
        {"codice": "63864", "nome": "Cous cous di verdure", "prezzo": 3.54},
        {"codice": "63735", "nome": "Insalata di riso", "prezzo": 3.54},
        {"codice": "63791", "nome": "Lasagne al ragù", "prezzo": 3.83},
        {"codice": "63789", "nome": "Penne al pomodoro", "prezzo": 3.34},
        {"codice": "63766", "nome": "Penne all’amatriciana", "prezzo": 3.73},
        {"codice": "63765", "nome": "Penne all’arrabbiata", "prezzo": 3.34},
        {"codice": "63767", "nome": "Polenta al ragù", "prezzo": 3.64},
        {"codice": "63715", "nome": "Strozzapreti al pesto", "prezzo": 3.79},
        {"codice": "63790", "nome": "Strozzapreti gamberi e zucchine", "prezzo": 4.13},
        {"codice": "63764", "nome": "Tagliatelle al ragù", "prezzo": 3.83},
        {"codice": "63820", "nome": "Tagliolini alla marinara", "prezzo": 4.32},
        {"codice": "63716", "nome": "Tagliolino allo scoglio", "prezzo": 4.33},
        {"codice": "63770", "nome": "Tortellini al ragù", "prezzo": 3.83},
        {"codice": "63771", "nome": "Tortellini boscaiola", "prezzo": 3.83},
        {"codice": "63857", "nome": "Tortelloni verdi alla norcina", "prezzo": 4.13}
    ],
    "verdure_mix": [
        {"codice": "63861", "nome": "Crema patate e ceci", "prezzo": 3.64},
        {"codice": "63883", "nome": "Fagiolini e patate", "prezzo": 2.75},
        {"codice": "63757", "nome": "Fagiolini sconditi", "prezzo": 2.75},
        {"codice": "63893", "nome": "Fricò di verdure", "prezzo": 2.75},
        {"codice": "63652", "nome": "Mozzarelline fritte", "prezzo": 3.44},
        {"codice": "63894", "nome": "Olive marchigiane", "prezzo": 3.44},
        {"codice": "63851", "nome": "Parmigiana di melanzane", "prezzo": 3.73},
        {"codice": "63850", "nome": "Parmigiana di zucchine", "prezzo": 3.73},
        {"codice": "63879", "nome": "Patate al forno", "prezzo": 2.46},
        {"codice": "63884", "nome": "Patate prezzemolate", "prezzo": 2.46},
        {"codice": "63843", "nome": "Polpettine melanzane e provola", "prezzo": 3.93},
        {"codice": "63898", "nome": "Spinaci cotti", "prezzo": 2.36},
        {"codice": "63891", "nome": "Tris di verdure", "prezzo": 2.75},
        {"codice": "63885", "nome": "Zucchine grigliate", "prezzo": 2.95},
        {"codice": "63860", "nome": "Vellutata di zucca", "prezzo": 3.64},
        {"codice": "63859", "nome": "Zuppa di legumi", "prezzo": 3.64},
        {"codice": "63913", "nome": "Zuppa di verdure", "prezzo": 3.64}
    ]
}

def genera_menu(foods):
    proteine = list({p['codice']: p for p in foods['proteine']}.values())
    primi = list({p['codice']: p for p in foods['primi']}.values())
    verdure = list({p['codice']: p for p in foods['verdure_mix']}.values())

    random.shuffle(proteine)
    random.shuffle(primi)
    random.shuffle(verdure)

    pasti = []
    for _ in range(12):
        p = proteine.pop() if proteine else random.choice(foods['proteine'])
        c = primi.pop() if primi else random.choice(foods['primi'])
        v = verdure.pop() if verdure else random.choice(foods['verdure_mix'])
        pasti.append([p, c, v])
    return pasti

def genera_testo_ordine(menu):
    ordine = {}
    for pasto in menu:
        for prodotto in pasto:
            codice = prodotto['codice']
            if codice not in ordine:
                ordine[codice] = prodotto
    testo = "Ciao Luca ti giro ordine B COOKING grazie!:\n\n"
    testo += f"{'Prodotto':40} {'Codice':10} {'Qty'}\n"
    testo += "-"*60 + "\n"
    for prod in ordine.values():
        testo += f"{prod['nome']:40} {prod['codice']:10} 1\n"

    return testo

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Generatore Menu Testuale</title>
    <style>
        body { font-family: monospace; padding: 20px; }
        pre { background-color: #f4f4f4; padding: 15px; border-radius: 5px; }
        button { padding: 10px 20px; font-size: 16px; margin-bottom: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Generatore Menu Testuale</h1>
    <form method="get">
        <button type="submit">Genera Menu</button>
    </form>

    {% if testo %}
    <button onclick="copiaTesto()">Copia negli appunti</button>
    <pre id="ordine">{{ testo }}</pre>

    <script>
        function copiaTesto() {
            const testo = document.getElementById('ordine').innerText;
            navigator.clipboard.writeText(testo).then(() => {
                alert('Testo copiato negli appunti!');
            });
        }
    </script>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    menu = genera_menu(foods)
    testo = genera_testo_ordine(menu)
    return render_template_string(TEMPLATE, testo=testo)

# Non serve app.run() su Vercel
