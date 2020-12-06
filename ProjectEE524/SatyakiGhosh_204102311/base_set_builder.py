import os
import time
import random
import resource
import numpy as np

from extract import extract_anns, extract_data
from constants import NUM_CHOSEN_PATIENTS, NUM_SEG_CHOSEN_PER_PATIENT, TRAIN_DATA_PATH, TRAIN_ANN_PATH


start = time.time()

class Dataset():
  def __init__(self, num_patients):

    self.num_patients = num_patients
    self.data_path = TRAIN_DATA_PATH
    self.ann_path = TRAIN_ANN_PATH
    self.patient_list = sorted(os.listdir(self.data_path))
    self.data_list = []                                 #list for trainset
    self.segs_global = []
    self.stats = []

  #@profile
  def extract_random_segments_for_given_patient(self, patient_no, num_segs_chosen_per_patient):   #helper

    current_patient = self.patient_list[patient_no]  
    patient_ann = current_patient[:-4] + '-nsrr.xml'
    ann, onset, duration = extract_anns(self.ann_path + patient_ann)
    preprocess = None  #getting un-preprocessed segments
    eeg_dict, stat = extract_data(self.data_path + current_patient, ann, onset, duration[-1], preprocess=preprocess, return_stats=True)
    self.stats.append(stat)

    len_dict = {}
    for i in eeg_dict.keys(): 
      len_dict[i] = len(eeg_dict[i])

    selected_tuples = []
    labels = []
    tuples = []    #all (label, segment)

    for label in [1]:
      for seg in range(len_dict[label]): 
        selected_tuples.append((int(label), eeg_dict[label][seg]))
        labels.append(label)

    for label in [0,2,3,4]:
      for seg in range(len_dict[label]): 
        tuples.append((int(label), eeg_dict[label][seg]))

    random.shuffle(tuples)

    for _ in range(num_segs_chosen_per_patient-len(selected_tuples)):
      t = tuples.pop()
      selected_tuples.append(t)
      labels.append(t[0])

    del tuples

    self.segs_global.extend(labels)
    self.data_list.extend(selected_tuples)
    del selected_tuples


  #@profile
  def create(self, num_segs_chosen_per_patient):      #main
  
    for p in range(self.num_patients): 
      if (p+1)%20==0:
        print(f"patient_no: {p+1}")
        print(f"Time taken so far: {time.time()-start} seconds")
        print(f"segs: {np.unique(self.segs_global, return_counts=True)}")
        print(f"RAM: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024} MB")
        print("\n")

      self.extract_random_segments_for_given_patient(patient_no=p, num_segs_chosen_per_patient=num_segs_chosen_per_patient)
    

data_set = Dataset(num_patients=NUM_CHOSEN_PATIENTS)  
data_set.create(num_segs_chosen_per_patient=NUM_SEG_CHOSEN_PER_PATIENT)
np.save(f"/content/drive/MyDrive/ML_lab_mini_project/data_set.npy", data_set.data_list)
np.save(f"/content/drive/MyDrive/ML_lab_mini_project/stats.npy", data_set.stats)

print(f"Total time: {time.time()-start} seconds")