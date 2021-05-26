from django.shortcuts import render


def posts_list(request):
    n = ['Vitaliy', 'Oleg', 'Tanya', 'Ksu']
    return render(request, 'blog/index.html',
                  context={'names': n})  # ключи словаря контекст, будут использованы в шаблоне
