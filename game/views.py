from . import random
from django.shortcuts import render, redirect

def iniciar_jogo(request):
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    mensagem = "Tente adivinhar o número entre 1 e 100!"

    return render(request, 'game/jogar.html', {
        'numero_aleatorio' : numero_aleatorio,
        'tentaativas' : tentativas,
        'mensagem' : mensagem
    })

def jogar(request):
    if request.method == "POST":
        try:
            palpite = int(request.POST.get('palpite'))
            numero_aleatorio = int(request.POST.get('numero_aleatorio'))
            tentativas = int(request.POST.get('tntativas'))

            print('palpites: ', palpite, '/', 'Correto: ', numero_aleatorio)

            if palpite < numero_aleatorio:
                mensagem = "Muito baixo! Tente novamente."
            elif palpite > numero_aleatorio:
                mensagem = "Muito alto! Tente novamente"
            else:
                return render(request, 'game/vitoria.html', {
                    'numero_aleatorio' : numero_aleatorio,
                    'tentativas' : tentativas,
                })
        except (ValueError, TypeError):
            mensagem = "Por favor, insira um valor válido!"
            numero_aleatorio = random.randint(1, 100)
            tentativas = 0
        
        return render(request, 'game/jogar.html', {
            'numero_aleatorio': numero_aleatorio,
            'tentativas' : tentativas,
            'mensagem' : mensagem
        })
    
    return redirect('iniciar_jogo')
