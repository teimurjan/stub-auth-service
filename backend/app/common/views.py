from flask import request
from flask.views import MethodView
from flask import jsonify


class ApiView(MethodView):
    service_factory = None

    def __init__(self, *args, **kwargs):
        self.service_factory = kwargs.get('service_factory')

    def dispatch_request(self, *args, **kwargs):
        handler = getattr(self, request.method.lower(), None)
        if handler is None and request.method == 'HEAD':
            handler = getattr(self, 'get', None)
        assert handler is not None, 'Unimplemented method %r' % request.method

        if not self.service_factory:
            raise Exception('Service factory is None')

        service = self.service_factory.create()
        body, status = handler(service=service, *args, **kwargs)
        response = jsonify(body)
        response.status_code = status
        return response
