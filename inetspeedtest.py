#!/usr/bin/python


import sys
import os
from termcolor import colored
import time
import pyspeedtest
import urllib2


os.system('clear')
file = open('logo')
print file.read()

def execute():

  while True:
       print colored("Press 0 to Exit",'yellow')
       print colored("Press 1 to Check Internet Speed",'yellow')
       print colored("Press 99 to Download",'yellow')
       main = input( colored("   :> ",'yellow'))
       if main == 1:
           os.system('clear')
           print colored("""\n
+------------+===============================================+
|     No     |                  Server List                  |
+------------+===============================================+
|      1.    |                88.84.191.230:8080             |
|      2.    |            speedtest.nornett.net:8080         |
|      3.    |        speedtest4.xj.chinamobile.com:8080     |
|      4.    |          mrm-speedtest-srv02.ti.ru:8080       |
|      5.    |           murmansk.speedtest.rt.ru:8080       |
|      6.    |               speedtest.mmsn.ru:8080          |
|      7.    |             ookla.trollfjord.no:8080          |
|      8.    |               speedtest.oltv.ru:8080          |
|      9.    |          naryan-mar.speedtest.rt.ru:8080      |
|     10.    |              speedtest.apanet.ru:8080         |
+------------+===============================================+
|     v.1    |       contact : loopstr34k@gmail.com          |
+------------+===============================================+ """,'green')

           f = open("server.lst","r")

           linelist = f.readlines()
           count = len(linelist)

           num = input("Use Server : ")
           os.system("pyspeedtest -s " + str(linelist[num]))
       if main == 99:

           url = raw_input("Using https or http\nInput Your link File : ")

           file_name = url.split('/')[-1]
           u = urllib2.urlopen(url)
           f = open(file_name, 'wb')
           meta = u.info()
           file_size = int(meta.getheaders("Content-Length")[0])
           print "Downloading: %s Bytes: %s" % (file_name, file_size)

           file_size_dl = 0
           block_sz = 8192
           while True:
              buffer = u.read(block_sz)
              if not buffer:
                   break

              file_size_dl += len(buffer)
              f.write(buffer)
              status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
              status = status + chr(8)*(len(status)+1)
              print status,
           f.close()
       if main == 0:
            os.system('clear')
            print colored("""\n\n\n
+---------------------------------------------+
|         Note                                |
+---------------------------------------------+
|                                             |
|  Thanks for using this tools                |
|  Its no a real tools                        | 
|  But its just recode from pyspeedtest       |
|  Pyspeedtest is tools from python for check |
|  Internet speed using python script         |
|                                             |
+---------------------------------------------+
|                                             |
| Recode by : Me :)                           |
|    Github : github.com/loopstr34k           |
|    Gmail  : loopstr34k@gmail.com            |
| Instagram : instagram.com/loopstr34k        |
|                                             |
+---------------------------------------------+     \n\n\n""",'green')
            time.sleep(3)
            sys.exit()

execute()

      


