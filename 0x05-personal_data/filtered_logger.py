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
    return re.sub(fields[1] + '=.*?' + separator, fields[1] + '=' +
                  redaction + separator, message)
