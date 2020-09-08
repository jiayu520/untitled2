import logging
from time import sleep,ctime
#
#
logging.basicConfig(level=logging.INFO)
# logging.debug("jiayuu")


import _thread
def loop0():
    logging.info('start loop0 at '+ ctime()   )
    sleep(4)
    logging.info('end loopp0 at ' + ctime())

def loop1():
    logging.info('start loop1 at '+ ctime()   )
    sleep(4)
    logging.info('end loopp1 at ' + ctime())

def main():
    logging.info('start all at '+ ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(8)
    logging.info('end all at'+ ctime())


if __name__ == '__main__':
    main()