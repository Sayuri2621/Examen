import logging
import os
import traceback


class Logger():

    def __set_logger(self):
        log_directory = 'logs'
        log_filename = 'app.log'

        logger = logging.getLogger("DynamoFlow")
        logger.setLevel(logging.INFO)

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger

    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)

            if (level == "critical"):
                logger.critical(message)
            elif (level == "debug"):
                logger.debug(message)
            elif (level == "error"):
                logger.error(message)
            elif (level == "info"):
                logger.info(message)
            elif (level == "warning"):
                logger.warning(message)
        except Exception as ex:
            print("IMPRIME EX",traceback.format_exc())
            print(ex)