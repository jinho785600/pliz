from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list', request=request, format=format),
        'errands': reverse('errand_list', request=request, format=format)
    })