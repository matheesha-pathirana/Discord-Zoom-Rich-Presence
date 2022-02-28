import tkinter as tk
import tkinter.font as tkFont
import subprocess
from pypresence import *
import time
from colored import fg, bg, attr

rpc = Presence("944039007258554379")
rpc.connect()

running = False



def run_rpc():
       rpc.update(state="In a Zoom Meeting", large_image="zoom_meeting", large_text="Zoom Meetings", small_image="red_dot",
               small_text="In a Zoom Meeting", start=time.time())

def dc_rpc():
    rpc.clear()


# if process_exists("Zoom.exe") == True:
#     if running == False:
#         run_rpc()
#     else:
#         dc_rpc()
#
#         running = True
# else:
#     if running == True:
#         dc_rpc()
#         running = False
# time.sleep(1)
#

def close():
    exit()

class App:
    def __init__(self, root):
        #setting title
        root.title("Discord Zoom RPC")
        #setting window size
        width=577
        height=309
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_746=tk.Label(root)
        ft = tkFont.Font(family='segoe ui',size=38)
        GLabel_746["font"] = ft
        GLabel_746["fg"] = "#333333"
        GLabel_746["justify"] = "center"
        GLabel_746["text"] = "Discord Zoom RPC"
        GLabel_746.place(x=10,y=10,width=566,height=96)

        GButton_688=tk.Button(root)
        GButton_688["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='segoe ui',size=18)
        GButton_688["font"] = ft
        GButton_688["fg"] = "#000000"
        GButton_688["justify"] = "center"
        GButton_688["text"] = "Start RPC"
        GButton_688.place(x=70,y=160,width=150,height=60)
        GButton_688["command"] = self.GButton_688_command

        GButton_47=tk.Button(root)
        GButton_47["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='segoe ui',size=18)
        GButton_47["font"] = ft
        GButton_47["fg"] = "#000000"
        GButton_47["justify"] = "center"
        GButton_47["text"] = "Stop RPC"
        GButton_47.place(x=350,y=160,width=150,height=60)
        GButton_47["command"] = self.GButton_47_command

        GButton_364=tk.Button(root)
        GButton_364["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='segoe ui',size=16)
        GButton_364["font"] = ft
        GButton_364["fg"] = "#000000"
        GButton_364["justify"] = "center"
        GButton_364["text"] = "Exit"
        GButton_364.place(x=240,y=240,width=95,height=48)
        GButton_364["command"] = self.GButton_364_command

    def GButton_688_command(self):
        run_rpc()

    def GButton_47_command(self):
        dc_rpc()


    def GButton_364_command(self):
        close()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
