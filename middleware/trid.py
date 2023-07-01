from django.utils.deprecation import MiddlewareMixin


class TRID(MiddlewareMixin):
    def process_request(self, request):
        request.trid = 'this is trid'
