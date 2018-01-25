import time

from deps.decorator import log


@log
def do_something(user_name):
    print('do something')
    time.sleep(2)


@log
def do_another_thing(user_name):
    print('do_another_thing')
    time.sleep(5)
