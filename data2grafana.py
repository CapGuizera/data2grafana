import base64
import binascii
import sys

# Get user inputs
password_hex = input("Password hash (hex): ")
salt = input("Salt: ")
iterations = 10000

try:
    # Convert hex to raw bytes
    target_raw = binascii.unhexlify(password_hex.replace("\n", ""))
    
    # Convert to base64
    target_hash64 = base64.b64encode(target_raw).decode("utf-8")
    salt64 = base64.b64encode(salt.encode("utf-8")).decode("utf-8")
    
    # Format the final string
    result = f"sha256:{iterations}:{salt64}:{target_hash64}"
    print(f"\n{result}")
    
except (binascii.Error, ValueError) as e:
    print("ERROR: Password hash is not valid hex:", e)
    sys.exit(1)
