import time

from selenium.common.exceptions import WebDriverException

TIMEOUT = 5


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > TIMEOUT:
                    raise e
                time.sleep(0.5)

    return modified_fn
