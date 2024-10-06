from urllib.parse import urlencode
from copy import deepcopy


# Middleware для работы pagination(пагинации страниц) для всего проекта
class QueryParamsInjectorMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        query_params = deepcopy(request.GET)
        if 'page' in query_params:
            del query_params['page']
        request.query_params = urlencode(query_params)

        response = self.get_response(request)

        return response
