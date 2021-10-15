import hashlib, binascii
import json
import random


# __GLOBALS__
SPACE = "123456"     # all the disponible characters for password
MAX_PWD_LEN = 6    # max length of a password
HIT_NUMBER = 10      # number of iterations to create a chain
CHAIN_NUMBER = 2


def H(plaintext):
    """NTLM hash"""

    hash = hashlib.new('md4', plaintext.encode('utf-16le')).digest()
    
    return binascii.hexlify(hash).decode("utf-8")


def R(h, i):
    """Reduce function of hash"""

    pwd = ""
    h = int(h, 16) # str to hex

    # iterate through len(space) times
    while len(pwd) < MAX_PWD_LEN:
        pwd += SPACE[(h + i) % len(SPACE)]
        h = h // len(SPACE)

    return pwd


def chain(start):
    """Generate the chain"""

    p = start

    # starting from 0 to HIT_NUMBER - 1
    for i in range(0, HIT_NUMBER):
        # Hash then reduce
        h = H(p)
        p = R(h, i)

    return p


def rainbow_table(pwds):
    """Generate the rainbow table"""

    out = []

    for start in pwds:
        # create a chain
        c = chain(start)

        # check if ending pwd not already exists in out table
        if c not in [e[1] for e in out]:
            out.append((start, c))

    return out


def kick_off():
    """Create starting passwords
    (beginning of each chain)"""

    # return ["".join(random.choices(SPACE, k=MAX_PWD_LEN)) for _ in range(CHAIN_NUMBER)]

    return ["111111"]
    

def save(table, filename):
    """Save table in file"""

    with open(filename, "w") as f:
        json.dump(table, f, indent=4)


if __name__ == "__main__":
    print(H("526633"))
    pwds = kick_off()
    table = rainbow_table(pwds)

    save(table, "table.rainbow")

    print(table)
