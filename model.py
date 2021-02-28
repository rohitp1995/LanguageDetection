import pandas as pd
import numpy as np
from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation
import pickle
from sklearn.feature_extraction.text import *
import warnings
warnings.filterwarnings("ignore")


with open('Char2Gram_nb.pkl', 'rb') as f:
    model = pickle.load(f)
      
with open('Char2Gram_features.pkl', 'rb') as c:
    columns = pickle.load(c)  
    
with open('vector.pkl', 'rb') as f:
    vector = pickle.load(f)
      


def languagePrediction(Sentence):
    features=vector.transform([Sentence])
    array=features.toarray()
    user_input=pd.DataFrame(array,columns=columns)
    lang_dict={0:'Arabic',1:'Chinese',2:'Dutch',3:'English',4:'Estonian',5:'French',6:'Hindi',7:'Indonesian',8:'Japanese',9:'Korean',10:'Latin',11:'Persian',12:'Portugese',13:'Pushto',14:'Romanian',15:'Russian',16:'Spanish',17:'Swedish',18:'Tamil',19:'Thai',20:'Turkish',21:'Urdu'}
    language = model.predict(user_input)  
    Language=pd.Series(language).map(lang_dict)
    return Language.values


