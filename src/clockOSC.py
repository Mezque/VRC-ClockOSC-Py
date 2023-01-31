import time
from pythonosc.udp_client import SimpleUDPClient

CLIENT = SimpleUDPClient("127.0.0.1", 9000) #Don't touch
SLEEP = 2 #set as desired time to wait to update osc input

osc_message = ["", True] #Don't touch
def send_message():
    # Below can be set as any of the following to format time display https://docs.python.org/2/library/time.html#time.strftime
    # Where a basic "%H:%M:%S" would give you hours in 24 hour clock, Minutes followed by Second each devived by a :
    # And "%I:%M:%S %p" would result in Hours in 12 hour clock followed by Minutes:Seconds with the appropriate meridiem displayed after.
    # %I:%M:%S %p (%H:%M) in %Z is what I have mine as, [ 12H:Min:Sec meridiem (24 hour time) in TIMEZONENAME ]
    curr_time = time.strftime("%I:%M:%S %p (%H:%M) in %Z", time.localtime())
    
    print(curr_time) #debug print to make sure the time is right.
    osc_message[0] = f"{curr_time}"
    CLIENT.send_message("/chatbox/input",osc_message)
    time.sleep(SLEEP)
    send_message()
    
if __name__ == "__main__":
    send_message()
