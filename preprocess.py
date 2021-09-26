import hashlib, binascii
import json


# __GLOBALS__
SPACE = "01234"     # all the disponible characters for password
MAX_PWD_LEN = 3     # max length of a password
HIT_NUMBER = 5      # number of iterations to create a chain


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
        i = i // len(SPACE)

    return pwd


def chain(start):
    """Generate the chain"""

    gen = start

    # starting from 0 to HIT_NUMBER - 1
    for i in range(HIT_NUMBER):
        # Hash then reduce
        gen = H(gen)
        gen = R(gen, i)

    return gen


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

    table = [
        "100",
        "111",
        "222",
        "444"
    ]

    return table
    

def save(table, filename):
    """Save table in file"""

    with open(filename, "w") as f:
        json.dump(table, f, indent=4)


if __name__ == "__main__":
    pwd = "411" # pwd to find
    h = H(pwd) # hash of the pwd

    print(h)

    pwds = kick_off()
    table = rainbow_table(pwds)

    save(table, "table.rainbow")

    print(table)