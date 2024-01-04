import os
import sys 
import logging


logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(            # This function configures the logging system.

    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),     #This handler directs log messages to a file specified by log_filepath.
        logging.StreamHandler(sys.stdout)      #configures a handler to send log messages to the console
    ]
)


logger = logging.getLogger("cnnClassifierLogger")