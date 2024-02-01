from wasteDetection.logger import logging
import sys
from wasteDetection.exception import AppException

try:
    a = 3/"s"
except Exception as e:
    raise AppException(e,sys)