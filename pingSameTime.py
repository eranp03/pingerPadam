import subprocess,time,threading
linesInfo = []
hosts = []
filter_host = []
logDead =[]
divisions = []
unitsAll = []
commanders = []
logAlive = []

fu = open('tableInfo.txt', 'r', encoding='utf-8')
for line in fu:
    linesInfo.append(line)
for i in range(len(linesInfo)-1):
    divisions.append(linesInfo[i].split(',')[0])
    unitsAll.append(linesInfo[i].split(',')[1])
    commanders.append(linesInfo[i].split(',')[2])
    hosts.append(linesInfo[i].split(',')[3])


for host in range(len(hosts)):
    a = hosts[host].split('\n')[0]
    filter_host.append(a)

def pingToLog():
    while True:



        t = time.localtime()
        nowTime = time.strftime("%H:%M:%S", t)
        for host in range(len(filter_host) + 1):
            p = subprocess.Popen('ping -n 1 ' + filter_host[host - 1], stdout=subprocess.PIPE)
            # the stdout=subprocess.PIPE will hide the output of the ping command
            p.wait()
            if p.poll():
                # print(filter_host[host] + " is down")
                logfile = open('logPing.txt', 'a', encoding='utf-8')
                logfile.write(divisions[host-1]+ ","+ unitsAll[host-1] + ","+nowTime + ","+ filter_host[host-1] + " Was Down"+ "\n")
                print("alive")
                logfile.close()
            else:
                logfile = open('logPing.txt', 'a', encoding='utf-8')
                logfile.write(divisions[host-1] + "," + unitsAll[host-1] + "," + nowTime + "," + filter_host[host-1] + " Was up"+ "\n")
                logfile.close()
        time.sleep(30)




t = threading.Thread(target=ping)
t.start()
#print("Up Servers: ", "\n" , logAlive, "\n","Down Servers: " ,"\n"  ,logDead)
