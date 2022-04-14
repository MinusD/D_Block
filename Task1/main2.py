import pickle
import traceback
from Task1.Hospital import *

if __name__ == '__main__':
    try:
        with open('data.pickle', 'rb') as f:
            hospital = pickle.load(f)
            doctor = pickle.load(f)
            print(hospital)
            print('========')
            print(doctor)
            print('========')
            print(hospital[99])
            print('========')
            doctor.all_patient()
            print('========')
            print(len(hospital))
            hospital + doctor
            print(len(hospital))
            print('========')
    except AssertionError:
        print("TEST ERROR")
        traceback.print_exc()
    else:
        print("TEST PASSED")
