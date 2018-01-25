print("a long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long sentence but what I need is here")

anum = 1
bnum = 2
cnum = 3
someValue = (anum * bnum + cnum) / (anum - bnum + cnum + anum * bnum) - anum - bnum + cnum


def generate_array():
    some_array = []
    for i in range(100):
        some_array.append(str(i) + '_suffix')
    return some_array


def fetch(path):
    file_r = None
    try:
        file_r = open(path,'r')
        return file_r.readlines()
    finally:
        if file_r:
            file_r.close()
