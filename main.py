print("""
                                             .__  .__ 
____________   ____   _____             ____ |  | |__|
\___   /  _ \ /  _ \ /     \   ______ _/ ___\|  | |  |
 /    (  <_> |  <_> )  Y Y  \ /_____/ \  \___|  |_|  |
/_____ \____/ \____/|__|_|  /          \___  >____/__|
      \/                  \/               \/         

    """)


import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst, week_day
import webbrowser
import urllib.request
# print("Dit me lai hoc a!")
def printCurrentTime() :
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time = ", current_time)

keyboard = Controller()
isStarted = False
currentDay = week_day[datetime.today().weekday()]

while True:
    for i in lst:
        meeting_link = i[0]
        currentStart = i[1]
        currentEnd = i[2]
        currentMeeting = i[3]

        if currentDay != i[4]:
            continue

        while True:
            hour_now = int(datetime.now().hour)
            minute_now = int(datetime.now().minute)
            if isStarted == False:
                if hour_now > int(i[1].split(':')[0]) or hour_now == int(i[1].split(':')[0]) and minute_now >= int(i[1].split(':')[1]):
                    if hour_now < int(i[2].split(':')[0]) or hour_now == int(i[2].split(':')[0]) and minute_now < int(i[2].split(':')[1]):
                        webbrowser.open(meeting_link, autoraise=False)
                        # urllib.request.urlopen(meeting_link)
                        isStarted = True
                        print("Current Day : " + currentDay + "DAY")
                        print("Current Meeting : " + currentMeeting)
                        print("Current Meeting Start : " + currentStart)
                        print("Current Meeting End : " + currentEnd)
                        print("Meeting Started ... (" + i[3] +")\n")  
                        print()
                    else:
                        break
                else:
                    break

            else:
                if  hour_now > int(i[2].split(':')[0]) or hour_now == int(i[2].split(':')[0]) and minute_now >= int(i[2].split(':')[1]):
                    time.sleep(1)
                    isStarted = False
                    print("Meeting Ended ...(" + i[3] +")\n")
                    print()
                    break
    # i = 1
    # print(++i)
    time.sleep(30)

































