"""Colors for strings."""
from colored import fore, style

# pylint: disable=I0011,E1101

def __color_and_reset__(color, msg):
    return color + msg + style.RESET

def error(msg):
    """Returns message stylized as an error."""
    return __color_and_reset__(fore.RED, msg)

def notification(msg):
    """Returns message stylized as a notification."""
    return __color_and_reset__(fore.BLUE, msg)

def success(msg):
    """Returns message stylized as a success."""
    return __color_and_reset__(fore.GREEN, msg)
