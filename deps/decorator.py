import time
import logging
import functools

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)
log_handler = logging.StreamHandler()
log_format = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
log_handler.setFormatter(log_format)
LOG.addHandler(log_handler)


def log(func):
    @functools.wraps(func)
    def wrap(*args, **kw):
        start_time = time.time()
        LOG.info('function %s started' % func.__name__)
        result = func(*args, **kw)
        LOG.info('function %s ended' % func.__name__)
        end_time = time.time()
        elapse = end_time - start_time
        LOG.info('elapse %s' % elapse)
        return result
    return wrap
