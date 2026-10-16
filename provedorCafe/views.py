from django.shortcuts import render
from django.shortcuts import render
from . import services

def index(request):
    return render(request,'index.html')
def cardapio(request):
    # Busca os dados da API externa
    cafes_brutos = services.buscar_cafes_da_api()
    
    # Exemplo: aplicando preços customizados dinamicamente no Python
    cardapio_com_preco = []
    for cafe in cafes_brutos:
        # Cria um dicionário enriquecido com preço baseado na quantidade de ingredientes
        ingredientes = cafe.get('ingredients', [])
        preco_calculado = 9.90 + (len(ingredientes) * 2.00)

        cafe_info = {
            'id': cafe.get('id'),
            'title': cafe.get('title'),
            'description': cafe.get('description'),
            'image': cafe.get('image'),
            'ingredients': ingredientes,
            'price': round(preco_calculado, 2) # Arredonda para 2 casas decimais
        }
        cardapio_com_preco.append(cafe_info)


    context = {
        'cafes': cardapio_com_preco
    }
    
    return render(request, 'cardapio.html', context)