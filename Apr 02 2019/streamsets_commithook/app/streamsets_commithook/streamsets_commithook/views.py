from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world..............")

def commithook(request):
    return HttpResponse('Request received: <br>' + 
                        'GET Parameters: <br>' +
                        '<br>'.join(param+'='+str(request.GET[param]) for param in sorted(request.GET)) +
                        '<br><br>' +
                        'Post Parameters: <br>' +
                        '<br>'.join(param+'='+str(request.POST[param]) for param in sorted(request.POST)) +
                        '<br><br>' +
                        "META: <br>" +
                        '<br>'.join(param+'='+str(request.META[param]) for param in sorted(request.META)) +
                        '<br><br>' +
                        ''
                       )
