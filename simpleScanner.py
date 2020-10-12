import socket
import sys
from datetime import datetime


args = sys.argv

fst_port = int(args[2])
lst_port = int(args[3])
target = args[1]
start = datetime.now()
try:
    print('Knock knock:)')
    for port in range(fst_port, lst_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = s.connect_ex((target, port))
        s.close()

        if res == 0:
            print('port %d is open:)' %(port))

    end = datetime.now()
    total_time = end - start
  
    print('Endgame:)')
    print("Total scan time Duration: " + str(total_time))

except KeyboardInterrupt:
    print('KeyboardInterrput.')
