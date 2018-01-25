import os
import sys

# 而不是 import os, sys
# 不过可以这样：
from subprocess import Popen, PIPE
print(os, sys, Popen, PIPE)
var_1, var_2, var_3, var_4 = None, None, None, None
var_a, var_b, var_c, var_d = None, None, None, None
this_is_one_thing, this_is_another_thing = True, True


def do_something():
    pass

# 缩进


def i_am_a_long_function(para1, para2, para3, para4,
                         para_a, para_b, para_c, para_d):
    pass


def i_am_a_long_function_too(
        para1, para2, para3, para4, para_a, para_b, para_c, para_d):
    pass


i_am_a_long_function(var_1, var_2, var_3, var_4,
                     var_a, var_b, var_c, var_d)
i_am_a_long_function_too(
    var_1, var_2, var_3, var_4, var_a, var_b, var_c, var_d)


# 单行请勿超过80字符
# implicit line joining inside parentheses, brackets and braces.


if (
        this_is_one_thing and this_is_another_thing
        and this_is_another_thing and this_is_another_thing
   ):
    do_something()

# 和元素对齐
my_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9,
    1, 2, 3, 4, 5, 6, 7, 8, 9,
    1, 2, 3, 4, 5, 6, 7, 8, 9]

income = (var_1
          + var_2
          + (var_3 - var_4)
          - var_a
          - var_b)


def complex(real, imag=0.0): return do_something(r=real, i=imag)

# 尽量不要用 \ 来换行
# 尽量不要在类中取太长的变量名
# 尽量
