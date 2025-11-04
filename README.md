How to Use This Script
This script generates a password hash using the PBKDF2-HMAC-SHA256 algorithm. It requires a password, a salt, and a rands value as input. It then produces a formatted string that includes the algorithm, iteration count, salt, and the final hash, all encoded in Base64.
Prerequisites

    You must have Python 3 installed on your system.

Instructions

    Save the Script:
    Save the code as a Python file, for example, hash_generator.py.
    Open Your Terminal:
    Open a terminal or command prompt on your computer.
        Windows: Open Command Prompt (cmd) or PowerShell.
        macOS/Linux: Open the Terminal application.
    Navigate to the Script's Directory:
    Use the cd (change directory) command to navigate to the folder where you saved hash_generator.py. For example, if you saved it on your Desktop, you would run:
    Bash

    cd Desktop

Run the Script:
Execute the script using the python command:
Bash

    python hash_generator.py

    Provide the Required Inputs:
    The script will prompt you to enter four pieces of information one by one. After typing each value, press Enter.
        Salt: Enter the salt value. This should be the specific string you intend to use for the hashing process.
        Rands: Enter the rands value. This string will be appended to the password before hashing.
        User: Enter the username. Note: This value is used for context in the prompt but is not part of the hash calculation itself.
        Password: Enter the plain-text password you wish to convert.

Example Usage
Here is an example of what a complete session in the terminal will look like:
Bash

    $ python hash_generator.py

Salt: LCBhdtJWj1
Rands: mY1941ma8w
User: boris
Password: my_secret_password

Output
After you provide all the inputs, the script will print a single line containing the formatted hash string. This is the final output you will use.
The output follows the format: sha256:iterations:salt_base64:hash_base64
Example output based on the inputs above:
Plain Text

sha256:10000:TENCaGR0SldqMQ==:tPb8E7/gL4a4g/pYp8bX2A7bF8rJ5eZ6c3nQ9sY4Z3A=

You can now copy this entire string and store it in your database or use it for verification purposes.
