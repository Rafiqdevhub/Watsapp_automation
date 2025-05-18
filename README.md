# WhatsApp Message Automation

A Python-based automation tool for scheduling and sending WhatsApp messages through WhatsApp Web.

## Features

- Send scheduled WhatsApp messages
- Support for international phone numbers
- User-friendly command-line interface
- Time scheduling in 24-hour format
- Automatic WhatsApp Web integration

## Prerequisites

- Python 3.13 or higher
- Active internet connection
- WhatsApp account
- Access to WhatsApp Web
- Web browser (default browser will be used)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Rafiqdevhub/Watsapp_automation.git
cd Watsapp_automation
```

2. Install dependencies using UV package manager:

```bash
uv add pywhatkit pyautogui requests pillow
```

## Usage

1. Run the script:

```bash
python main.py
```

2. Follow the interactive prompts:

   - Enter the recipient's phone number with country code (e.g., 911234567890)
   - Type your message
   - Set the delivery time (hour and minutes)
   - Wait for the message to be sent at the specified time

3. To quit the program:
   - Type 'q' when prompted for a phone number

## Example

```
Welcome to WhatsApp Message Automation!
--------------------------------------

Enter phone number (with country code, e.g., 911234567890)
or 'q' to quit: 911234567890
Enter your message: Hello, this is a test message
Enter the hour (24-hour format, 0-23): 14
Enter the minutes (0-59): 30

Initiating WhatsApp Web...
Message will be sent at 14:30
```

## Important Notes

- The application requires WhatsApp Web access
- First-time users will need to scan the QR code
- The program creates a log file (PyWhatKit_DB.txt) to track sent messages
- Ensure your phone is connected to the internet when messages are scheduled to be sent
- The default wait time for WhatsApp Web to load is 15 seconds

## Dependencies

- pywhatkit: For WhatsApp automation
- pyautogui: For GUI automation
- requests: For HTTP requests
- pillow: For image processing

## Contributing

Feel free to submit issues and enhancement requests!
