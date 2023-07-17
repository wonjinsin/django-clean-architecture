from django.http import JsonResponse
from rest_framework.utils.serializer_helpers import ReturnDict
from middleware.context import ContextMiddleware


def response(code: int, msg: str, data: ReturnDict | dict | None = None, custom_code: str | None = None) -> JsonResponse:
    print(type(data))
    res = {
        'trid': ContextMiddleware.get_trid(),
        'code': to_response_code(code),
        'msg': msg,
    }
    if data != None:
        res['data'] = data
    if custom_code != None:
        res['code'] = custom_code
    return JsonResponse(res, status=code)


def to_response_code(code: int) -> str:
    return f'{code:04}'
