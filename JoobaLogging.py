import logging

# Task 1 
# Create a logging configuration

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s *>> %(levelname)s *>> %(message)s *>> %(asctime)s *>> %(filename)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    filename="All_logs.log", #this line will create a file and write there logs instead of console.
    filemode='w' #default - a (meaning append) 'w' means it deletes old logs and write new ones.
)

logging.critical("I will Cry!")
logging.critical("Life is Strange!")
logging.error("Error!")
logging.warning("Warning!")
logging.info("Info!")
logging.debug("debug")

root_logger = logging.getLogger()

# Handlers   custom Handlers
main_formatter = logging.Formatter(
    '%(name)s => %(levelname)s => %(message)s => %(asctime)s => %(filename)s'
)
console = logging.StreamHandler() #FileHandler SMTPHandler HTTPHandler
console.setLevel(logging.WARNING)
console.setFormatter(main_formatter)

root_logger.addHandler(console)

root_logger.critical("Something went Wrong")
