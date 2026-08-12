from django.http import HttpRequest,JsonResponse

def faraz(request):
    return HttpRequest("<h1>faraz test django again<h1>")

def testjson(request):
    return JsonResponse({"name":"faraz"})