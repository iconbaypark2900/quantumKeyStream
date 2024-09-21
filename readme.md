# Quantum Random Number Generator (QRNG) Using Strangeworks HC

This is a Quantum Random Number Generator (QRNG) app that connects to the Strangeworks HC platform to generate true random numbers based on quantum phenomena. These numbers are then used to create secure cryptographic keys. The app provides a user-friendly dashboard for generating and visualizing quantum random numbers.

## Features

- **Quantum Random Number Generation:** Fetches quantum random numbers from Strangeworks HC using their API.
- **Entropy Extraction:** Processes quantum random numbers through an entropy extraction algorithm to ensure suitability for cryptographic purposes.
- **Cryptographic Key Generation:** Uses the extracted entropy to simulate cryptographic key generation.
- **User-Friendly Interface:** Built with Streamlit for an easy-to-use web interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a Strangeworks account and API access. [Sign up here](https://strangeworks.com/).
- You have Python 3.7 or higher installed.
- You have installed the necessary Python libraries (detailed below).

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/qrng-strangeworks-hc.git
   cd qrng-strangeworks-hc
