from django.shortcuts import render

# Create your views here.

from catalogo.models import Genero, Linguagem, Autor, Livro, ExemplarLivro

def index(request):

    # Contando o número de livros e exemplares:
    num_livros = Livro.objects.all().count()
    num_exemplares = ExemplarLivro.objects.all().count()

    # Contando a quantidade de exemplares disponíveis (situacao = 'd')
    num_exemplares_disponiveis = ExemplarLivro.objects.filter(situacao__exact='d').count()

    # Contando o número de autores. A opção 'all()' é implícita por padrão:
    num_autores = Autor.objects.count()

    contexto = {
        'num_livros': num_livros,
        'num_exemplares': num_exemplares,
        'num_exemplares_disponiveis': num_exemplares_disponiveis,
        'num_autores': num_autores,
    }

    # Renderizando o template index.html com os dados da variável contexto:
    return render(request, 'index.html', context=contexto)
