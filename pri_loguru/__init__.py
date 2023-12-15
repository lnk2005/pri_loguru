import logging

from loguru import logger

from conf import EsHandlersConfig
from handler import EsHandlers


# TODO logger config update 使用一组表示 handler 的配置来构建 logger
# TODO set logger level
def get_logger(
        index: str = "debug",
        enable_console: bool = False,
        enable_es: bool = True,
        es_conf: EsHandlersConfig = None,
) -> logging.Logger:
    """
    a logger to catch logs

    if you want to turn off console output, must turn on es.

    :param es_conf: es handler 的配置
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
        _handler = EsHandlers(conf=es_conf)
        _logger.add(
            _handler,
            format="{time:YYYY-MM-DD HH:mm:ss!UTC+8} {level} {message}",
            backtrace=True,
            serialize=True,
        )

    _logger.info(f"set a logger for {index}")
    return logger


def get_es_handler(_conf: EsHandlersConfig = None) -> EsHandlers:
    """

    :param _conf: Handler config
    :return:
    """
    if not _conf:
        raise ValueError("conf can not be None")

    return EsHandlers(conf=_conf)
