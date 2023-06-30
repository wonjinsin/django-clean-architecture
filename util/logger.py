import logging
import inspect
import re
from django.conf import settings


class Logger():
    def __init__(self):
        logging.basicConfig(
            format='{"l":"%(levelname)s","t":"%(asctime)s",%(message)s}',
            level=logging.DEBUG,
            datefmt='%Y/%m/%d %H:%I:%S%z',
            encoding='utf-8'
        )

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

    def info(self, msg: str, **kwargs) -> None:
        logging.info(self.__getFmtMsg(msg, **kwargs))

    def warning(self, msg: str, **kwargs) -> None:
        logging.warning(self.__getFmtMsg(msg, **kwargs))

    def error(self, msg: str, **kwargs) -> None:
        logging.error(self.__getFmtMsg(msg, **kwargs))

    def debug(self, msg: str, **kwargs) -> None:
        logging.warning(self.__getFmtMsg(msg, **kwargs))


logger = Logger()
