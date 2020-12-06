import os
import time
import random
import numpy as np

from features import feature_gen
from constants import NUM_SEG_CHOSEN_PER_PATIENT, NUM_CHOSEN_PATIENTS, DJ

start = time.time()


class TrainSetBuilder:
  
  #@profile
  def __init__(self): 

    self.base_dataset = np.load('/content/drive/MyDrive/ML_lab_mini_project/data_set.npy', allow_pickle=True)
    print(f"Base dataset loaded in {time.time()-start} seconds")
    
    self.trainset_list = []                                 #list for trainset

  #@profile
  def generate_features(self, selected_tuple, mean, std):

    selected_label = selected_tuple[0]
    selected_segment = selected_tuple[1]
    s1 = np.array(selected_segment)

    try:
      F = feature_gen(s1, mean, std)
    except Warning:
      print("Warning encountered..")
      print("*************************")
      return

    #print(np.mean(F_avg, axis=0).shape)
    self.trainset_list.append((selected_label, F))
    #np.save(f"/content/drive/MyDrive/ML_lab_mini_project/train_data.npy", train_set.trainset_list)


  #@profile
  def create(self):      #main
    stats = np.load('/content/drive/MyDrive/ML_lab_mini_project/stats.npy', allow_pickle=True)
    mean = stats[0, 2]
    std =  stats[0, 3]
    for i, selected_tuple in enumerate(self.base_dataset):
      self.generate_features(selected_tuple, mean, std)    
      if (i+1)%NUM_SEG_CHOSEN_PER_PATIENT==0:
        p = (i+1)//NUM_SEG_CHOSEN_PER_PATIENT

        if p==NUM_CHOSEN_PATIENTS: break

        mean = stats[p, 2]
        std =  stats[p, 3]
        print(f"{i+1}: Time taken so far is {time.time()-start} seconds")

    print(f"{i+1}: Time taken so far is {time.time()-start} seconds")
#************************************************************************************************************


train_set = TrainSetBuilder()  
train_set.create()
np.save(f"/content/drive/MyDrive/ML_lab_mini_project/train_test_data.npy", train_set.trainset_list)