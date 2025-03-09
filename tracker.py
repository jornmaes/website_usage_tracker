import tkinter as tk
import threading
import time
from plyer import notification
import pygetwindow as gw
import sqlite3
import os
#import win32com.client
import shutil
import re


def copy_history_file(browser):
    if browser == "chrome":
        history_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
        history_copy_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History_copy")
    elif browser == "edge": #this "profile 4" won't be universal
        history_path = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile 4\\History")
        history_copy_path = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile 4\\History_copy")

    try:
        shutil.copy(history_path, history_copy_path)
        #print(f"copied to {history_copy_path}")
    except Exception as e:
        print(f"Error copying history file: {e}")

    return history_copy_path




def get_active_tab(browser):

    history_copy_path = copy_history_file(browser)
    
    conn = sqlite3.connect(history_copy_path)
    cursor = conn.cursor()

    #now we query the "urls" from the file to get the most recent visited urls
    query = """
    SELECT url FROM urls
    ORDER BY last_visit_time DESC LIMIT 1;
    """

    cursor.execute(query)
    result = cursor.fetchone()

    #use regex to extract the domain name from the title -> will likely not work
    match = re.search(r"([a-zA-Z0-9-]+\.[a-zA-Z]+)", result[0])

    if match:
        return match[0]
    return None

"""
def get_active_window():
    #get the active website
    active_window = gw.getActiveWindow()
    if active_window:
        title = active_window.title
        
        #use regex to extract the domain name from the title -> will likely not work
        match = re.search(r"([a-zA-Z0-9-]+\.[a-zA-Z]+)", title)
        if match:
            return match.group(0)
    return None"
"""


class WebsiteTrackerApp:
    def __init__(self, root):
        self.root = root
        #set the window the same size as the full window
        #self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")

        self.root.geometry(f"1000x600")

        self.root.title("Website Usage Tracker")
        self.website_usage = {} #to track the website usage and time spent -> put in CSV file later for storage

        #label to display the currect active website and time
        self.label = tk.Label(root, text="No activity yet", font=("Arial", 16))
        self.label.pack(pady = 10) #adjust later

        #listbox to show the visited websites and time spent
        self.listbox = tk.Listbox(root, height=10, width=100) #adjust
        self.listbox.pack(pady = 10) #adjust

        #button to start tracking
        self.start_button = tk.Button(root, text = "Start Tracking" , command=self.start_tracking, bg = "green")
        self.start_button.pack(pady = 10) #adjust

        
    def start_tracking(self):
        #this function starts the tracking in a seperate thread so the UI doesn't completely freeze
        threading.Thread(target = self.track_websites, daemon= True).start() #we make it a daemon thread so we don't have to worry about stopping it



    def update_display(self):
        #clear the listbox and update it with new website usage data
        self.listbox.delete(0, tk.END)
        for website, time_spent in self.website_usage.items():
            self.listbox.insert(tk.END, f"{website}: {time_spent//3600} hours and {time_spent//60} minutes and {time_spent%60} seconds") #add the amount of seconds that the website has been open on the listbox
        

    def track_websites(self):
        #this function will update the website tracker
        while True:
            website = get_active_tab("edge") #function that will return the website in use
            if website not in self.website_usage:
                self.website_usage[website] = 0 #if not yet registered than make a new entry in the dict
            self.website_usage[website] += 1 #increase the second counter
            self.update_display() # good idea to do this so often?

            #now check if the time spent on the website is above a threshold where we should send a notification
            if self.website_usage[website] > 10: #just for testing
                self.send_notification(website, self.website_usage[website]) #send a notif using the website and time spent (not that necessary to add)

            time.sleep(1)

    def send_notification(self, website, time_spent):
        #use plyer to show a notif to the user that they have spent a certain amount of time on a website
        notification.notify(
            title= f"Time Alert for {website}",
            message= f"You have been on {website} for {time_spent:.2f} seconds!",
            timeout = 10 
        )



#make the window
if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteTrackerApp(root)
    root.mainloop()























