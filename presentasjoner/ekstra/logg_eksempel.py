import logging
import traceback

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Start')
    logging.debug('Midt i')
    logging.info('Slutt')
    a = 5
    b = 0
    try:
        c = a / b
    except Exception as err:
        logging.warning("Error %s",err)
        logging.warning(traceback.format_exc())
if __name__ == '__main__':
    main()