import logging

# PipeLine -> The set of scripts which does some things with Data
            #  ETL, ELT pipelines
# Exctract 
# Transform
# Load

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s => %(levelname)s => %(message)s => %(asctime)s => %(filename)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    filename="All_logs.log", #this line will create a file and write there logs instead of console.
    filemode='w' #default - a (meaning append) 'w' means it deletes old logs and write new ones.
    
)

# (lineno)d

logging.critical("Production is Down!")

logging.error("Error!")

logging.warning("Warning!") # Default level

#  We won't see the logging.info and logging.debug
# Because idk, but we can to change the configuration

logging.info("Info!")

logging.debug("debug")


try:
    result = 1 / 0
except ZeroDivisionError as a:
    logging.error('Some Error Occured!')
    logging.error('Error', exc_info=True)
    logging.error(f'Error {a}')
    
logger = logging.getLogger()
test_logger = logging.getLogger('test')
file_logger = logging.getLogger(__name__)

root_logger = logging.getLogger()

print(logger is root_logger)


#  In order to Add additional infomartion and Functionality to our logger config 
#  We need instances declared above.

# Handlers   custom Handlers
main_formatter = logging.Formatter(
    '%(name)s => %(levelname)s => %(message)s => %(asctime)s => %(filename)s'
)
console = logging.StreamHandler() #FileHandler SMTPHandler HTTPHandler
console.setLevel(logging.WARNING)
console.setFormatter(main_formatter)

root_logger.addHandler(console)  # What have we done here?

# Formatters  custom filter

# Filters    (Filter some data) custom filter
class AntiTestFilter(logging.Filter):
    def filter(self, record):
        print(dict(record))
        return True

anti_spam_filter = AntiTestFilter()

root_logger.addFilter(anti_spam_filter)