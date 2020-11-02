#!/usr/bin/env python3
"""
Filtered Logger
"""
from typing import List
import re

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ filter datum """
    
    message = re.sub('password=[a-z0-9A-Z]*' + separator,'password=' + redaction + separator , message)
    return re.sub('date_of_birth=([0-9]*\D[0-9]*\D[0-9]*)' + separator, 'date_of_birth=' + redaction + separator, message )
