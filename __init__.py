import logging

from loguru import logger

from .handler import EsHandlers


# TODO logger config update
# TODO set logger level
def get_logger(
    index: str = "debug",
    queue_size: int = 1,
    enable_console: bool = False,
    enable_es: bool = True,
) -> logging.Logger:
    """
    a logger to catch logs

    if you want to turn off console output, must turn on es.

    :param index: if es is enabled, this is the of log
    :param queue_size: the size of cache queue
    :param enable_console: enable console to output logs
    :param enable_es: enable es to catch logs
    :return: logger
    """
    _logger = logger
    # Turn off console output if enable es and disable console
    if enable_es and not enable_console:
        _logger.remove(handler_id=None)

    # use es to collect log
    if enable_es:
        _handler = EsHandlers(index=index, queue_size=queue_size)
        _logger.add(
            _handler,
            format="{time:YYYY-MM-DD HH:mm:ss!UTC+8} {level} {message}",
            backtrace=True,
            serialize=True,
        )

    _logger.info(f"set a logger for {index}")
    return logger
