# Website Usage Tracker (Daily Coding Challenge)

## Overview

This project is part of a **Daily Coding Challenge** where the goal is to build a new, small project every day. For this challenge, I decided to create a simple Python application that tracks the websites you visit throughout the day. It notifies you after you reach specific thresholds, helping you stay on top of your website usage.

This application tracks which websites you are currently active on, updates regularly, and can notify you if you've spent too much time on a specific website. It's built using **Python**, with a **GUI** created with **Tkinter**.

## Features

- **Tracks websites you visit** using Chrome's / Edge's history database.
- **Displays a list of active websites** that you are currently visiting.
- **Sends notifications** based on time thresholds (optional).
- **Simple GUI** for showing active websites and stats.

## Technologies Used

- **Python** (Core Language)
- **Tkinter** (For the GUI)
- **SQLite** (To query Chrome’s History database)
- **Shutil** (To copy the Chrome history file for use in the program)
- **Time and Notifications** (For timed alerts on website usage)

## How It Works

The application queries Chrome's or Edge's **History** database file, which contains URLs of websites you’ve visited. It then extracts the most recent URLs, displaying them in a simple Tkinter window.

- **Polling Mechanism**: The program regularly checks for updates to the history file to track the websites you are active on.
- **Notifications**: You can set time thresholds (e.g., after spending X minutes on a website) to get notified.

### Key Functions

1. **Copying the History File**: Since Chrome or Edge locks its `History` file, we copy it to another location to access the data.
2. **Querying the History Database**: The program uses SQLite to query the most recent URLs from Chrome’s or Edge's `History` database.
3. **Tracking Active Websites**: It regularly checks the active websites by reading the `last_visit_time` in the `urls` table of the database.
4. **Displaying Active Websites**: The Tkinter GUI updates with the latest active websites every few seconds.

## How to Use

1. **Prerequisites**:
    - **Python**: Make sure Python is installed on your system (>= 3.7).
    - **Chrome Browser**: This program is designed to work with Chrome’s History file, so ensure you have it installed and running.

2. **Installation**:

    Clone this repository or download the code to your local machine.

    ```bash
    git clone https://github.com/yourusername/website-usage-tracker.git
    cd website-usage-tracker
    ```

3. **Install Dependencies**:

    The program requires the following Python packages:
    
    ```bash
    pip install pygetwindow sqlite3 plyer
    ```

4. **Run the Application**:

    Run the main script (`tracker.py`):

    ```bash
    python tracker.py
    ```

    Once the application starts, the **Tkinter** GUI will display a list of the most recently visited websites.

5. **Viewing the Results**:

    - The GUI will show the top websites you've visited recently.
    - The program will periodically check and refresh the data every few seconds.
    - If you stay on a website for too long, a notification will appear.

6. **Customizing Thresholds and Notifications**:

    - You can modify the code to add custom thresholds for notifications (e.g., alert after spending 30 minutes on a website).

---

## Code Walkthrough

### Main Logic:
- **`get_active_tabs()`**: Queries the Chrome History database and returns a list of the most recent URLs.
- **GUI with Tkinter**: Displays active websites in a simple, real-time window.
- **Notifications**: Tracks your usage over time and sends a notification if you exceed a set time threshold (e.g., after 30 minutes on the same website).


## Roadmap for Future Improvements

1. **Browser Extension**: Integrate with a Chrome Extension to track active tabs in real-time (without relying on the History database).
2. **Notifications**: Enhance the notification system to send more customized alerts.
3. **Cross-browser Support**: Extend the functionality to support Firefox, Safari, etc.
4. **Dashboard**: Create a web-based dashboard for tracking your website usage over time (e.g., weekly stats).
5. **Data Persistence**: Store website visit data in a local database for analysis over time.

---

## Conclusion

This project was created as part of my **Daily Coding Challenge**, where I aimed to build a new small project every day. The **Website Usage Tracker** is a simple but effective tool for tracking how much time you spend on different websites.

Feel free to fork the repo and make improvements, or use it to track your own website usage!

---

## License

This project is licensed under the MIT License.
