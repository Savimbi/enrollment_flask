import os


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or b'\xc3\xc4}!\x1a\xdf3\x8b`\xc5\x01c\x05y\x14r'

    MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}
