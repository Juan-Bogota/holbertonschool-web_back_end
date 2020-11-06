#!/usr/bin/env python3
"""
Module: Basic Auth, Extract base64 Authorization,
Decode Base64 Authorization
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Method: Decode Base64 Authorization
        Return a string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base = base64_authorization_header.encode('utf-8')
            decoded = b64decode(base)
            info = decoded.decode('utf-8')
            return info
        except:
            return None
