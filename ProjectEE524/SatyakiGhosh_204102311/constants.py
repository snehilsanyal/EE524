SLEEP_STAGES = {'Wake|0':0, 
                'Stage 1 sleep|1':1, 
                'Stage 2 sleep|2':2, 
                'Stage 3 sleep|3':3, 
                'Stage 4 sleep|4':3, 
                'REM sleep|5':4}
#SLEEP_STAGES_INV = {v: k for k, v in SLEEP_STAGES.items()}
SAMPLE_RATE = 125    #fixed for shhs1
NUM_SLEEP_STAGES = 5   #fixed
DURATION_OF_EACH_SEGMENT = 30 #seconds
downsample_by=1

TRAIN_DATA_PATH = r"/content/drive/My Drive/NSRR2/Data/train/"
TRAIN_ANN_PATH = r"/content/drive/My Drive/NSRR2/Annotations/train/"

TEST_DATA_PATH = r"/content/drive/My Drive/NSRR/Data/test/"
TEST_ANN_PATH = r"/content/drive/My Drive/NSRR/Annotations/test/"


NUM_CHOSEN_PATIENTS = 100  
NUM_SEG_CHOSEN_PER_PATIENT = 200


# MEAN AND STD DEV OF WHOLE DATASET: (PRE CALCULATED)
'''
d= np.load('/content/drive/My Drive/ML_lab_mini_project/data_set.npy', allow_pickle=True)
e=np.array(d[:,1])
np.shape(e)
signals=[]
for i in range(32000):
  signals.extend(e[i])
len(signals)
print(np.mean(signals))

M=-9.01671756535955e-07
STD_DEV=2.9249746179861722e-05
MAX=0.00012499999999999998
MIN=-0.00012401960784313724
'''