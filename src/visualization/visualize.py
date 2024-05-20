import sys
import os
# Append the directory of your quantum module to sys.path
sys.path.append('/home/gengar/data/quantum/quantumKeyStream/src')

import matplotlib.pyplot as plt
from quantum.quantumRandomGenerator import QuantumRandomGenerator

def visualize_random_bits(num_bits):
    qrng = QuantumRandomGenerator(num_bits)
    random_bits = qrng.generate_quantum_random_bits()
    bit_counts = [int(bit) for bit in random_bits]

    plt.bar(range(num_bits), bit_counts)
    plt.xlabel('Bit Position')
    plt.ylabel('Bit Value')
    plt.title('Quantum Random Bits Visualization')
    plt.show()

if __name__ == "__main__":
    visualize_random_bits(16)
    visualize_random_bits(16)