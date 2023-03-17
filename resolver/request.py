# -*- coding: utf-8 -*-

import requests

from validator_collection import checkers
from sceptre.resolvers import Resolver
from sceptre.exceptions import SceptreException


class InvalidResolverArgumentValueError(SceptreException):
    """
    Error raised if a resolver's argument value is invalid.
    """

    pass


class Request(Resolver):
    """
    Resolve data from a REST API endpoint.
    """

    def _make_request(self, url):
        """
        Make a request to a REST API endpoint
        :param url: The url endpoint reference
        """
        content = None
        response = requests.get(url)
        content = response.text
        response.raise_for_status()
        return content

    def resolve(self):
        """
        This method is invoked by Sceptre

        :returns: Response from the request
        :rtype: str
        """

        arg = self.argument
        if checkers.is_url(arg):
            response = self._make_request(arg)
        else:
            raise InvalidResolverArgumentValueError(f"Invalid argument: {arg}")

        return response
