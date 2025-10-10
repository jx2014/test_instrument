import logging
import sys
from datetime import datetime
from pathlib import Path

def setup_logging(level=logging.INFO, log_dir="logger"):
    log_path = Path(log_dir)
    log_file_name = f'test_automation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    log_file_path = log_path / log_file_name
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file_path)
        ]
    )
    suppress_loggers = {
        'pyvisa': logging.WARNING,
        'urllib3': logging.WARNING,
        'matplotlib': logging.WARNING,
        'PIL': logging.WARNING,
        'pyvisa-py': logging.WARNING
    }

    for logger_name, log_level in suppress_loggers.items():
        logging.getLogger(logger_name).setLevel(log_level)

def get_logger(name):
    return logging.getLogger(name)