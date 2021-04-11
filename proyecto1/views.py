from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Marcos! Esta es nuestra primera pagina con Django!!") 

def despedida(request):
    return HttpResponse("Nos vemos la proxima vez, te deseo suerte Mar!")

def saludo2(request): 
    
    doc_externo= open("C:/Users/chris/Desktop/django/proyecto1/proyecto1/plantillas/miplantilla.html")
    
    plt= Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx= Context()
    
    documento= plt.render(ctx)
    
    return HttpResponse(documento)
    