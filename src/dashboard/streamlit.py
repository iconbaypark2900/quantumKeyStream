import streamlit as st
from quantum.quantumRandomGenerator import QuantumRandomGenerator
import matplotlib.pyplot as plt
import numpy as np
import logging
from analysis.statisticalAnalysis import generate_data, perform_tests, plot_data

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    st.title('Quantum Random Number Generator Dashboard')

    # User input for the number of bits and number of random numbers
    num_bits = st.sidebar.slider('Select the number of bits for the random number', min_value=1, max_value=16, value=8)
    num_numbers = st.sidebar.slider('Select the number of random numbers to generate', min_value=1, max_value=100, value=10)

    # User input for statistical analysis parameters
    size = st.sidebar.number_input('Sample Size', min_value=100, max_value=10000, value=1000)
    mean = st.sidebar.slider('Mean', min_value=-5.0, max_value=5.0, value=0.0)
    std_dev = st.sidebar.slider('Standard Deviation', min_value=0.1, max_value=10.0, value=1.0)

    if st.button('Generate Random Numbers'):
        qrng = QuantumRandomGenerator(num_bits=num_bits)  # Initialize with user-specified bits
        try:
            # Generate random numbers
            random_numbers = [qrng.generate_cryptographic_random_number() for _ in range(num_numbers)]
            st.write('Generated Random Numbers:', random_numbers)

            if random_numbers:
                fig, ax = plt.subplots()
                ax.hist(random_numbers, bins=20, edgecolor='black')
                ax.set_title('Distribution of Random Numbers')
                ax.set_xlabel('Number')
                ax.set_ylabel('Frequency')
                st.pyplot(fig)
        except Exception as e:
            logging.error(f"Error generating random numbers with {num_bits} bits: {e}")
            st.error("Failed to generate random numbers. Please try again.")

    # Data generation and analysis for statistical properties
    if st.button('Analyze Random Data'):
        data = generate_data(size, mean, std_dev)
        test_results = perform_tests(data)
        plot_data(data)
        st.write("### Summary Statistics", data.describe())
        st.image('/mnt/data/histogram.png', caption='Histogram of Quantum Random Numbers')
        st.write("### Statistical Test Results", test_results)

        if st.button('Show Raw Data'):
            st.write(data)

if __name__ == '__main__':
    main()