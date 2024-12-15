# pip install pysound
import time
from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the alarm date and time in 24 hour format (Hour(00-23):Minute(00-59):Second(00-59)): ")
task = input(f"Enter task to do at{alarm_time}: ")
print(f"You will be alarmed at {alarm_time}.")

# Step 3: Check the time continuously
while True:
    current_time = datetime.now()
    
    if current_time == alarm_time:
        print(f"Time to {task}")
        
        playsound("alarm_clock\\mixkit-morning-clock-alarm-1003.wav")
        break
    
    time.sleep(1)
