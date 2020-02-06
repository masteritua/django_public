from django.db import models
from datetime import datetime
from time import time


class Logger(models.Model):
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=5)
    time_delta = models.CharField(max_length=11)
    user_id = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    def __init__(self, get_response):
        self.get_response = get_response

    @classmethod
    def to_db(cls, _path, time_delta, method, user_id):

        logger = cls(
            path=_path,
            time_delta=time_delta,
            method=method,
            user_id=user_id,
            created=datetime.now(),
        )

        logger.save()

    def __call__(self, request):
        path = request.path_info
        start_time = time()
        response = self.get_response(request)
        time_delta = time() - start_time

        if "admin" in path:
            if request.user.is_active:
                self.to_db(path, time_delta, request.method, request.user.id)

        return response
