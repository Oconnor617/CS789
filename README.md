# CS789
Thomas O'Connor - Final Project

This contains my algorithms for my CS789 Cyptography final project. The algortihms are written in Python and run via a Flask Application that take user input from a Web Server.
The App is built from the ground up using Flask and is primaritly used for simulating message Encryption/Decryption in El Gamal and RSA. It also cantains functions to play to role 
of Eve who can eavesdrop and decrypt an encrypted message in either RSA or El Gamal.

## Code Style
- <a href="https://www.python.org/dev/peps/pep-0008/">PEP 8</a> (Python Enhancement Proposals)
## Core Features
### RSA Encryption/Decryption/Cracking
Code is included for:

  ### RSA Encryption/Decryption/Cracking
  1) Genreate Encryption/Decryption keys based on uuser provided Primes p&q
  2) Genreate Encryption/Decryption keys based on large PseudoRandom Primes p&q
  3) Encrypt a number based on a given encryption key e and group n
  4) Decrypt a number based on a given deryption key e, group n and an entered encrypted message
  5) Crack RSA encryption based on Pollard's p-1 method for factoring n into it prime components
    
  ### ElGamal Encryption/Decryption/Cracking
  1) Genreate Encryption/Decryption keys based on user provided prime modulus
  2) Genreate Encryption/Decryption keys base on user provided prime modulus and primitive root/generator
  3) Encrypt a number based on a given recievers Public Key and the sender's Private Key
  4) Decrypt a number based on a given reievers Private Ket and the sender's Public Key
  5) Crack ElGamal by either eavesdropping or computing the discrete log to determine the participants Private Keys
    
  ### Helper Functions
  Many functions are included to make the above simulations work. They include functions such as:

      -Euclid's Greates Common Divisor
      
      -Extended Euclid's Greates Common Divisor

      -Fast Modular Exponentiation

      -Modular Inverse

      -Baby-Step Giant-Step for computing the discrete log

      -Primitive Root Search Algorithm (used for genreating ElGamal Keys)

      -Prime Factorization

      -Miller-Rabin primality test

      -PseudoRandom Prime Generator

      -Pollard's P-1 Method for factoring

      -and many more
      
   ### tests.py
    A module for running automatic tests via Pythons unittest framework is included. The tests were run periodically to ensure everything was working properally as 
    the app was developed. However since the whole app is built on the Flask framework the tests.py module needs a Flask context when running. 
    This is easily achived by running the tests.py from the commandline/terminal with the required Virtual Enviornment activated (See Setup and Running below). 
    Once you navigate to the directory you have saved this in simply activate the Virtual Enviornment and run it with the command: py tests.py. See my setup below.
                  (venv) C:\Users\tomoc\Desktop\CS789>py tests.py
      

## Technology and Frameworks
- IDE: Visual Studio Code
- Front-end framework: jQuery/JavaScript/Bootstrap
- Back-end framework: Flask
- Version Control: Github


## Setup and Running (Developer)
To use this app:-
1. Clone the app into a directory of your choice
2. Create a fresh virtual environment with no packages installed
   First from the terminal/command line navicate to the source where you have save the directory and type: py -m venv venv
3. Activate the new virtual environment you just created: 
        Windows: $source venv\Scripts\activate
        Linux/Mac: $source venv/bin/activate
4. Run the command - py -m pip install -r requirements.txt
5. With the venv active and the requirments installed run the app by typing flask run.
      ex) (venv) C:\Users\tomoc\Desktop\CS789>flask run
6. Navigate to the Localhost webserver (http://127.0.0.1:5000/) and begin using the app
