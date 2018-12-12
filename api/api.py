# encoding: utf-8
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np

import os
import re
import csv
import sys
import codecs
import pandas as pd

#from nltk.corpus import stopwords
#from nltk.stem import SnowballStemmer
from string import punctuation


from gensim.models import KeyedVectors
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Flatten, Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.models import Model,load_model
from keras.layers.normalization import BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint, Callback
from keras.layers import Bidirectional, GlobalMaxPool1D,GlobalAveragePooling1D ,Conv1D, MaxPooling1D, GRU, CuDNNGRU
from keras.optimizers import RMSprop, SGD
from keras import backend as K
from keras.engine.topology import Layer
from keras import initializers, regularizers, constraints

import textproc

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

maxlen=70
max_features=95000

app = Flask(__name__)
api = Api(app)


model_path = '../model/' 

with open(model_path+'tokenizer.pickle', 'rb') as handle:
	tokenizer = pickle.load(handle)

modelx=load_model(model_path+"model.hdf5")
modelx._make_predict_function()
print (modelx.summary())
# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

def prepare_question(question, PreProcess=False):
    global tokenizer
 
    questions=[question]
    

    if PreProcess:
        prep_questions = [text_to_wordlist(questions)]
    else:
        prep_questions = questions
   
    question_ = tokenizer.texts_to_sequences(prep_questions)

    ## Pad the sentences 
    questions_pad = pad_sequences(question_, maxlen=maxlen)

    
    return questions_pad

class PredictSentiment(Resource):
	def get(self):
		# use parser and find the user's query
		args = parser.parse_args()
		user_query = args['query']

		# vectorize the user's query and make a prediction
		tq=prepare_question(user_query)

		prediction = modelx.predict(tq, batch_size=512, verbose=1)

		# Output either 'Negative' or 'Positive' along with the score
		prediction=prediction[0,0].item()
		if (prediction>= 0.33):
				pred_text = 'Insincere'
		else:
				pred_text = 'Sincere'

		# round the predict proba value and set to new variable
		confidence = round(prediction, 3)
		# create JSON object
		output = {'prediction': pred_text, 'confidence': confidence}
		print (output)
		return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(host= '127.0.0.1',port=5001,debug=True)
