import os
import subprocess 
import datetime
import time

def shutdown():
    try:
        # Add platform-specific shutdown command
        if os.name == 'posix':  # Linux or macOS
            subprocess.run(["sudo", "shutdown", "-h", "now"])
        elif os.name == 'nt':  # Windows
            subprocess.run(["shutdown", "/s", "/t", "0"], shell=True)
        else:
            print("Unsupported operating system for shutdown.")
    except Exception as e:
        print("Error occurred while shutting down the system:", e)

def sleep():
    try:
        # Add platform-specific sleep command
        if os.name == 'posix':  # Linux or macOS
            subprocess.run(["sudo", "pmset", "sleepnow"])
        else:
            print("Unsupported operating system for sleep.")
    except Exception as e:
        print("Error occurred while putting the system to sleep:", e)
        
def say_time():
    # Get current time
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    # Let's say it out loud
    print("Hey, it's currently", current_time)

def say_today():
    # Get current day and date
    current_day_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    # Let's give you the scoop
    print("Psst... Today is", current_day_date)

def check_internet(wifi_name, password):
    def is_connected():
        try:
            subprocess.check_output(["ping", "-c", "1", "google.com"])
            return True
        except subprocess.CalledProcessError:
            return False

    def enable_wifi():
        try:
            subprocess.run(["nmcli", "r", "wifi", "on"], check=True)
            time.sleep(2)  # Wait for Wi-Fi to enable
            return True
        except subprocess.CalledProcessError as e:
            print("Error enabling Wi-Fi:", e)
            return False

    def connect_wifi():
        try:
            subprocess.run(["nmcli", "device", "wifi", "connect", wifi_name, "password", password], check=True)
            time.sleep(5)  # Wait for connection to establish
            return True
        except subprocess.CalledProcessError as e:
            print("Error connecting to Wi-Fi:", e)
            return False

    if is_connected():
        print("Internet is already connected.")
        return True
    else:
        print("Internet is not connected. Attempting to connect...")
        if enable_wifi():
            if connect_wifi():
                print("Connected to Wi-Fi successfully.")
                return True
            else:
                print("Failed to connect to Wi-Fi. Please check the network credentials.")
        else:
            print("Failed to enable Wi-Fi. Please check your Wi-Fi hardware.")
    
    return False