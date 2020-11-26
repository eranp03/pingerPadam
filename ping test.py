import subprocess,threading, time
iplist=["127.0.0.1","8.8.8.9"]

def send_ping():
    while True:
        for ip in iplist:
            p = subprocess.Popen('ping -n 1 '+ip,stdout=subprocess.PIPE)
            # the stdout=subprocess.PIPE will hide the output of the ping command
            p.wait()
            if p.poll():
                print(ip+" is down")
            else:
                print(ip+" is up")
        time.sleep(20)


t = threading.Thread(target=send_ping)
t.start()

'''
                    try:
                        x = subprocess.check_output(["ping", "-n", "1", filter_host[host]], stderr=subprocess.STDOUT, universal_newlines=True)
                        alive.append(filter_host[host])
                        self.tableWidget.item(host+1, 3).setBackground(QtGui.QColor(255,0, 0))
                    except:
                        self.tableWidget.item(host+1, 3).setBackground(QtGui.QColor(255, 0, 0))
                        dead.append(filter_host[host])

'''