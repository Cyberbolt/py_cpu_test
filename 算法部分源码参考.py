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
        
        for p in ps:
            p.start()
        for p in ps:
            p.join()
