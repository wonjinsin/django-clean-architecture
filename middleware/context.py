from const.system import TRID
from django.utils.deprecation import MiddlewareMixin
import logging
from util.time import gen_trid
from const.system import TRID_DEFAULT


class ContextMiddleware(MiddlewareMixin):
    __ctx = {
        'trid': TRID_DEFAULT,
    }

    @classmethod
    def get_trid(cls):
        return cls.__ctx.get(TRID)

    def process_request(self, _):
        self.__ctx['trid'] = gen_trid()


class TRIDFilter(logging.Filter):
    def filter(self, record):
        record.trid = ContextMiddleware.get_trid()
        return True
