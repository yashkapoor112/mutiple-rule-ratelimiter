from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse


class ResultBuilder(object):
    """
    Builds json response for API calls

    """
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
        """
        Sets the status message for a response

        :param message: string
        :return: ResultBuilder()
        """
        self.status_message = message
        return self

    def set_success(self):
        """
        Sets the status code 1 for a response

        :return: ResultBuilder()
        """
        self.status_code = 1
        return self

    def set_fail(self):
        """
        Sets the status code 0 for a response

        :return: ResultBuilder()
        """
        self.status_code = 0
        return self

    def get_response(self):
        """
        Gets the JSON and gives a Reponse object
        :return:
        """
        content = self.get_json()
        return Response(content, status=self.status_code)

    def set_results(self, results):
        """
        Sets the result field in the object

        :param results: dict
        :return: ResultBuilder()
        """
        self.results = results
        return self