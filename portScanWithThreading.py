import socket
import threading
import sys
from datetime import datetime

args = sys.argv

fst_port = int(args[2])
lst_port = int(args[3])
target = args[1]

threads = []
p = []
isopen = []

start = datetime.now()

def Scanner(port, i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = s.connect_ex((target, port))

    if res == 0:
        isopen[i] = 1

count = 0
for port in range(fst_port, lst_port):
    p.append(port)
    isopen.append(0)
    thread = threading.Thread(target=Scanner, args=(port, count))
    thread.start()
    threads.append(thread)
    count = count + 1

for i in range(len(threads)):
    threads[i].join()
    if isopen[i] == 1:
        print('port %d open :)' % p[i])
end = datetime.now()
total_time = end - start

print('Endgame :)')
print('Total Scan Duration: ' + str(total_time))
