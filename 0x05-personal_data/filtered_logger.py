#!/usr/bin/env python3
"""
Filtered Logger
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """filter datum"""

    message = re.sub(fields[0] + '=.*?' + separator, fields[0] + '=' +
                     redaction + separator, message)
    return re.sub(fields[1] + '=([0-2][0-9]|3[0-1])(\/)(0[1-9]|1[0-2])\\2(\\d{4})' +
                  separator, fields[1] + '=' + redaction + separator,
                  message)
