from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class SimpleQuantumRandomDemo:
    def __init__(self, num_bits):
        self.num_bits = num_bits
        self.simulator = AerSimulator()  # Using AerSimulator as the backend

    def generate_random_bits(self):
        # Create a Quantum Circuit acting on a quantum register of size 'num_bits'
        circuit = QuantumCircuit(self.num_bits, self.num_bits)
        circuit.h(range(self.num_bits))  # Apply Hadamard gate to all qubits
        circuit.measure(range(self.num_bits), range(self.num_bits))  # Measure all qubits
        return circuit

    def run_simulation(self):
        circuit = self.generate_random_bits()
        result = self.simulator.run(circuit, shots=1).result()  # Execute the circuit on the quantum simulator
        counts = result.get_counts(circuit)
        return counts

    def visualize(self, counts):
        plot_histogram(counts)
        plt.show()  # Display the histogram

# Example usage
if __name__ == "__main__":
    num_bits = 8
    demo = SimpleQuantumRandomDemo(num_bits)
    result_counts = demo.run_simulation()
    print("Quantum random bits:", result_counts)
    demo.visualize(result_counts)
