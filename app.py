import sklearn
from flask import Flask, render_template, request
from model import load, prediksi
import pickle
app = Flask(__name__)

# load model dan scaler
load()

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict#project", methods=["POST"])
def predict():

    penyakit1 = int(request.form['penyakit1'])
    penyakit2 = int(request.form['penyakit2'])

    # if penyakit1 == penyakit2:
    #     print("Penyakit Sama! Silahkan Masukan Penyakit ulang")
    # else:
        
    data_baru = [[penyakit1, penyakit2]]
    prediction_result= prediksi(data_baru)
    # prediction_result = int(prediction_result)
    return render_template('index.html', hasil_prediksi=prediction_result)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)