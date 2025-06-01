---
title: Logging
---

# Logging
To debug the code, you need to collect information and analyze it after execution. This section briefly introduces the logging module. The `logging` module is a standard Python module used to record diagnostic messages in a log file.

## Simple configurarion
The following is a simple code example that shows how to use the logging module.

``` python 
import logging
logging.basicConfig(
    filename  = 'debug.log',      # Log output file
    level     = logging.INFO,   # Output level
)

list_n = ['a',0, 1, 2, 'b']
for entry in list_n:
        print("The entry is", entry)
        logging.info(f' computation for {entry} started')
        r = 1/int(entry)
        logging.debug(f' computation is done for {entry}')
logger.info(f'Process id Done')
```

logging.basicConfig is a one-time configuration at the beginning. Later, we'll show how you can change the configuration. There are different logging levels: `DEBUG`, `ERROR`, `WARNING`, `INFO`, and `CRITICAL`. By choosing a level, you can filter messages, such as sending INFO and WARNING to sys.stdout, INFO, WARNING, and ERROR (and above) to sys.stderr, and the rest to a file named app.log.

## Logging Configuration
Let use `try-except` statement

``` py
import sys
import logging
# create a logger with 'test_application'
logger = logging.getLogger('test_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('file.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

list_n = ['a',0, 1, 2, 'b']
for entry in list_n:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        logger.info(f' computation is done for {entry}')
    except Exception as e:
        print(f'Reason: Oops!, {e.__class__} occurred.')
        logger.warning(f' Could not compute for {entry}')
        logger.debug(f'Reason: Oops!, {e.__class__} occurred.')
    finally: 
        logger.info(f'Next entry')
logger.info(f'Process id Done')
```

Most programs use `logging.getLogger(__name__)` instead of specifying a name directly. We can rewrite the function as follows:


``` py
# main.py
import sys
import logging

list_n = ['a',0, 1, 2, 'b']

def reciptocal(list_n):
    for entry in list_n:
        try:
            print("The entry is", entry)
            r = 1/int(entry)
            logger.info(f' computation is done for {entry}')
        except Exception as e:
            print(f'Reason: Oops!, {e.__class__} occurred.')
            logger.warning(f' Could not compute for {entry}')
            logger.debug(f'Reason: Oops!, {e.__class__} occurred.')
        finally: 
            logger.info(f'Next entry')
    logger.info(f'Process id Done')


if __name__ == '__main__':
    # create a logger with 'test_application'
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('file.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    fh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    reciptocal(list_n)
```

