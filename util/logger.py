import logging
import inspect
from django.conf import settings

logging.basicConfig(
    format='{"l":"%(levelname)s","t":"%(asctime)s",%(message)s,"caller":"%(pathname)s:%(lineno)d"}',
    level=logging.DEBUG,
    datefmt='%Y/%m/%d %H:%I:%S%z',
    encoding='utf-8'
)
l = logging

# class Logger():
#     def __init__(self):

#     def __getFmtMsg(self, msg: str, **kwargs) -> str:
#         fmtMsg = f'"msg":"{msg}"'
#         for key, val in kwargs.items():
#             fmtMsg += f',"{key}":"{val}"'
#         return fmtMsg

#     def warning(self, msg: str, **kwargs) -> None:
#         logging.warning(self.__getFmtMsg(msg, **kwargs))
