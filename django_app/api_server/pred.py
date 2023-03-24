import joblib

pm25_model = joblib.load('../pkl_file/pm25.pkl')
NO_model = joblib.load("../pkl_file/no.pkl")
NO2_model = joblib.load("../pkl_file/no2.pkl")
NOx_model = joblib.load("../pkl_file/nox.pkl")
Nh3_model = joblib.load("../pkl_file/nh3.pkl")
CO_model = joblib.load("../pkl_file/co.pkl")
SO2_model = joblib.load("../pkl_file/so2.pkl")
O3_model = joblib.load("../pkl_file/o3.pkl")
random_forest_model = joblib.load('../pkl_file/random_forest_model.pkl')

def predict_aqi(date):
    # PM2.5,NO,NO2,NOx,NH3,CO,SO2,O3,AQI
    val1 = pm25_model.predict([[date]])
    val2 = NO_model.predict([[date]])
    val3 = NO2_model.predict([[date]])
    val4 = NOx_model.predict([[date]])
    val5 = Nh3_model.predict([[date]])
    val6 = CO_model.predict([[date]])
    val7 = SO2_model.predict([[date]])
    val8 = O3_model.predict([[date]])
    prediction_array = []
    prediction_array.append(val1[0])
    prediction_array.append(val2[0])
    prediction_array.append(val3[0])
    prediction_array.append(val4[0])
    prediction_array.append(val5[0])
    prediction_array.append(val6[0])
    prediction_array.append(val7[0])
    prediction_array.append(val8[0])
    print()
    # print([val1[0],val2[0],val3[0],val4[0],val5[0],val6[0],val7[0]])
    aqi = random_forest_model.predict([prediction_array])
    return int(aqi[0])

#448
# print(predict_aqi(20230319))
