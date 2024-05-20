# from qiskit import IBMQ
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from hashlib import sha3_256
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class QuantumRandomGenerator:
    _backend_cache = {}

    def __init__(self, num_bits, backend_name='aer_simulator'):
        self.num_bits = num_bits
        # Use AerSimulator directly or fetch another backend
        self.backend = AerSimulator() if backend_name == 'aer_simulator' else self.get_backend(backend_name)
        logging.info(f"QuantumRandomGenerator initialized with {num_bits} bits on {backend_name} backend.")

    # @classmethod
    # def get_backend(cls, backend_name):
    #     if backend_name not in cls._backend_cache:
    #         try:
    #             IBMQ.load_account()
    #             provider = IBMQ.get_provider(hub='ibm-q')
    #             cls._backend_cache[backend_name] = provider.get_backend(backend_name)
    #             logging.info(f"Loaded and cached backend: {backend_name}")
    #         except Exception as e:
    #             logging.error(f"Failed to load backend {backend_name}: {e}")
    #             raise
    #     return cls._backend_cache[backend_name]

    def generate_quantum_random_bits(self):
        circuit = QuantumCircuit(self.num_bits, self.num_bits)
        circuit.h(range(self.num_bits))  # Create superposition
        circuit.measure(range(self.num_bits), range(self.num_bits))  # Collapse the state
        job = self.backend.run(circuit, shots=1)
        result = job.result()
        bits = list(result.get_counts().keys())[0]
        logging.info("Quantum random bits generated.")
        return bits

    def generate_cryptographic_random_number(self):
        raw_bits = self.generate_quantum_random_bits()
        hashed = sha3_256(raw_bits.encode()).hexdigest()
        logging.info("Cryptographic random number generated.")
        return int(hashed, 16)

# Example usage: Generate a 256-bit cryptographic random number
if __name__ == "__main__":
    # Generate various cryptographic random numbers
    qrng_128 = QuantumRandomGenerator(128)
    print(f"128-bit random number: {qrng_128.generate_cryptographic_random_number()}")

    qrng_512 = QuantumRandomGenerator(512)
    print(f"512-bit random number: {qrng_512.generate_cryptographic_random_number()}")

    qrng_64 = QuantumRandomGenerator(64)
    print(f"64 quantum random bits: {qrng_64.generate_quantum_random_bits()}")

    # # Real quantum device example
    # qrng_real = QuantumRandomGenerator(256, 'ibmq_quito')
    # print(f"256-bit random number from real quantum device: {qrng_real.generate_cryptographic_random_number()}")

    # Generate multiple random numbers in a loop
    for i in range(3):
        qrng_loop = QuantumRandomGenerator(256)
        print(f"Random number {i+1}: {qrng_loop.generate_cryptographic_random_number()}")

    # Direct usage of quantum random bits
    qrng_direct_bits = QuantumRandomGenerator(256)
    print(f"Direct 256 quantum random bits: {qrng_direct_bits.generate_quantum_random_bits()}")
