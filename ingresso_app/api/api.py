from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.http import HttpRequest
import json

from ingresso_app.models import Estadio, Ingresso

@api_view(['GET'])
def lugares(request):
    """
    Pega informações de estádios.

    Query parameters:
        estadio_id: ID estadio
    """

    print("lugares")

    data = request.GET

    try: 
        estadio = Estadio.objects.get(id=data['estadio_id'])
    except Estadio.DoesNotExist:
        raise ParseError(f"Estadio não foi encontrado")

    ingressos_reservados = Ingresso.objects.filter(estadio=estadio)

    max_vaga = estadio.vagas

    print(max_vaga)

    ingressos = []

    i = 1
    while(i<=max_vaga):
        print("vaga: " + str(i))
        has_reserva = False
        for x in ingressos_reservados:
            if x.vaga == i:
                print("já ocupada")
                has_reserva = True
                break
        if(not has_reserva):
            ingressos.append({
                "assento": i,
                "status": 0,
                "nome": ""
                })
        else:
            ingressos.append({
                "assento": i,
                "status": 1,
                "nome": x.cliente
                })
        i += 1

    print(ingressos)

    return Response(ingressos)