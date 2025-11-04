import hashlib
import base64

def generate_hash(password, salt, rands, iterations=10000):
    password_with_rands = password + rands
    salt_bytes = salt.encode('utf-8')
    
    hash_bytes = hashlib.pbkdf2_hmac('sha256', 
                                    password_with_rands.encode('utf-8'), 
                                    salt_bytes, 
                                    iterations, 
                                    dklen=32)
    
    # Converter salt e hash para base64
    salt_b64 = base64.b64encode(salt_bytes).decode('utf-8')
    hash_b64 = base64.b64encode(hash_bytes).decode('utf-8')
    
    # Formatar no padrão sha256:10000:salt64:hash64
    formatted_hash = f"sha256:{iterations}:{salt_b64}:{hash_b64}"
    
    return formatted_hash

# Get user inputs
salt = input("Salt: ")
rands = input("Rands: ")
user = input("User: ")
password = input("Password: ")

# Generate and print the hash
result = generate_hash(password, salt, rands)
print(f"\n{result}")
