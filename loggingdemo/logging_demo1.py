"""
logging demo 1
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging as log

log.basicConfig(filename="test2.log", level=log.DEBUG)

log.warning("Test  message")
log.info("Test info message")
log.error("Test error message")
log.debug("Test debug message")
log.critical("Test critical message")
