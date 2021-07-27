import pickle

loaded_model = pickle.load(open('dib.pkl','rb'))
pred = loaded_model.predict([[10,35,2,43,5,24,63,43]])
if(pred[0]):
    print('Person has diabetes')
else:
    print('Person is non-diabetic')