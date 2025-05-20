import pywhatkit
import time

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
        phone_number = input("\nEnter phone number (with country code, e.g., 923129185825)\nor 'q' to quit: ")
        
        if phone_number.lower() == 'q':
            print("Thank you for using WhatsApp Automation. Goodbye!")
            break
        
        message = input("Enter your message: ")
        

        while True:
            try:
                time_input = input("Enter the time (e.g., 3:30 PM or 15:30): ").strip().upper()
                # Check if time is in 12-hour format with AM/PM
                if "AM" in time_input or "PM" in time_input:
                    # Split time and meridian
                    time_part = time_input.replace("AM", "").replace("PM", "").strip()
                    meridian = "AM" if "AM" in time_input else "PM"
                    
                    # Split hours and minutes
                    if ":" in time_part:
                        hours, minutes = map(int, time_part.split(":"))
                    else:
                        hours = int(time_part)
                        minutes = 0
                    
                    # Validate hours
                    if not (1 <= hours <= 12):
                        print("Please enter a valid hour between 1 and 12")
                        continue
                    
                    # Convert to 24-hour format
                    if meridian == "PM" and hours != 12:
                        hours += 12
                    elif meridian == "AM" and hours == 12:
                        hours = 0
                else:
                    # Assume 24-hour format
                    if ":" in time_input:
                        hours, minutes = map(int, time_input.split(":"))
                    else:
                        hours = int(time_input)
                        minutes = 0
                    
                    if not (0 <= hours <= 23):
                        print("Please enter a valid hour between 0 and 23")
                        continue
                
                # Validate minutes
                if not (0 <= minutes <= 59):
                    print("Please enter valid minutes between 0 and 59")
                    continue
                
                break
            except ValueError:
                print("Please enter a valid time format (e.g., 3:30 PM or 15:30)")
        
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
