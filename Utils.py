import os
import pickle
import pandas as pd
import numpy as np
from Config import *

class CellPhone:
    def __init__(self,Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness):
        self.Sale = Sale
        self.weight = weight
        self.resoloution = resoloution
        self.ppi = ppi
        self.cpu_core = cpu_core
        self.cpu_freq = cpu_freq
        self.internal_mem = internal_mem
        self.ram = ram
        self.RearCam = RearCam
        self.Front_Cam = Front_Cam
        self.battery = battery
        self.thickness = thickness

    def load_model(self):
        with open(MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)


    def get_predictions(self):
        try: 
            self.load_model()

            test_array = np.zeros(12,dtype=int)
            test_array[0] = self.Sale
            test_array[1] = self.weight
            test_array[2] = self.resoloution
            test_array[3] = self.ppi
            test_array[4] = self.cpu_core
            test_array[5] = self.cpu_freq
            test_array[6] = self.internal_mem
            test_array[7] = self.ram 
            test_array[8] = self.RearCam
            test_array[9] = self.Front_Cam
            test_array[10] = self.battery
            test_array[11] = self.thickness

            return self.model.predict([test_array])[0]
        except:
            return 'Error in get_predictions'



