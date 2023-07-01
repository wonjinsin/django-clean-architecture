from const.system import TRID
import datetime
import random
from django.utils.deprecation import MiddlewareMixin


class TRIDGenerator(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, TRID, self.__gen_trid())

    def __gen_trid(self) -> str:
        date = datetime.datetime.now().strftime('%Y%m%d%H%I%S%f')
        ran_digit = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        return f'{date}{ran_digit}'
