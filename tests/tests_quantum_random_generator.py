from qiskit import IBMQ, QuantumCircuit, execute
from qiskit.exceptions import IBMQBackendError
from quantum.quantumRandomGenerator import generate_quantum_random_bits, generate_cryptographic_random_number
from hashlib import sha256
import sts 

def initialize_ibmq():
    try:
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        return provider.get_backend('ibmq_quito')
    except Exception as e:
        print(f"Failed to initialize IBMQ: {e}")
        raise

def generate_quantum_random_bits(num_bits):
    try:
        backend = initialize_ibmq()
        circuit = QuantumCircuit(num_bits, num_bits)
        circuit.h(range(num_bits))
        circuit.measure(range(num_bits), range(num_bits))
        result = execute(circuit, backend, shots=1).result()
        bits = list(result.get_counts().keys())[0]
        return bits
    except IBMQBackendError as e:
        print(f"Error executing quantum circuit: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def generate_cryptographic_random_number(num_bits):
    raw_bits = generate_quantum_random_bits(num_bits)
    hashed = sha256(raw_bits.encode()).hexdigest()
    return int(hashed, 16)

def perform_nist_tests(bit_sequence, num_bits):
    # Convert integer to binary string
    binary_sequence = bin(bit_sequence)[2:].zfill(num_bits)
    # Perform NIST tests
    results = sts.nist_test_suite(binary_sequence, num_bits)
    return results

# Example usage
if __name__ == "__main__":
    # Example 1: Generate a 128-bit cryptographic random number
    qrng_128 = QuantumRandomGenerator(128)
    random_number_128 = qrng_128.generate_cryptographic_random_number()
    print(f"128-bit random number: {random_number_128}")

    # Example 2: Generate a 512-bit cryptographic random number
    qrng_512 = QuantumRandomGenerator(512)
    random_number_512 = qrng_512.generate_cryptographic_random_number()
    print(f"512-bit random number: {random_number_512}")

    # Example 3: Generate quantum random bits with 64 bits
    qrng_64 = QuantumRandomGenerator(64)
    random_bits_64 = qrng_64.generate_quantum_random_bits()
    print(f"64 quantum random bits: {random_bits_64}")

    # Example 4: Use a real quantum device as backend
    qrng_real = QuantumRandomGenerator(256, 'ibmq_quito')
    random_number_real = qrng_real.generate_cryptographic_random_number()
    print(f"256-bit random number from real quantum device: {random_number_real}")

    # Example 5: Generate multiple random numbers in a loop
    for i in range(5):
        qrng_loop = QuantumRandomGenerator(256)
        random_number_loop = qrng_loop.generate_cryptographic_random_number()
        print(f"Random number {i+1}: {random_number_loop}")

    # Example 6: Generate a random number with minimal bits
    qrng_minimal = QuantumRandomGenerator(1)
    random_number_minimal = qrng_minimal.generate_cryptographic_random_number()
    print(f"Minimal bit random number: {random_number_minimal}")

    # Example 7: Generate a large number of bits for a high-security application
    qrng_high_security = QuantumRandomGenerator(1024)
    random_number_high_security = qrng_high_security.generate_cryptographic_random_number()
    print(f"1024-bit high-security random number: {random_number_high_security}")

    # Example 8: Generate random bits and use them directly without hashing
    qrng_direct_bits = QuantumRandomGenerator(256)
    direct_bits = qrng_direct_bits.generate_quantum_random_bits()
    print(f"Direct 256 quantum random bits: {direct_bits}")

    # Example 9: Generate random numbers using different hash functions
    qrng_sha256 = QuantumRandomGenerator(256)
    random_number_sha256 = qrng_sha256.generate_cryptographic_random_number()
    print(f"Random number with SHA-256: {random_number_sha256}")

    # Example 10: Generate and log multiple random numbers for batch processing
    for j in range(3):
        qrng_batch = QuantumRandomGenerator(256)
        random_number_batch = qrng_batch.generate_cryptographic_random_number()
        logging.info(f"Batch random number {j+1}: {random_number_batch}")
        print(f"Batch random number {j+1}: {random_number_batch}")


import unittest
from quantum.quantumRandomGenerator import QuantumRandomGenerator
from qiskit import Aer

class TestQuantumRandomGenerator(unittest.TestCase):
    def setUp(self):
        # Use the Aer simulator for all tests
        self.backend_name = 'qasm_simulator'

    def test_generate_128_bit_random_number(self):
        qrng = QuantumRandomGenerator(128, self.backend_name)
        result = qrng.generate_cryptographic_random_number()
        self.assertIsInstance(result, int)
        self.assertEqual(result.bit_length(), 128)

    def test_generate_512_bit_random_number(self):
        qrng = QuantumRandomGenerator(512, self.backend_name)
        result = qrng.generate_cryptographic_random_number()
        self.assertIsInstance(result, int)
        self.assertEqual(result.bit_length(), 512)

    def test_generate_64_quantum_random_bits(self):
        qrng = QuantumRandomGenerator(64, self.backend_name)
        bits = qrng.generate_quantum_random_bits()
        self.assertEqual(len(bits), 64)

    def test_generate_multiple_random_numbers(self):
        results = []
        for i in range(5):
            qrng = QuantumRandomGenerator(256, self.backend_name)
            result = qrng.generate_cryptographic_random_number()
            results.append(result)
        self.assertEqual(len(results), 5)
        self.assertTrue(all(isinstance(num, int) for num in results))

    def test_generate_minimal_bit_random_number(self):
        qrng = QuantumRandomGenerator(1, self.backend_name)
        result = qrng.generate_cryptographic_random_number()
        self.assertIn(result, [0, 1])

    def test_generate_high_security_random_number(self):
        qrng = QuantumRandomGenerator(1024, self.backend_name)
        result = qrng.generate_cryptographic_random_number()
        self.assertIsInstance(result, int)
        self.assertEqual(result.bit_length(), 1024)

    
    def test_generate_direct_quantum_random_bits(self):
        qrng = QuantumRandomGenerator(256, self.backend_name)
        bits = qrng.generate_quantum_random_bits()
        self.assertEqual(len(bits), 256)

    def test_generate_random_number_with_sha256(self):
        qrng = QuantumRandomGenerator(256, self.backend_name)
        result = qrng.generate_cryptographic_random_number()
        self.assertIsInstance(result, int)
        self.assertEqual(result.bit_length(), 256)

    def test_batch_random_number_generation(self):
        results = []
        for j in range(3):
            qrng = QuantumRandomGenerator(256, self.backend_name)
            result = qrng.generate_cryptographic_random_number()
            results.append(result)
        self.assertEqual(len(results), 3)
        self.assertTrue(all(isinstance(num, int) for num in results))

if __name__ == '__main__':
    unittest.main()

