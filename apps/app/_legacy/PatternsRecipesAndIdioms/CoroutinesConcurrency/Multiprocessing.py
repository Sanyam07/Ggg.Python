import sys
import time
import multiprocessing

DELAY = 0.1
DISPLAY = ['|', '/', '-', '\\']


def spinner_func(before='', after=''):
    write, flush = sys.stdout.write, sys.stdout.flush
    pos = -1
    while True:
        pos = (pos + 1) % len(DISPLAY)
        msg = before + DISPLAY[pos] + after
        write(msg)
        flush()
        write('\x08'
              *
              len(msg))
        time.sleep(DELAY)


def long_computation():
    # emulate a long computation
    print("long_computation started.")
    time.sleep(3)
    print("long_computation finished.")


if __name__ == '__main__':
    # https://docs.python.org/3.6/library/multiprocessing.html
    spinner = multiprocessing.Process(
        None, spinner_func, args=('Please wait ... ', ''))
    spinner.start()
    try:
        long_computation()
        print('Computation done')
    finally:
        spinner.terminate()
