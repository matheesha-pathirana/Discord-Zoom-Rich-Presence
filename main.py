import subprocess
from pypresence import *
import time
from colored import fg, bg, attr

rpc = Presence("944039007258554379")
rpc.connect()
print("%sDiscord Rich presence has started! Created by matheesha#2006%s" % (fg(45), attr(0)))

running = False


def chrome():
    print("%sGoogle Chrome has started, connecting Rich Presence!%s" % (fg(46), attr(0)))
    rpc.update(state="Google Chrome", large_image="chrome", large_text="Browsing", start=time.time())


def dc_chrome():
    print("%sGoogle Chrome has been closed, disconnecting Rich Presence...%s" % (fg(1), attr(0)))
    rpc.clear()


def default():
    print("%sZoom has started, connecting Rich Presence!%s" % (fg(46), attr(0)))
    rpc.update(state="In a Zoom Meeting", large_image="zoom_meeting", large_text="Zoom Meetings", small_image="red_dot",
               small_text="In a Zoom Meeting", start=time.time())


def run_rpc():
    print("%sZoom has started, connecting Rich Presence!%s" % (fg(46), attr(0)))
    rpc.update(state="In a Zoom Meeting", large_image="zoom_meeting", large_text="Zoom Meetings", small_image="red_dot",
               small_text="In a Zoom Meeting", details=(topic), start=time.time())


def dc_rpc():
    print("%sZoom has been closed, disconnecting Rich Presence...%s" % (fg(1), attr(0)))
    rpc.clear()


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


while True:
    if process_exists("chrome.exe"):
        if running == False:
            chrome()
        else:
            dc_chrome()

            running = True

    else:
        if running == True:
            dc_chrome()
            running = False
        time.sleep(1)

    if process_exists("Zoom.exe") == True:
        if running == False:
            topic = input("Please Enter Your Zoom meeting Topic (To skip type 'x') :")
            if topic == 'x':
                default()
            else:
                dc_rpc()

            running = True

    else:
        if running == True:
            dc_rpc()
            running = False
    time.sleep(1)
