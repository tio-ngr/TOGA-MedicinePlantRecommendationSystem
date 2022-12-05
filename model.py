import pickle

# global variable
global model,scaler

def load():
    global model, scaler
    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))

def prediksi(data_baru):
    data_baru = scaler.transform(data_baru)
    prediksi = int(model.predict(data_baru))
    if prediksi == 0:
        hasil_prediksi = 'jahe'
    elif prediksi == 1:
        hasil_prediksi = 'kunyit'
    elif prediksi == 2:
        hasil_prediksi = 'temulawak'
    elif prediksi == 3:
        hasil_prediksi = 'kencur'
    elif prediksi == 4:
        hasil_prediksi = 'sirih'
    elif prediksi == 5:
        hasil_prediksi = 'Kemangi'
    elif prediksi == 6:
        hasil_prediksi = 'sambiloto'
    elif prediksi == 7:
        hasil_prediksi = 'binahong'
    elif prediksi == 8:
        hasil_prediksi = 'temu hitam'
    elif prediksi == 9:
        hasil_prediksi = 'lidah buaya'
    elif prediksi == 10:
        hasil_prediksi = 'beluntas'
    elif prediksi == 11:
        hasil_prediksi = 'kumis kucing'
    else:
        hasil_prediksi = 'jahe'
    return hasil_prediksi
   
    