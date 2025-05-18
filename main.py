import pywhatkit
import time
from datetime import datetime

def send_whatsapp_message(phone_number: str, message: str, hours: int, minutes: int):
    try:
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        # Create the full phone number with country code
        full_number = f"+{phone_number}"
        
        # Wait time in seconds (default to 15 seconds to give time to load WhatsApp Web)
        wait_time = 15
        
        # Send message at specified time
        pywhatkit.sendwhatmsg(full_number, message, hours, minutes, wait_time, True)
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    print("Welcome to WhatsApp Message Automation!")
    print("--------------------------------------")
    
    while True:
        # Get user input
        phone_number = input("\nEnter phone number (with country code, e.g., 911234567890)\nor 'q' to quit: ")
        
        if phone_number.lower() == 'q':
            print("Thank you for using WhatsApp Automation. Goodbye!")
            break
        
        message = input("Enter your message: ")
        
        # Get time input
        while True:
            try:
                hours = int(input("Enter the hour (24-hour format, 0-23): "))
                if 0 <= hours <= 23:
                    break
                print("Please enter a valid hour between 0 and 23")
            except ValueError:
                print("Please enter a valid number")
        
        while True:
            try:
                minutes = int(input("Enter the minutes (0-59): "))
                if 0 <= minutes <= 59:
                    break
                print("Please enter valid minutes between 0 and 59")
            except ValueError:
                print("Please enter a valid number")
        
        print("\nInitiating WhatsApp Web...")
        print(f"Message will be sent at {hours:02d}:{minutes:02d}")
        
        # Send the message
        if send_whatsapp_message(phone_number, message, hours, minutes):
            print("\nMessage has been scheduled successfully!")
        else:
            print("\nFailed to schedule message. Please try again.")
        
        time.sleep(2)  # Give some time to read the status

if __name__ == "__main__":
    main()
