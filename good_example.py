print("a long long long long long long long long long long long long "
      "long long long long long long long long long long long long "
      "long long long long long long sentence but what I need is here")

anum, bnum, cnum = 1, 2, 3
someValue = ((anum * bnum + cnum)
             / (anum - bnum + cnum + anum * bnum)
             - anum - bnum + cnum)


def generate_array():
    """
    generate array with suffix
    """
    return ['%s_suffix' % x for x in range(100)]


def fetch(path):
    """
    get all lines for file: path
    """
    with open(path, 'r') as file_r:
        return file_r.readlines()