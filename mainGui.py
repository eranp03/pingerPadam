from PyQt5 import uic
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
import os
import logging
from PyQt5.QtWidgets import *
from collections import Counter
import subprocess
import threading
import time
import sys

class Second(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("addHostgui.ui", self)

        self.show()



class UI(QMainWindow):

    def closeEvent(self, event):
        os._exit(1)
    def getFilterByDivision(companyNames):
        dups = Counter(companyNames) - Counter(set(companyNames))
        return list(dups.keys())
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("pingerGui162.ui", self)


        #self.setStyleSheet("background-image : url(wallpaper.png); color: white" )

        def just(self):
            global sleep
            sleep = 60
            set_time = cbT.currentText()
            if set_time == "15 Minutes":
                sleep = 15 * 60
            elif set_time == "30 Minutes":
                sleep = 30 * 60
            elif set_time == "60 Minutes":
                sleep = 60 * 60
            elif set_time == "90 Minutes":
                sleep = 90 * 60
            elif set_time == "Minute":
                sleep =60
            elif set_time == "30 Seconds":
                sleep =30
            else:
                pass


        #gui Buttons
        pingByTimeBTN = self.findChild(QPushButton, "pingTimeBTN")
        #gui lables
        lable = self.findChild(QLabel,"lastTime")
        self.setWindowFlags(QWidget().windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(QWidget().windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)
        lable.setText("Wating for ping")
        pingByTimeBTN.clicked.connect(just)


        # Row count
        self.tableWidget.setRowCount(1)

        # Column count
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setStyleSheet("background-image : url(serversWallpapaer.png) background-size: 200px auto;")


        #titles
        #self.tableWidget.setItem(0, 0, QTableWidgetItem("Value"))
        '''
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Company name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Company type"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Server role"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("IP Address"))
        '''

        self.tableWidget.setHorizontalHeaderLabels(['Company name', 'Company Type', 'Server role', 'IP Address'])

        #bold titles
        myFont = QtGui.QFont()
        myFont.setBold(True)

        ''' self.tableWidget.item(0,0).setFont(myFont)
        self.tableWidget.item(0, 1).setFont(myFont)
        self.tableWidget.item(0, 2).setFont(myFont)
        self.tableWidget.item(0, 3).setFont(myFont)
        '''




        #get data from the tableInfo file
        companyNames = []
        companyServers = []
        companyTypes = []
        hosts = []
        alive = []
        dead = []
        filter_host = []
        linesInfo = []

        fu = open('tableInfo.txt', 'r', encoding='utf-8')
        for line in fu:
            linesInfo.append(line)
        length = len(linesInfo)

        #put the data in different arrays
        for i in range(length):
            companyNames.append(linesInfo[i].split(',')[0])
            companyServers.append(linesInfo[i].split(',')[1])
            companyTypes.append(linesInfo[i].split(',')[2])
            hosts.append(linesInfo[i].split(',')[3])
        line = 0


        dups = Counter(companyNames) - Counter(set(companyNames))
        companyNamesFilter = list(dups.keys())

        for host in range(len(hosts)):
            a = hosts[host].split('\n')[0]
            filter_host.append(a)
        #print(filter_host)
        self.tableWidget.setRowCount(len(hosts))

        #put the data on the gui Table
        for j in range(length) :
            self.tableWidget.setItem(line, 0, QTableWidgetItem(companyNames[j]))
            self.tableWidget.setItem(line, 1, QTableWidgetItem(companyServers[j]))
            self.tableWidget.setItem(line, 2, QTableWidgetItem(companyTypes[j]))
            self.tableWidget.setItem(line, 3, QTableWidgetItem(filter_host[j]))
            line+=1

        self.tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)


        def send_ping():
            line =0
            while True:
                try:
                    #print("sleep on", str(sleep))
                    time.sleep(sleep)
                except:
                    time.sleep(1)

                for host in range(len(filter_host)):

                    p = subprocess.Popen('ping -n 2 ' + self.tableWidget.item(line, 3).text(), stdout=subprocess.PIPE)
                    # the stdout=subprocess.PIPE will hide the output of the ping command
                    p.wait()
                    if p.poll():
                        #print(filter_host[host] + " is down")
                        dead.append(filter_host[host])
                        self.tableWidget.item(line, 3).setBackground(QtGui.QColor(255, 114, 110))
                        self.tableWidget.viewport().update()
                        line+=1

                    else:
                        #print(filter_host[host] + " is up")
                        #color 51, 255, 51
                        self.tableWidget.item(line, 3).setBackground(QtGui.QColor(143, 220, 113))
                        self.tableWidget.viewport().update()
                        line += 1
                        alive.append(filter_host[host])


                lable.setText(now)
                dupsA = Counter(alive) - Counter(set(alive))
                dupsD = Counter(dead) - Counter(set(dead))
                global alivesFilter,deadsFilter
                alivesFilter = list(dupsA.keys())
                deadsFilter = list(dupsD.keys())
                #print(" Alives: ", alivesFilter)
                #print(" Dead: ", deadsFilter)

                if line == len(filter_host):
                    line = 0
                    t = time.localtime()
                    nowlP = time.strftime("%H:%M:%S", t)
                    lable.setText("Last Time Ping: " + " " + nowlP)
                else:
                    pass

                #print("line is: ", line)

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
                        logfile.write(companyNames[host - 1] + "," + companyServers[host - 1] + "," + nowTime + "," + filter_host[host - 1] + " Was Down" + "\n")
                        logfile.close()
                    else:
                        logfile = open('logPing.txt', 'a', encoding='utf-8')
                        logfile.write(companyNames[host - 1] + "," + companyServers[host - 1] + "," + nowTime + "," + filter_host[host - 1] + " Was up" + "\n")
                        logfile.close()
                time.sleep(1800)


        t1 = threading.Thread(target=send_ping)
        t1.start()
        t2 =threading.Thread(target=pingToLog)
        t2.start()

        #FilterByDivision
        cb = self.findChild(QComboBox, "comboBoxF")
        cb.addItems(companyNamesFilter)

        cbT = self.findChild(QComboBox, "comboBoxTime")
        cbT.addItem("30 Seconds")
        cbT.addItem("Minute")
        cbT.addItem("15 Minutes")
        cbT.addItem("30 Minutes")
        cbT.addItem("60 Minutes")
        cbT.addItem("90 Minutes")


        #self.tableWidget.item(2, 3).setBackground(QtGui.QColor(128, 255, 0))




        #show the gui
        self.show()


app = QApplication(sys.argv)
window = UI()
app.exec_()
