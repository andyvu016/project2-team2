import pandas as pd
import numpy as np
from pathlib import Path
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import json
import joblib

def predict_dementia(data):
    # Load the model
    model_file_path = Path("../Resources/2017-2021 NHAMCS Data/nn_opt_model.h5")

    # Load the model to a new object
    nn_imported = tf.keras.models.load_model(model_file_path)

    # Load the empty prediction
    prediction_file_path = Path("../Resources/2017-2021 NHAMCS Data/predict.json")

    # Load the empty prediction to a dictionary
    with open(prediction_file_path) as predict_json:
        predict_dict = json.load(predict_json)

    # Load the diagnostic icd dictionary
    icd_file_path = Path("../Resources/2017-2021 NHAMCS Data/inv_diag.json")

    # Load the diagnostic icd dictionary to a dictionary
    with open(icd_file_path) as icd_json:
        icd_dict = json.load(icd_json)

    # Load the Standard Scaler
    scaler_file_path = Path("../Resources/2017-2021 NHAMCS Data/nhamcs_scaler.bin")

    # Load the NHAMCS Standard Scaler
    nhamcs_scaler =  joblib.load(scaler_file_path) 

    # Parse user input into prediction dictionary
    predict_dict["AGE"] = data["age"]

    if data["sex"] == "Male":
        predict_dict["SEX_MALE"] = 1
        predict_dict["SEX_FEMALE"] = 0
    else:
        predict_dict["SEX_FEMALE"] = 1
        predict_dict["SEX_MALE"] = 0

    if data["ethnicity"] == "Hispanic or Latino":
        predict_dict["ETHIM_Hispanic or Latino"] = 1
    else:
        predict_dict["ETHIM_Not Hispanic or Latino"] = 1

    if data["race"] == "White Only":
        predict_dict["RACEUN_White Only"] = 1
    elif data["race"] == "Black/African American Only":
        predict_dict["RACEUN_Black/African American Only"] = 1
    elif data["race"] == "Asian Only":
        predict_dict["RACEUN_Asian Only"] = 1
    elif data["race"] == "Native Hawaiian/Oth Pac Isl Only":
        predict_dict["RACEUN_Native Hawaiian/Oth Pac Isl Only"] = 1
    elif data["race"] == "American Indian/Alaska Native Only":
        predict_dict["RACEUN_American Indian/Alaska Native Only"] = 1
    else:
        predict_dict["RACEUN_nan"] = 1

    if data["alcohol"] == "Yes":
        predict_dict["ETOHAB"] = 1
    else:
        predict_dict["ETOHAB"] = 0

    if data["asthma"] == "Yes":
        predict_dict["ASTHMA"] = 1
    else:
        predict_dict["ASTHMA"] = 0

    if data["cancer"] == "Yes":
        predict_dict["CANCER"] = 1
    else:
        predict_dict["CANCER"] = 0
    
    if data["cvatia"] == "Yes":
        predict_dict["CEBVD"] = 1
    else:
        predict_dict["CEBVD"] = 0
    
    if data["ckd"] == "Yes":
        predict_dict["CKD"] = 1
    else:
        predict_dict["CKD"] = 0

    if data["copd"] == "Yes":
        predict_dict["COPD"] = 1
    else:
        predict_dict["COPD"] = 0
        
    if data["chf"] == "Yes":
        predict_dict["CHF"] = 1
    else:
        predict_dict["CHF"] = 0
    
    if data["cad"] == "Yes":
        predict_dict["CAD"] = 1
    else:
        predict_dict["CAD"] = 0

    if data["depress"] == "Yes":
        predict_dict["DEPRN"] = 1
    else:
        predict_dict["DEPRN"] = 0
    
    if data["diabetes1"] == "Yes":
        predict_dict["DIABTYP1"] = 1
    else:
        predict_dict["DIABTYP1"] = 0

    if data["diabetes2"] == "Yes":
        predict_dict["DIABTYP2"] = 1
    else:
        predict_dict["DIABTYP2"] = 0

    if data["diabetes0"] == "Yes":
        predict_dict["DIABTYP0"] = 1
    else:
        predict_dict["DIABTYP0"] = 0

    if data["esrd"] == "Yes":
        predict_dict["ESRD"] = 1
    else:
        predict_dict["ESRD"] = 0

    if data["hpe"] == "Yes":
        predict_dict["HPE"] = 1
    else:
        predict_dict["HPE"] = 0

    if data["hiv"] == "Yes":
        predict_dict["EDHIV"] = 1
    else:
        predict_dict["EDHIV"] = 0
    
    if data["hyplipid"] == "Yes":
        predict_dict["HYPLIPID"] = 1
    else:
        predict_dict["HYPLIPID"] = 0

    if data["htn"] == "Yes":
        predict_dict["HTN"] = 1
    else:
        predict_dict["HTN"] = 0

    if data["obesity"] == "Yes":
        predict_dict["OBESITY"] = 1
    else:
        predict_dict["OBESITY"] = 0

    if data["osa"] == "Yes":
        predict_dict["OSA"] = 1
    else:
        predict_dict["OSA"] = 0

    if data["ostprsis"] == "Yes":
        predict_dict["OSTPRSIS"] = 1
    else:
        predict_dict["OSTPRSIS"] = 0

    if data["substab"] == "Yes":
        predict_dict["SUBSTAB"] = 1
    else:
        predict_dict["SUBSTAB"] = 0

    if data["othercon"] == "Yes":
        predict_dict["NOCHRON"] = 1
    else:
        predict_dict["NOCHRON"] = 0

    for i in data["diag"]:
        icd = icd_dict[i]
        if icd in predict_dict.keys():
            predict_dict[icd] = 1
        else:
            pass

    # Turn the prediction dictionary to a DataFrame
    predict_df = pd.DataFrame(predict_dict, index = [0])

    # Apply the Standard Scaler to the prediction DataFrame
    predict_scaled = nhamcs_scaler.transform(predict_df)

    # Make the prediction using the model
    prediction = nn_imported.predict(predict_scaled)

    # Return the prediction
    return prediction[0,0]
