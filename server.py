
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/lee929")
def lee929():
    return {
        "payNow": [["february 2024", 3000, "february2024"], ["january 2024", 3500, "january2024"], ["deposit", 5000, "deposit"], ["march 2024", 3000, "march2024"]],
        "log": [["july 2022", 5000, "july2022"], ["july 2022", 5000, "july2022"], ["june 2022", 5000, "june2022"]],
        "autopay": [True, "4893"]
    }




if __name__ == "__main__":
    app.run(debug=True)
