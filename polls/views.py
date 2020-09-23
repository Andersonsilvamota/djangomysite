from django.http import HttpResponse

def index(request):
    return HttpResponse()

def sobre(request):
    print('equipe pweb')
    return HttpResponse('minha equipe pweb:anso,mayk,fontineles')

def turmaA(request):
    print('')
    return  HttpResponse('Professor: Leonardo')
def turmaB(request):
    print('')
    return  HttpResponse('Professor: Saulo')