import numpy as np
import pycwt as wavelet
from utils import get_sums, correntropy,downsample
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import kurtosis, skew, moment, trim_mean
from constants import DJ,M,STD_DEV,downsample_by


def backward_difference_operator(s,k):
  if k==0:
    return s
  return backward_difference_operator(np.diff(s),k-1)


#@profile
def feature_gen(s1,patient_mean, patient_std):    
  
  #downsampling
  s1=downsample(s1,downsample_by)
  #print(f'shape of returned seg {np.shape(s1)}') #=938
  #print(s1)

  eps=1e-3
  #time domain features
  f_t1 = np.max(s1)
  f_t2 = np.min(s1)
  f_t3 = np.mean(s1)
  f_t4 = np.std(s1)
  f_t5 = f_t1-f_t2
  f_t6 = np.percentile(s1, 25)
  f_t7 = np.percentile(s1, 50)
  f_t8 = np.percentile(s1, 75)
  f_t9 = skew(s1)
  f_t10 = kurtosis(s1)

  f_t11 = np.mean(np.absolute(s1))
  f_t12 = np.where(np.diff(np.sign( [i for i in s1 if i] )))[0].shape[0] #zero crossings
  f_t13 = np.where(np.diff(np.sign( [i for i in np.gradient(s1) if i] )))[0].shape[0] #slope sign change
  
  f_t14 = np.sum([n**2 for n in s1])/(len(s1))    #power
  f_t15 = np.sum(np.abs(s1[i+1]-s1[i])for i in range(len(s1)-1))/(len(s1)-1) #First difference
  f_t16 = f_t15/f_t4 # Normalized first difference
  f_t17 = np.sum(np.abs(s1[i+2]-s1[i])for i in range(len(s1)-2))/(len(s1)-2) #Second difference
  f_t18 = f_t17/f_t4  # Normalized second difference
  f_t19 = np.sum((s1[i]-f_t3)**2 for i in range(len(s1)))/(len(s1)) # Activity
  f_t20 = np.std(np.diff(s1))/(f_t4)  # Mobility
  f_t21 = ( np.std(np.diff(np.diff(s1))) / (np.std(np.diff(s1))+eps) )/(f_t20+eps) # Complexity    #REMOVED ONLY FOR EMG (INVALID VALUE ENCOUNTERED)
  bd = backward_difference_operator(s1,10) 
  f_t22 = np.where(np.diff(np.sign( [i for i in bd if i] )))[0].shape[0]  # Higher order crossings



  f = [f_t1,f_t2,f_t3,f_t4,f_t5,f_t6,f_t7,f_t8,f_t9,f_t10,f_t11,f_t12,f_t13,f_t14,f_t15,f_t16,f_t17,f_t18,f_t19,f_t20,f_t21,f_t22]   
  #print(len(f))
  return np.array(f)