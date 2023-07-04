import datetime
import random


def gen_trid() -> str:
    date = datetime.datetime.now().strftime('%Y%m%d%H%I%S%f')
    ran_digit = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return f'{date}{ran_digit}'
