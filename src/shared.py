# encoding: utf-8

import time

def block_thread(logger=False, exception=False, thName='', assName=''):
  # this function will lock the thread visually, in case a fatal error happened

  while True:
    if logger:
      logger.info('\n\n\n\n\n\n THREAD %s BLOCKED (%s)\n\n\n\n\n\n' % (thName, assName))
    else:
      print('\n\n\n\n\n\n THREAD %s BLOCKED (%s)\n\n\n\n\n\n' % (thName, assName))

    if exception:
      print(str(exception))

    time.sleep(10)
