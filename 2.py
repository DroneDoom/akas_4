import time
import random
from multiprocessing import Process
print('открытие файла')
text=open('text.txt','r')
text=text.readlines()
def create_file(n):
    kol=random.randrange(100,10000)
    file=open(('file'+str(n)+'.txt'),'a+')
    for i in range(kol):
        line=random.randrange(1,41)
        file.write(text[(line)])
    file.close()
start=time.time()
for i in range(100):
    create_file(18+i)
end=time.time()
print(end-start)
print('процессы: ')
kol_p=int(input())
a=[]
for i in range(5):
    p = Process(target=create_file, args=(i+1,))
    a.append(p)
    p.start()
start=time.time()
[multiprocessing.join() for multiprocessing in a]
end=time.time()
print(end-start)
