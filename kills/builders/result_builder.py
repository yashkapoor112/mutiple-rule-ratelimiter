from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse


class ResultBuilder(object):

    def __init__(self):
        self.results = {}
        self.status_code = 1
        self.status_message = ""

    def get_json(self):
        content = {}
        content['status-code'] = self.status_code
        content['status-message'] = self.status_message
        content['data'] = self.results
        return content

    def get_json_response(self):
        content = self.get_json()
        return JsonResponse(content)

    def set_message(self, message):
        self.status_message = message
        return self

    def set_success(self):
        self.status_code = 1
        return self

    def set_fail(self):
        self.status_code = 0
        return self

    def get_response(self):
        content = self.get_json()
        return Response(content, status=self.status_code)

    def set_results(self, results):
        self.results = results
        return self