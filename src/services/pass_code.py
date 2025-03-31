from bcrypt import hashpw, checkpw, gensalt


def check_match(password, hash_password):
    """
    :param password: Password from plain text
    :param hash_password: Password from hash text
    :return: True if it matches or false otherwise.

    """
    match_password = checkpw(password.encode('utf8'), hash_password)
    return match_password


def encrypt(password):
    """
    :param password: Password
    :return: encrypt password

    """
    hash_password = hashpw(password.encode('utf8'), gensalt())
    return hash_password




