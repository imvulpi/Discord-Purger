# Discord Purger

Automate the deletion of your unwanted Discord messages with this Python script powered by Playwright!

**Requirements**: Python version 3.8 or higher (Tested with Python 3.10.6)

The program navigates through discord and deletes your unwanted messages. This script retries after being rate-limited, and checks at the end whether all of the messages were deleted (retries if not).

## Quick Tutorial

**Command**: `python.exe purger.py delete u- s- e- p-`

**Explanation of Arguments**:

- **u-(...)**: Enter the Discord server URL here. Simply copy the URL from the server where you want your messages deleted.
  
- **s-(...)**: Provide the search query here. If your query includes emojis, the program will still recognize them, even if displayed differently in the command line.

- **e-(...) (Optional)**: Your Discord email.

- **p-(...) (Optional)**: Your Discord password.

The last two arguments (email and password) are optional. You can alternatively **log in via a QR code** by scanning screenshots the qr code taken by the program.

(Note: Logging in is required to use this program.)

## Configuration

In **config.py** you can configure:

- Delays

- Timeouts

- Screenshot path

- Deletion speeds
