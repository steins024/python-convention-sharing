from functools import reduce

from deps.decorator import log
# file_path = './data/biomart.txt'


@log
def get_line_cnt_v1(file_path):
    """
    perf: 69.213, 69.005, 68.936
    """
    with open(file_path, 'r') as file_r:
        return sum([1 for line in file_r])


@log
def get_line_cnt_v2(file_path):
    """
    perf: 70.993, 71.667, 71.018
    """
    file_r = open(file_path, 'r')
    cnt = 0
    for line in file_r:
        cnt += 1
    file_r.close()
    return cnt


@log
def get_line_cnt_v3(file_path):
    """
    perf: 71.588, 71.706, 71.642
    """
    with open(file_path, 'r') as file_r:
        return sum((1 for line in file_r))


@log
def get_line_cnt_v4(file_path):
    """
    """
    with open(file_path, 'r') as file_r:
        return reduce(lambda x, y: x + y, [1 for line in file_r])


@log
def get_line_cnt_v5(file_path):
    """
    """
    with open(file_path, 'r') as file_r:
        return reduce(lambda x, y: x + y, (1 for line in file_r))
