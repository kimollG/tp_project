from configparser import ConfigParser

configparser = ConfigParser()
configparser.read(".params")

SECURITY_SECTION_NAME = "Security"
DATABASE_SECTION_NAME = "Database"

SECRET_KEY = configparser[SECURITY_SECTION_NAME]["secret_key"] or \
             "default_security_key11" \
             "default_security_key22" \
             "default_security_key334455"

assert DATABASE_SECTION_NAME in configparser.sections(), \
    "No database parameters provided"

DATABASE_PARAMETERS = {
    "username": configparser[DATABASE_SECTION_NAME]["username"],
    "database": configparser[DATABASE_SECTION_NAME]["database"],
    "password": configparser[DATABASE_SECTION_NAME]["password"],
}

FETCH_BATCH_SIZE = 10000

