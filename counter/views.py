from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from counter.models import Counter


@csrf_exempt
def index(request):

    # Get the current counter
    counter = Counter.objects.first()

    # If there is no counter, create one
    if not counter:
        counter = Counter.objects.create()

    if request.method == 'GET':
        return JsonResponse({'count': counter.count})

    if request.method == 'POST':
        return JsonResponse({'count': counter.increment()})
