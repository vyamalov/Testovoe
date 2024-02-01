from drf_multiple_model.views import FlatMultipleModelAPIView
from .serializers import *


class AZSAPIView(FlatMultipleModelAPIView):
    querylist = [
        {'queryset': Source1.objects.all(), 'serializer_class': Source1Serializer},
        {'queryset': Source2.objects.all(), 'serializer_class': Source2Serializer},
    ]
