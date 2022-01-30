import datetime
from playsound import playsound
# Note to install playsound use pip install playsound in the cmd or terminal ..... enjoy 

alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAm = input("am / pm: ")

if alarmAm == "pm":
    alarmHour +=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print('playing...')
        playsound('punky.mp3')
        break
        
        
#         ferel free to edit ths and update the code. 
