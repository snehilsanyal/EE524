# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:51:13 2020

@author: keyen
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:47:30 2020

@author: keyen
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:05:10 2020

@author: keyen
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:04:53 2020

@author: keyen
"""


import csv
import numpy
import pandas as pnd

import matplotlib.pyplot as plt


import pandas as pnd
import numpy as np
from scipy import stats
import scipy.linalg as lnA
import matplotlib.pyplot as plt
import seaborn as sn




# Normalize the dataset
## implemenation of min-max scaling

def normalized_vector(vector):
    fmax=vector.max(axis=0)
    fmin=vector.min(axis=0)

    temp1=(vector-fmin)/(fmax-fmin)


    return temp1

# Mean subtracted data

def meansubtract(data):

    mean=data.mean(axis=0)
    meansubdata=data-mean

    return meansubdata


def filereadcsv(filename):
    import csv
    from numpy import genfromtxt
    fields=[]
    rows=[]
    with open(filename, 'r') as csvfile:
        csvreader=csv.reader(csvfile)
        fields = next(csvreader)
        key=genfromtxt(filename, delimiter=',')
        for row in csvreader:
            rows.append(row)
    return key


#def preprocess_trialdata(filedir):
def trialdataprocess():

#Column names
    columnname=['Fp1', 'AF3', 'F7', 'F3', 'FC5', 'FC1', 'T7', 'C3', 'CP5', 'CP1', 'P7', 'P3', 'PO3', 'Pz', 'O1', 'Oz', 'Fp2', 'AF4', 'Fz', 'FC2', 'Cz', 'C4', 'T8', 'CP6', 'CP2', 'F4', 'F8', 'FC6', 'P4', 'P8', 'O2','PO4']
    namecol=list(zip(columnname))
    frames1 = []
    labels=[]
    stimuli=[]
    targets=[]
    eventarrays=[]
    p=0
    for j in range(1,5):
        for i in range(1,5):
    ## filenames
            stimuliname='stimuli_'+str(j)+'_'+str(i)+'.csv'
            labelname='label_'+str(j)+'_'+str(i)+'.csv'
            targetname='target_'+str(j)+'_'+str(i)+'.csv'

    ## reading to variables
            target=filereadcsv(targetname)
            stimulus=filereadcsv(stimuliname)
            label=filereadcsv(labelname)
    # define a matrix
            raweeg=pnd.read_csv("eegdata_"+str(j)+"_"+str(i)+".csv", sep=',',header=None)
            # return raweeg.

        ## Session details()
    ## Time points index
            timearray=[]
            for k in range(0,64):
                time=round(k*1000/64)
                timearray.append(str(time)+'_ms')
    ## Event index
            eventarray=[]
            for k in range(0,len(label)):
                eventarray.append('Event_'+str(k))
    ## class label
            arrays=[]
            for k in range(0,len(label)):
                temper=numpy.repeat(eventarray[k], 64, axis=0)
                temp=[temper,timearray]
                arrays.append(numpy.array(temp))

    ## Session detain variable

            tuples = list(zip(*arrays))

    #return session details



    ## Concatenated data frame with all the trials indexed from n - big n
            frames = [];
            for k in range(0, len(label)):
                results = numpy.array(raweeg.iloc[k*32:(k+1)*32])
                df_tmp = pnd.DataFrame(results.T)
                frames.append(df_tmp)
            eventarray=[]
            for u in range(0,len(label)):

                eventarray.append('Event_'+str(p))

                p=p+1

            dfd = pnd.concat(frames, axis=0)

            dfd.columns=columnname


            frames1.append(dfd)
            labels.append(label)
            stimuli.append(stimulus)
            targets.append(target)
            eventarrays.append(eventarray)

    events=[]
    for m in range(0,len(eventarrays)):
        temp=eventarrays[m];
        events.extend(temp)


    arrays=[timearray,events]
    dfg=pnd.concat(frames1,axis=0)
    dfg.reset_index(drop=True)
    ind = pnd.MultiIndex.from_product([events,timearray], names=['event', 'event_time'])
    dfdg = pnd.DataFrame(dfg.values, index=ind, columns=columnname)
    dfdg.reindex(ind)

    return dfdg, targets, stimuli, labels,eventarrays,timearray

## Preprocess data import them into a data frame with corresponding stimuli, label and event arrays
df,target,stimuli,label,eventarrays,timearray= trialdataprocess();


## Define the amplitude interval in consideration
## THe time vector, event details for analysis plotting etc
timevector=numpy.linspace(0,1000,64)
amplitudepoint= timevector[21]
ampind=21

electrodes=['Fz', 'Cz', 'Pz', 'Oz', 'P7', 'P3', 'P4', 'P8', 'O1', 'O2', 'C3', 'C4', 'FC1', 'FC2', 'CP1', 'CP2']
#channels = ['Fz', 'Cz', 'Pz', 'Oz', 'P7', 'P3', 'P4', 'P8']
channels = ['Fz','Cz']

#channelnumber=[1,2,3,4,5,6,7,8]
channelnumber=[1]

events=[]
for i in range(0,len(eventarrays)):
    temp=eventarrays[i];
    events.extend(temp)

labeled=[]
for i in range(0,len(eventarrays)):
    temp=label[i];
    labeled.extend(temp)
labels=np.array(labeled)

stimulis=[]
for i in range(0,len(eventarrays)):
    temp=stimuli[i];
    stimulis.extend(temp)
stimulus=np.array(stimulis)


## Data set preparation for running the algorithm
## Preprocessing
## Take data from all events into a matrix
## TRAINING DATA
traineeg=[]

#for i in range(0,len(df)):
#name='Event_'+str(i)

targeteeglist=[]
eventname=[]
for i in events:
    temp=df.loc[i]
    eventname.append(i)
    targeteeglist.append(temp)
targeteeglist=pnd.concat(targeteeglist,axis=0,keys=eventname)


for i in range(len(events)):
    traineeg.append(df.loc[events[i],channels])

traineeglist=pnd.concat(traineeg,axis=0,keys=eventname)
### ID two features that can represent the data
## Training data with all samples
trainfeaturevector=[]
trainmeanampvector=[]


for i in range(0,len(events)):
#    name='Event_'+str(i)
#    name=df.index[i*64][0]
#    tempmean=traineeglist.iloc[ampind-10:ampind+10].mean()
#    temp=traineeglist.iloc[ampind:ampind+1]

    name=events[i]
    tempmean=traineeglist.loc[name][ampind-10:ampind+10].mean()
    h=traineeglist.loc[name][:]
    tempamp=h.iloc[ampind]
    temp=(np.array(tempamp))

    print(i)
#for i in range(0,len(stimuli)):
#    temp=[];tempmean=[]
#    for j in channels:
#        temper=numpy.mean(traineeglist[i][j][ampind-10:ampind+10])
#        temp.append(traineeglist[i][j][ampind])
#        tempmean.append(temper)
    trainfeaturevector.append(temp)
    trainmeanampvector.append(tempmean)

traineegfeatures=numpy.vstack(trainfeaturevector)
trainmeanamp=numpy.vstack(trainmeanampvector)



##CLUSTERED DATA

##  Identify the target trials for amplitude average across trials
#indice=[]
#for i in range(0,len(label)):
#    indice.append(numpy.where(label[i]==1 ))
indice=numpy.where(labels==-1)

## indices of each of trails in the dataframe
fd=numpy.array(indice[0][:])
fdx=indice[0][:]
targeteeglist=[]
eventname=[]
for i in fd:
    temp=df.loc[events[i]]
    eventname.append(events[i])
    targeteeglist.append(temp)
targeteeglist=pnd.concat(targeteeglist,axis=0,keys=eventname)

targeteegfeaturevector=[];targeteegmeanampvector=[]
for i in fd:
#    name=[]
#    name='Event_'+str(i)
#    name=df.index[i*64][0]
    name=events[i]
    tempmean=targeteeglist.loc[name][ampind-10:ampind+10].mean()
    h=targeteeglist.loc[name][:]
    tempamp=h.iloc[ampind]
    temp=(np.array(tempamp))

    print(i*3)
#for i in range(0,len(stimuli)):
#    temp=[];tempmean=[]
#    for j in channels:
#        temper=numpy.mean(traineeglist[i][j][ampind-10:ampind+10])
#        temp.append(traineeglist[i][j][ampind])
#        tempmean.append(temper)
    targeteegfeaturevector.append(temp)
    targeteegmeanampvector.append(tempmean)

targeteegfeatures=numpy.vstack(targeteegfeaturevector)
targetmeanamp=numpy.vstack(targeteegmeanampvector)


## ID the non target trials
index=numpy.where(labels==-1)
## indices of each of trails in the dataframe
fg=numpy.array(index[0][:])
fgx=index[0][:]
nontargeteeglist=[]
noneventname=[]
for i in fgx:
    temp=df.loc[events[i]]
    noneventname.append(events[i])
    nontargeteeglist.append(temp)

nontargeteeglist=pnd.concat(nontargeteeglist,axis=0,keys=noneventname)


nontrainfeaturevector=[];nontrainmeanampvector=[]
for i in fg:
#   name='Event_'+str(i)
#    name=df.index[i*64][0]
    name=events[i]
    tempmean=nontargeteeglist.loc[name][ampind-10:ampind+10].mean()
    h=nontargeteeglist.loc[name][:]
    tempamp=h.iloc[ampind]
    temp=(np.array(tempamp))

    print(i)
#for i in range(0,len(stimuli)):
#    temp=[];tempmean=[]
#    for j in channels:
#        temper=numpy.mean(traineeglist[i][j][ampind-10:ampind+10])
#        temp.append(traineeglist[i][j][ampind])
#        tempmean.append(temper)
    nontrainfeaturevector.append(temp)
    nontrainmeanampvector.append(tempmean)

nontraineegfeatures=numpy.vstack(nontrainfeaturevector)
nontrainmeanamp=numpy.vstack(nontrainmeanampvector)


### Feature Reduction


## PCA
#array1=numpy.array(df.loc['Event_1'])
#normeeg=normalized_vector(array1)
#eeg=meansubtract(normeeg)
#covariance=covarianceMatrix(eeg)
#eigenvectors=eigenPCA(covariance)
#pcaeeg=principalComponents(eeg, eigenvectors, 2)



###### SKI LEARN SVM


import pandas as pnd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

labels[labels==-1]=0

## Q1: Load the dataset
#=pnd.read_csv("iris (1).data", sep=',', names=["SepLen","SepWid","PetLen","PetWid","Species"])
X = trainmeanamp
y = labels

# Q2: Split the dataset
#Split the dataset for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

## Q3 : Train the dataset
svclassifier = SVC(kernel='sigmoid')
svclassifier.fit(X_train, y_train)

## Q4 : Test the datset
y_pred = svclassifier.predict(X_test)

plt.figure()
## Q5: Permormance of model
print(confusion_matrix(y_test,y_pred))
sn.heatmap((confusion_matrix(y_test,y_pred)),annot=True)
## Q6 : Accuracy of the classification
print(classification_report(y_test,y_pred))


######

######
#######
##Multiclass KNN

#y=stimulus
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

#from sklearn.neighbors import KNeighborsClassifier
#knn = KNeighborsClassifier(n_neighbors = 6).fit(X_train, y_train)

# accuracy on X_test
#accuracy = knn.score(X_test, y_test)
#print(accuracy)

# creating a confusion matrix
#knn_predictions = knn.predict(X_test)
#cm = confusion_matrix(y_test, knn_predictions)
#print(cm)

#print(confusion_matrix(y_test,y_pred))
#plt.imshow(confusion_matrix(y_test,y_pred))
## Q6 : Accuracy of the classification
#print(classification_report(y_test,y_pred))

plt.figure()
plt.plot(timevector,(df.loc[events[1]].mean(axis=1)),label='Non-Trial')
plt.plot(timevector,(df.loc[events[4]].mean(axis=1)),'r',label='Trial');plt.show()
plt.legend()
plt.xlabel('Event Time length')
plt.ylabel('Amplitude')
plt.title('Averaged Amplitude of EEG acorss electrodes for single trials')




timevector=numpy.linspace(0,1000,64)
plt.figure()
ax=plt.gca()


ax1=plt.subplot(411)
plt.plot(timevector,df.loc[events[4],'Fz'],label='Fz electrode')
plt.legend()
#ax1.set_xlabel('Event Time length')
#ax1.set_ylabel('Amplitude')
#ax1.set_title('Fz')


ax2=plt.subplot(412)
plt.plot(timevector,df.loc[events[4],'Cz'],label='Cz electrode')
plt.legend()
#ax2.set_xlabel('Event Time length')
#ax2.set_ylabel('Amplitude')
#ax2.set_title('Cz')


ax3=plt.subplot(413)
plt.plot(timevector,df.loc[events[4],'Pz'],label='Pz electrode')
plt.legend()
#ax3.set_xlabel('Event Time length')
#ax3.set_ylabel('Amplitude')
#ax3.set_title('Pz')


ax4=plt.subplot(414)
plt.plot(timevector,df.loc[events[4],'Oz'],label='Oz electrode')
plt.legend()
#ax4.set_xlabel('Event Time length')
#ax4.set_ylabel('Amplitude')
#ax4.set_title('Oz')
ax4.set_xlabel('Event Time length')
ax3.set_ylabel('Amplitude')

plt.show()







# -*- coding: utf-8 -*-


import pandas as pnd
import numpy as np
import random
from scipy import stats
import seaborn as sn
import matplotlib.pyplot as plt


#Implementation of Bubble Sort function
def bubbleSort(arr):
    import copy as copy
    temp=copy.copy(arr)
    n = len(temp)
    ind = []
    for i in range(n):
        for j in range(0, n-i-1):
            if temp[j]>temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]

    for i in range(n):
        temparray=copy.copy(arr)
        #temparray=temparray.tolist()
        ind.append(temparray.index(temp[i]))

    temp=np.array(temp)
    ind=np.array(ind)
    return temp, ind


## Euclidean Distance

def euclidiandistance(vector1,vector2):
    term=[]
    for i in range(len(vector2)-1):
        temp=0
        temp=(vector1[i]-vector2[i])**2
        term.append(np.sqrt(temp))
    distance = np.sum(term)
    return distance

#nearest neighbor

#### KNN Algo
k=3
distancetoeachpoint=[]

testrecord=traineegfeatures
kneighbors=[]
neighborlabel=[]
prediction=[]
predictioncalc=[]
for i in range(0,len(traineegfeatures)):
    distancetoeachpoint=[]
    sortedarray=[]
    ind=[]

    for j in range(0,522):
        comparisondata=testrecord[j]
        if euclidiandistance(testrecord[i],comparisondata)==0.:
            continue
        else:
            distancetoeachpoint.append(euclidiandistance(testrecord[i],comparisondata))


    sortedarray,ind=bubbleSort(distancetoeachpoint)

    kneighbors.append(sortedarray[0:k])
    neighborlabel.append(labels[ind[0:k]])
    predictioncalc.append(stats.mode(neighborlabel[i]))
    prediction.append(predictioncalc[i][0][0])

correctlabel=labels


species=[0,1]
accuracy=[]
erind=[]
for i in range(0,522):
    if correctlabel[i]==prediction[i]:
        accuracy.append('correct')
    else:
        accuracy.append('incorrect')
        #erind.append()
        print(i)
        print(events[i])
        print('Sample '+str(events[i])+' is classified incorrectly' )
        print('Predicted class --> '+str(prediction[i]))
        print('But the actual class ----> '+str(correctlabel[i]))
        print('-------------------------------------------------------------')


a21=0
a31=0
a12=0
a32=0
a23=0
a13=0
a22=0
a11=0
a33=0


for i in range(0,522):

    if prediction[i]==species[0] and correctlabel[i] == species[0]:
        a11+=1
    elif prediction[i]==species[0] and correctlabel[i] == species[1]:
        a21+=1
#    elif prediction[i]==species[0] and correctlabel[i] == species[2]:
#        a31+=1

    if prediction[i]==species[1] and correctlabel[i] == species[0]:
        a12+=1
    elif prediction[i]==species[1] and correctlabel[i] == species[1]:
        a22+=1
#    elif prediction[i]==species[1] and correctlabel[i] == species[2]:
#        a32+=1

#    if prediction[i]==species[2] and correctlabel[i] == species[0]:
#        a13+=1
#    elif prediction[i]==species[2] and correctlabel[i] == species[1]:
#        a23+=1
#    elif prediction[i]==species[2] and correctlabel[i] == species[2]:
#        a33+=1

#a11=50-a21-a31
#a22=50-a12-a32
#a33=50-a13-a23


A=[[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]

A=[[a11,a12],[a21,a22]]
    
plt.figure(figsize = (10,7))
sn.heatmap(A, annot=True)

print(accuracy)


    ####### Shit downside
