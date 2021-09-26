# Rainbow-Tables

# General
Rainbow tables implementation in Python using NTLM hashing function (Windows) for password cracking.
This password cracking method know as TMTO (time memory tradeoff) permits you to crack a password based on its hash.

# Files
* preprocess.py : pre-calculations (exhaustive research)
* attack.py : real-time online attack (hash cracking)

# How to use
1. Launch preprocess.py file and wait for it to finish the work
2. Put the hash you want to crack
3. Launch attack.py file

# Downsides
* Very slow due to massive calculations on the preprocessing step
* Based on one hash function (need to re-calculate the table for every hash function to break)
