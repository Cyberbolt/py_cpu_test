import os
import time
import pickle
import hashlib
import platform
import multiprocessing


class Test:
    def __init__(self):
        arr = None # 此处的数据集在 source.dict 中，数据类型: list[float]
        self.arr = arr
    
    def bubbleSort(self, arr: list):
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def multi_bubbleSort(self, arr: list):
        ps = []
        for i in range(256):
            p = multiprocessing.Process(target=self.bubbleSort, args=(arr,))
            ps.append(p)
        
        start2 = time.time()
        for p in ps:
            p.start()
        for p in ps:
            p.join()
        end2 = time.time()
        
        spend2 = end2 - start2
        self.score2 = int(70000 / spend2)
        print('多核成绩: {}'.format(self.score2))

    def run(self):
        arr = self.arr[:25000]
        
        print('正在测试单核性能')
        start1 = time.time()
        self.bubbleSort(arr)
        end1 = time.time()
        spend1 = end1 - start1
        self.score1 = int(10000 / spend1)
        print('单核成绩: {}'.format(self.score1))
        
        print('正在测试多核性能')
        self.multi_bubbleSort(arr[:5000])


def main():
    with open('data.dict', 'rb') as f:
        data = pickle.load(f)
    
    test = data['obj']
    test.run()
    

if __name__ == '__main__':
    main()