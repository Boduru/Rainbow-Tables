# Rainbow Tables

# General
Rainbow tables implemented in Python using the NTLM hashing function (Windows) for password cracking. 
This password cracking method known as TMTO (time memory tradeoff) allows you to crack a password based on its hash.

# Files
* preprocess.py : pre-calculations (exhaustive research)
* attack.py : real-time online attack (hash cracking)

# How to use
1. Launch preprocess.py file and wait for it to finish the work
2. Plug the hash you want to crack
3. Launch attack.py file

# Downsides
* Very slow due to massive calculations on the preprocessing step
* Based on one hashing function (need to re-calculate the table for every hashing function to break)

## Requirements
- Python 3.X.X
