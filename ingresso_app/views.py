from django.shortcuts import render
from ingresso_app.models import Estadio, Ingresso
from django.http import HttpRequest

# Create your views here.
def hello_world(request):
    estadio_id = 1 #request.GET['estadio_id']
    ingressos = list(ingressos_disponiveis(estadio_id))
    print(ingressos)
    return render(request, 'hello_world.html', {'ingressos':ingressos})

def comprar_ingresso(request: HttpRequest):
    if request.method == 'POST':
        print("is post")
        usuario = request.POST['nome']
        estadio_id = 1 #request.POST['estadio_id']
        assentos = request.POST.getlist('assento')

        for assento in assentos:
                
            ingresso = Ingresso.objects.filter(
                vaga=assento
            ).first()
            print(ingresso)
            if(ingresso):
                print("ingresso já reservado")
                return

            ingresso = Ingresso.objects.create(
                cliente = usuario,
                vaga = assento,
                estadio_id = estadio_id
            )

    estadio_id = 1 #request.POST['estadio_id']
    ingressos = list(ingressos_disponiveis(estadio_id))
    print(ingressos)
    return render(request, 'hello_world.html', {'ingressos':ingressos})

def ingressos_disponiveis(estadio_id):
    try: 
        estadio = Estadio.objects.get(id=estadio_id)
    except Usuario.DoesNotExist:
        raise ParseError(f"Estadio com id={estadio_id} não foi encontrado")

    ingressos_reservados = Ingresso.objects.filter(estadio=estadio)

    max_vaga = estadio.vagas

    print(max_vaga)

    ingressos_disponiveis = []

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
            ingressos_disponiveis.append(i)
        i += 1

    print(ingressos_disponiveis)

    return ingressos_disponiveis