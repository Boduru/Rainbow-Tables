import json

from preprocess import H, R, SPACE, HIT_NUMBER, MAX_PWD_LEN


def attack(h):
    """Find chain and position to password and calculate password"""

    # List of all ending password (last column of rainbow table)
    ends = [e[1] for e in table]
    
    for j in range(HIT_NUMBER - 1, -1, -1):
        pwd = generate_pwd(h, HIT_NUMBER - 1, j)

        if pwd in ends:
            # sub-list index
            c = ends.index(pwd)
            
            return get_pwd(c, j)

    return None


def generate_pwd(h, i, j=0):
    """Go back in table to look for correct hash"""

    if i == j:
        return R(h, i)

    return R(H(generate_pwd(h, i - 1, j)), i)


def get_pwd(chain, pos):
    """Get the password using chain and position index"""

    # get the very first element (password of chain)
    p = table[chain][0]

    for i in range(pos):
        h = H(p)
        p = R(h, i)

    return p


def load(filename):
    """Load table from file"""

    with open(filename, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    table = load("table.rainbow")

    # hash to crack
    h = "01716c20793b54b07576cb3014a5f4ee"
    
    pwd = attack(h)

    print(pwd)
