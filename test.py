import subprocess
import threading
import time
from collections import Counter
linesInfo = []
alive = []
dead = []
hosts = []
filter_host = []
fu = open('tableInfo.txt', 'r', encoding='utf-8')
for line in fu:
    linesInfo.append(line)
length = len(linesInfo)

#put the data in different arrays
for i in range(length):
    hosts.append(linesInfo[i].split(',')[3])
for host in range(len(hosts)):
    a = hosts[host].split('\n')[0]
    filter_host.append(a)

print(filter_host)
lengthH = len(filter_host)
def send_ping():
    while True:
        for host in range(lengthH):
            try:
                x = subprocess.check_output(["ping", "-c", "1", filter_host[host]], stderr=subprocess.STDOUT, universal_newlines=True)
                alive.append(filter_host[host])
            except:
                dead.append(filter_host[host])
        time.sleep(60)


def deadalive():
    alivesFilter = []
    deadsFilter = []

    while True:

        time.sleep(60)


t = threading.Thread(target=send_ping)
t1 = threading.Thread(target=deadalive)
t.start()
t1.start()