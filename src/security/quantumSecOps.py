from quantum.quantumRandomGenerator import QuantumRandomGenerator

def generate_session_key():
    """ Generate a secure session key using QRNG. """
    qrng = QuantumRandomGenerator(256)
    return int(qrng.generate_quantum_random_bits(), 2)  # Generate a 256-bit session key

def simulate_secure_communication():
    """ Simulate a secure communication session using a QRNG-generated session key. """
    session_key = generate_session_key()
    print("Session Key for Secure Communication:", session_key)

def write_random_data_to_file(file_name, num_bits, num_samples):
    qrng = QuantumRandomGenerator(num_bits)
    with open(file_name, "wb") as file:
        for _ in range(num_samples):
            # Generate random numbers and write them as binary data
            num = qrng.generate_cryptographic_random_number()
            file.write(num.to_bytes((num_bits + 7) // 8, byteorder='big'))

def encrypt_data(data, key):
    """ Encrypt data using XOR encryption with a quantum-generated key. """
    encrypted = ''.join(chr(ord(char) ^ key) for char in data)
    return encrypted

# Example usage
if __name__ == "__main__":
    # Generate and write 10,000 samples of 16-bit random numbers
    write_random_data_to_file("random_data.bin", 16, 10000)
    # Generate a session key using QRNG
    session_key = generate_session_key()
    print("Session Key for Secure Communication:", session_key)
    # Encrypt data example using the generated session key
    encrypted_data = encrypt_data("Sensitive bank transaction details", session_key)
    print("Encrypted Transaction:", encrypted_data)