from django.http import HttpRequest,JsonResponse

def test(request):
    return HttpRequest("faraz test django again")