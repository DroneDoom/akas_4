import time
import threading
import urllib.request
urls = [
 'https://github.com/dashboard',
 'https://github.com/DroneDoom/NetProg',
 'https://github.com/DroneDoom',
 ]
def urlstatus(url):
    with urllib.request.urlopen(url) as u:
        return u.getcode()
threads = []
start = time.time()
for url in urls:
    t = threading.Thread(target=urlstatus, args=(url,))
    threads.append(t)
    t.start()
    print(url,urlstatus(url))
[thread.join() for thread in threads]
print(time.time() - start)
