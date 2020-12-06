import time
import numpy as np
import pickle
import tensorflow as tf
from sklearn.svm import SVC
from scipy.stats import mode
from itertools import combinations 
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

from sklearn.decomposition import PCA

from constants import *
from utils import *


train_test_list=np.load('/content/drive/MyDrive/ML_lab_mini_project/train_test_data.npy',allow_pickle=True)
train_test_list=np.asarray(train_test_list)
m=np.shape(train_test_list)[0]
train_size=int(0.95*m)
test_size=int(0.05*m)


#TRAINING

train_list=train_test_list[0:train_size,:]
x=train_list[:,1]
y=np.asarray(train_list[:,0])

x_train=np.ndarray((train_size,22))
for i in range(train_size):
  for j in range(22):
    x_train[i][j]=x[i][j]

x_train= x_train.astype('float32')
y_train= np.asarray(y).astype('float32')

pca_components=10
pca = PCA(n_components=pca_components)
principalComponents = pca.fit_transform(x_train-np.mean(x_train,axis=0))
#print(np.shape(principalComponents))
#print(pca.explained_variance_ratio_)
#print(pca.singular_values_)
x_train=principalComponents

mx=np.max(x_train,axis=0)
mn=np.min(x_train,axis=0)
x_train=(x_train-mn)/(mx-mn)

print('Shape of training data:')
print(np.shape(x_train))
print()
print('Shape of training labels:')
print(np.shape(y_train))
print()
print('Labels count of each class')
print(np.unique(y_train,return_counts=True))
print()
activation='sigmoid'  #relu can also be used


# Create a `Sequential` model and add a Dense layer as the first layer.
def baseline_model():
  model = tf.keras.models.Sequential()
  model.add(tf.keras.Input(shape=(pca_components)))
  model.add(tf.keras.layers.Dense(8, activation=activation))
  model.add(tf.keras.layers.Dense(16, activation=activation))
  model.add(tf.keras.layers.Dense(32, activation=activation))
  model.add(tf.keras.layers.Dense(128, activation=activation))
  model.add(tf.keras.layers.Dense(32, activation=activation))
  model.add(tf.keras.layers.Dense(16, activation=activation))
  model.add(tf.keras.layers.Dense(5,activation='softmax'))
  print('Model output shape:')
  print(model.output_shape)
  print('%%%%%%%%%%')
  #[print(i.shape, i.dtype) for i in model.inputs]
  #[print(o.shape, o.dtype) for o in model.outputs]
  #[print(l.name, l.input_shape, l.dtype) for l in model.layers]
  opt = keras.optimizers.Adam(learning_rate=0.001)  #lr can be varied 
  model.compile(optimizer=opt,
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])
                  
  return model

y_train = np_utils.to_categorical(y_train)
print('y_train (one-hot-encoded)')
print(y_train)
print()

k=10
estimator = KerasClassifier(build_fn=baseline_model, epochs=20, batch_size=5, verbose=0)
kfold = KFold(n_splits=k, shuffle=True)
results = cross_val_score(estimator, x_train, y_train, cv=kfold)
print(f'{k}-fold cross-validation results on training set:')
print("Baseline: Accuracy: %.2f%% (Standard deviation: %.2f%%)" % (results.mean()*100, results.std()*100))
print()

baseline_model().fit(x_train, y_train, epochs=20)


# TESTING


test_list=train_test_list[train_size:train_size+test_size,:]
x=test_list[:,1]
y=np.asarray(test_list[:,0])

x_test=np.ndarray((test_size,22))
for i in range(test_size):
  for j in range(22):
    x_test[i][j]=x[i][j]

x_test= x_test.astype('float32')
y_test= np.asarray(y).astype('float32')

x_test=pca.transform(x_test)

mx=np.max(x_test,axis=0)
mn=np.min(x_test,axis=0)
x_test=(x_test-mn)/(mx-mn)

print('Shape of testing data:')
print(np.shape(x_test))
print()
print('Shape of testing labels:')
print(np.shape(y_test))
print()


pred=baseline_model().predict(
    x_test, batch_size=None, verbose=0, steps=None, callbacks=None, max_queue_size=10,
    workers=1, use_multiprocessing=False
)
print('shape of prediction')
print(np.shape(np.argmax(pred,axis=1)))
print()
print('shape of given labels')
print(np.shape(y_test))
print()
print('accuracy')
print(np.mean(np.argmax(pred,axis=1)==y_test))
print()
print('predicted labels')
print(np.argmax(pred,axis=1))
print()
print('predicted probabilites')
print(pred)
print()
print('true labels')
print(y_test)
print()
test_pred=np.argmax(pred,axis=1)
test_target=y_test
print('Confusion Matrix')
print(confusion_matrix(test_target,test_pred))
print()
print('Accuracy')
print(accuracy_score(test_target,test_pred))
print()
print(classification_report(test_target, test_pred))