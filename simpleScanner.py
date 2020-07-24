import socket
import sys

args = sys.argv

fst_port = int(args[2])
lst_port = int(args[3])
target = args[1]

try:
    print('Knock knock:)')
    for port in range(fst_port, lst_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = s.connect_ex((target, port))
        s.close()

        if res == 0:
            print('port %d is open:)' %(port))

    print('Endgame:)')

except KeyboardInterrupt:
    print('KeyboardInterrput.')
