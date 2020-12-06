from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

from constants import NUM_SLEEP_STAGES


def describe(df: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df.mean().rename('mean'),
                      df.median().rename('median'),
                      df.max().rename('max'),
                      df.min().rename('min')
                     ], axis=1).T

                     
def out_std(s, nstd=3.0, return_thresholds=False):
    """
    Return a boolean mask of outliers for a series
    using standard deviation, works column-wise.
    param nstd:
        Set number of standard deviations from the mean
        to consider an outlier
    :type nstd: ``float``
    param return_thresholds:
        True returns the lower and upper bounds, good for plotting.
        False returns the masked array 
    :type return_thresholds: ``bool``
    """
    data_mean, data_std = s.mean(), s.std()
    cut_off = data_std * nstd
    lower, upper = data_mean - cut_off, data_mean + cut_off
    if return_thresholds:
        return lower, upper
    else:
        return [True if x < lower or x > upper else False for x in s]


def out_iqr(s, k=1.5, return_thresholds=False):
    """
    Return a boolean mask of outliers for a series
    using interquartile range, works column-wise.
    param k:
        some cutoff to multiply by the iqr
    :type k: ``float``
    param return_thresholds:
        True returns the lower and upper bounds, good for plotting.
        False returns the masked array 
    :type return_thresholds: ``bool``
    """
    # calculate interquartile range
    q25, q75 = np.percentile(s, 25), np.percentile(s, 75)
    iqr = q75 - q25
    # calculate the outlier cutoff
    cut_off = iqr * k
    lower, upper = q25 - cut_off, q75 + cut_off
    if return_thresholds:
        return lower, upper
    else: # identify outliers
        return [True if x < lower or x > upper else False for x in s]


def remove_nan(df: pd.DataFrame) -> pd.DataFrame:

  if df.isnull().values.any():
    print(f'Data not OK, removing nan values..')
    print()
    nan_values = []
    indices = list(np.arange(df.shape[1]))
    for j in range(df.shape[1]):
      nan_values.append(df[j].isnull().sum().sum())
    
    print(f'Before:')
    print(f"Indices:    {indices}")      #index of feature   
    print(f"NaN values: {nan_values}")   #number of nan values corresponding to each feature
    print()

    df = df.fillna(df.median())  #replacing nan with median

    nan_values = []
    indices = list(np.arange(df.shape[1]))
    for j in range(df.shape[1]):
      nan_values.append(df[j].isnull().sum().sum())

    print(f'After:')
    print(f"Indices:    {indices}")        #index of feature
    print(f"NaN values: {nan_values}")     #number of nan values corresponding to each feature
    print()

  else:
    print(f"Data has no NaN values")
  
  return df


#@profile
from math import pi
def correntropy(x, y, preprocessing='standardize'):
    #N = len(x)
    X = preprocess(x, preprocessing)
    Y = preprocess(y, preprocessing)
    sigma = np.std(X, axis=0)*6
    #print(f"std dev: {s}")
    V = (1/(np.sqrt(2*pi*sigma)))*np.exp(-0.5*np.square(X - Y)/sigma**2)
    #CIP = 0.0 # mean in feature space should be subtracted!!
    #for i in range(0, N):
        #CIP += np.average(np.exp(-0.5*(x- y[i])**2/s**2))/N
    return V


#@profile
def get_sums(W,inv):
  path = '/content/drive/My Drive/Cross-spectrum-EEG/datasets/matrix_masks/'

  if inv==True:  
    row_mask = np.load(path + 'row_mask_6_inverse.npy', allow_pickle=True)  #mask matrices have fixed shape for same scale and time i.shape/j.shape=(263,3750)
    column_mask = np.load(path + 'column_mask_6_inverse.npy', allow_pickle=True) 
  else: 
    row_mask = np.load(path + 'row_mask_6.npy', allow_pickle=True)  #mask matrices have fixed shape for same scale and time i.shape/j.shape=(263,3750)
    column_mask = np.load(path + 'column_mask_6.npy', allow_pickle=True) 

  accum = np.multiply(W, row_mask+1)
  accum = np.sum(accum)
  accum_2 = np.multiply(W, np.multiply(row_mask+1, column_mask+1))
  accum_2 = np.sum(accum_2)

  accum_sq = np.multiply(W, (row_mask+1)**2)
  accum_sq = np.sum(accum_sq)
  accum_sq_2 = np.multiply(W, np.multiply((row_mask+1)**2, (column_mask+1)**2))
  accum_sq_2 = np.sum(accum_sq_2)
  
  return accum, accum_sq, accum_2, accum_sq_2


#@profile
def get_sums2(total_scales, total_time, W):

  ones = np.ones((total_scales, total_time))
  x = np.arange(total_scales).reshape(-1, 1)
  y = np.arange(total_time).reshape(1,-1)
  i = np.multiply(ones, x).astype(int)
  j = np.multiply(ones, y).astype(int)
  accum = np.multiply(W, np.multiply(i, j))  #kind of masking
  accum = np.sum(accum)
  accum_sq = np.multiply(W, np.multiply(i**2, j**2))
  accum_sq = np.sum(accum_sq)
  
  return accum, accum_sq


def get_len_dict(eeg_dict):  
  len_dict = {}
  for i in eeg_dict.keys():
    len_dict[i] = len(eeg_dict[i])
  print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in len_dict.items()) + "}")


def split_dataset(data_dict: dict) -> [np.ndarray, list]:
  """
  data_dict -> labelwise dict of (selected_seg_label, avg feature_vector of ref_label: selected_seg X ref_seg)
  """
  X_0, X_1, X_2, X_3, X_4 = ([] for _ in range(NUM_SLEEP_STAGES)) #initializing 5 empty strings
  X = [X_0, X_1, X_2, X_3, X_4]
  
  #features_to_keep = [0,1,2,5,6,7,9,13,16,18,19,20,21,25,26,27,28,29,30,31]
  # features_to_keep = list(range(17))+list(range(24,32))
  # features_to_delete = []
  # for i in range(32):
  #   if i not in features_to_keep:
  #     features_to_delete.append(i) 

  # print(f"Features kept: {features_to_keep}")

  for i in range(NUM_SLEEP_STAGES):
    for tup in data_dict[i]:  
      #x = np.delete(tup[1], 8)
      x = tup[1]       #uncomment if nothing to delete
      X[i].append(x) 

  Y = []
  clf_id = np.random.randint(NUM_SLEEP_STAGES) #emphasizing that it doesn't  matter which ref label we'll use because the label of the randomly selected sample will be same for all keys in the dict
  for tup in data_dict[clf_id]:   
    Y.append(tup[0]) 

  return np.array(X), Y         #(num_sleep_stages, total_samples, num_features), num_samples


def split_datalist(data_list1: np.ndarray, clf_id1: int, data_list2: np.ndarray, clf_id2: int) -> [np.ndarray, np.ndarray]:    
  """
  data_list -> list of (selected_seg_label, avg feature_vector of ref_label: selected_seg X ref_seg)
  clf_id -> signifies which SVM this data is meant for
  """
  # print(f"clf_id:{clf_id}")

  X1 = np.array(list(data_list1[:, 1]))
  X1 = np.stack([x for x in X1])
  Y1 = np.array(data_list1[:, 0]).astype('int')

  X2 = np.array(list(data_list2[:, 1]))
  X2 = np.stack([x for x in X2])
  Y2 = np.array(data_list2[:, 0]).astype('int')

  X = np.concatenate((X1,X2), axis=1)
  assert np.all(Y1==Y2) 
  Y = Y1    #can be Y2 as well

  pos_indices0 = np.where((Y != clf_id1) & (Y != clf_id2))[0]
  pos_indices1 = np.where(Y == clf_id1)[0]
  pos_indices2 = np.where(Y == clf_id2)[0]

  Y[np.where((Y != clf_id1) & (Y != clf_id2))[0].tolist()] = -1 #none

  assert np.all(np.where(Y == -1)[0] == pos_indices0)
  assert np.all(np.where(Y == clf_id1)[0] == pos_indices1)
  assert np.all(np.where(Y == clf_id2)[0] == pos_indices2)
  
  return X, Y                #(total_samples, num_featues), (total_samples,) 


#used for training and in correntropy calculation
#@profile
def preprocess(X: np.ndarray, preprocessing: str) -> np.ndarray:

  if preprocessing=="standardize":
    m = np.mean(X, axis=0)
    s = np.std(X, axis=0)
    data = (X - m)/s
  
  if preprocessing=="normalize":
    mx = np.max(X, axis=0)
    mn = np.min(X, axis=0)
    data = (X - mn)/(mx - mn)

  return data               #(total_samples, num_featues)


def preprocess_test(X: np.ndarray, preprocessing: str) -> np.ndarray:
  
  if preprocessing=="standardize":
    m = np.mean(X, axis=1)[:,np.newaxis, :]
    s = np.std(X, axis=1)[:,np.newaxis, :]
    data = (X - m)/s
  
  if preprocessing=="normalize":
    mx = np.max(X, axis=1)[:,np.newaxis, :]
    mn = np.min(X, axis=1)[:,np.newaxis, :]
    data = (X - mn)/(mx - mn)

  return data                   #(num_sleep_stages, total_samples, num_features)


def downsample(x,n):
  l=np.shape(x)[0]
  seg=[]
  #print(f'shape of original seg {np.shape(x)}')  # = 3750
  for i in range(l):
    if i%n==0:
      seg.append(x[i])
  return np.array(seg)

