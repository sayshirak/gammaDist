from sklearn import svm
from scipy.special import gamma
import numpy as np

X = [0.7874,0.7727,0.7565,0.7376,0.7254,0.7072,0.7022,0.6808,0.6619,0.6574,0.6268,0.6116,0.5917,0.5661]
Lable = [0.0667,0.1333,0.2,0.2667,0.3333,0.4,0.4667,0.5333,0.6,0.6667,0.7333,0.8,0.8667,0.9333]

def calGammaCum():
    a = 0
    b = 0
    while a < 20:
        while b < 100:
            for i in range(len(X)):
                pass
            b += 0.01

    pass

if __name__ == '__main__':
    calGammaCum()