import threading
import time
import random
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
create_file(9)
create_file(8)
create_file(7)
create_file(6)
end=time.time()
print(end-start)
print('потоки: ')
kol_p=int(input())
threads = []
for i in range(kol_p):
    t = threading.Thread(target=create_file, args=(i+1,))
    threads.append(t)
    t.start()
start=time.time()
[thread.join() for thread in threads]
end=time.time()
print(end-start)
