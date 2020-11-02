#!/usr/bin/env python3
"""
Filtered Logger
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """filter datum"""

    message = re.sub(fields[0] + '=.*?' + separator, 'password=' +
                     redaction + separator, message)
    return re.sub(fields[1] + '=([0-9]{2}\\D[0-9]{2}\\D[0-9]{4})' +
                  separator, 'date_of_birth=' + redaction + separator,
                  message)
