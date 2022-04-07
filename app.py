import os
import time
import pickle
import hashlib
import platform
import multiprocessing


if platform.system() == 'Windows':
    source_path = 'source_win.dict'
    data_path = 'data_win.dict'
else:
    source_path = 'source.dict'
    data_path = 'data.dict'

with open(source_path, 'rb') as f:
    source = pickle.load(f)['source']

loc = locals()
exec('{}'.format(source))
Signature = loc['Signature']
Test = loc['Test']


def main():
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    
    test = data['obj']
    test.run()
    

if __name__ == '__main__':
    main()