import logging
import logging.config
import inspect
import re
from django.conf import settings
from middleware.context import var


class Logger():
    def __init__(self):
        config = {
            'version': 1,
            'formatters': {
                'standard': {
                    'class': 'logging.Formatter',
                    'format': '{"l":"%(levelname)s","t":"%(asctime)s",%(message)s}',
                    'datefmt': '%Y/%m/%d %H:%I:%S%z',
                },
            },
            'handlers': {
                'app': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'standard',
                },
            },
            'loggers': {
                'root': {
                    'handlers': ['app'],
                    'level': 'DEBUG',
                    'propagate': True,
                },
            },
        }
        logging.config.dictConfig(config)

    def _getPrevFile(self) -> dict[str, str]:
        previous_frame = inspect.currentframe().f_back.f_back.f_back
        file = re.sub(rf'^{settings.BASE_DIR}/', '',
                      previous_frame.f_code.co_filename)
        return {
            'file': file,
            'line': previous_frame.f_lineno,
        }

    def __getFmtMsg(self, msg: str, **kwargs) -> str:
        fmtMsg = f'"msg":"{msg}"'
        for key, val in kwargs.items():
            fmtMsg += f',"{key}":"{val}"'

        prev = self._getPrevFile()
        fmtMsg += f'"caller":"{prev["file"]}:{prev["line"]}"'
        return fmtMsg

    def __getRoot(self) -> logging.Logger:
        return logging.getLogger()

    def info(self, msg: str, **kwargs) -> None:
        self.__getRoot().info(self.__getFmtMsg(msg, **kwargs))

    def warning(self, msg: str, **kwargs) -> None:
        self.__getRoot().warning(self.__getFmtMsg(msg, **kwargs))

    def error(self, msg: str, **kwargs) -> None:
        self.__getRoot().error(self.__getFmtMsg(msg, **kwargs))

    def debug(self, msg: str, **kwargs) -> None:
        self.__getRoot().warning(self.__getFmtMsg(msg, **kwargs))


logger = Logger()
