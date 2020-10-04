from .is_ongoing import is_ongoing


def before_request():
    is_ongoing()
