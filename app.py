import os
import time
import pickle
import hashlib
import platform
import multiprocessing


with open('source.dict', 'rb') as f:
    loc = locals()
    exec('{}'.format(pickle.load(f)['source']))
    Signature = loc['Signature']
    Test = loc['Test']


def main():
    with open('data.dict', 'rb') as f:
        data = pickle.load(f)
    
    test = data['obj']
    test.run()
    

if __name__ == '__main__':
    main()