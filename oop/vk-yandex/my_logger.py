import logging
import datetime

file_name = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
_log_format = f"%(asctime)-24s * %(levelname)-8s * %(filename)-10s * %(funcName)-15s * line:%(lineno)-5s * %(message)s"

def get_file_handler():
    file_handler = logging.FileHandler(f"{file_name}.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    return logger