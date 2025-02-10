from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from client.models import Dato
import json

def historial(request):
    datos_list = Dato.objects.all().order_by('-fecha', '-hora')
    paginator = Paginator(datos_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'historial.html', {'page_obj': page_obj})

def index(request):
    ultimo = Dato.objects.all().order_by('-fecha', '-hora').first()
    
    ph = {
        "valor": ultimo.ph,
        "rotacion": min(180 * ultimo.ph / 14, 180),
        "irotacion": -1*min(180 * ultimo.ph / 14, 180),
        }
    
    temperatura = {
        "valor": ultimo.temperatura,
        "rotacion": min(ultimo.temperatura + 55, 180),
        "irotacion": -1 * min(ultimo.temperatura + 55, 180),
        }
    
    turbidez = {
        "valor": ultimo.turbidez,
        "rotacion": min(180 * ultimo.turbidez / 1100, 180),
        "irotacion": -1 * min(180 * ultimo.turbidez / 1100, 180),
        }
    
    tds = {
        "valor": ultimo.tds,
        "rotacion": min(180 * ultimo.tds / 1000, 180),
        "irotacion": -1 * min(180 * ultimo.tds / 1000, 180),
        }
    
    co2 = {
        "valor": ultimo.co2,
        "rotacion": min(180 * ultimo.co2 / 5000, 180),
        "irotacion": -1*min(180 * ultimo.co2 / 5000, 180),
        }
    
    return render(request, 'registro.html', {'dato': ultimo,'ph': ph, 'temperatura': temperatura, 'turbidez': turbidez, 'tds': tds, 'co2': co2})

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ph = data.get('ph')
        temperatura = data.get('temperatura')
        turbidez = data.get('turbidez')
        tds = data.get('tds')
        co2 = data.get('co2')

        Dato.objects.create(ph=ph, temperatura=temperatura, turbidez=turbidez, tds=tds, co2=co2)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'}, status=400)
