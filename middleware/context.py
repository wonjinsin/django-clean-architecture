from contextvars import ContextVar
import datetime

var: ContextVar[str] = ContextVar(
    'var', default=datetime.datetime.now().strftime('%Y%m%d%H%I%S%f'))

print(var)
