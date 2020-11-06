#!/usr/bin/env python3
"""
Module: Basic Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class: Basic Authorization"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Method: Extract base64 Authorization"""
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]
