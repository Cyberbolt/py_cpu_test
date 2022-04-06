import time
import multiprocessing

class CpuTest:
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
