import pickle 
def main():
    file_name = "pipeline_v1.bin"
    with open(file_name,'rb') as file:
        dv,model = pickle.load(file)

    request_test = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0}



    X = dv.transform([request_test])
    pred = model.predict_proba(X)[0,1]
    print("pred is +", pred)

if __name__ == "__main__":
    main()
