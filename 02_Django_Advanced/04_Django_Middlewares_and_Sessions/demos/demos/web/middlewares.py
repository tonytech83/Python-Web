import time

from django.utils.deprecation import MiddlewareMixin

"""
Middleware should be callable -> class or function
"""


# Function middleware - `get_response` is a func
def measure_execution_time(get_response):
    def middleware(request, *args, **kwargs):
        # Before the request
        start_time = time.time()

        result = get_response(request, *args, **kwargs)

        # After the request
        end_time = time.time()

        print(f'Method:{request.method} with path: {request.path} was executed in {end_time - start_time} seconds')

        return result

    return middleware


# Class middleware
class MeasureExecutionTimeMiddleware(MiddlewareMixin):
    # Before
    def process_request(self, request):
        self.start_time = time.time()

    # After
    def process_response(self, request, response):
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time
        print(f'Method:{request.method} with path: {request.path} was executed in {self.duration} seconds')

        return response
