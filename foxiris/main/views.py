
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')

@login_required
def about(request):
    return render(request, 'main/about.html')


@login_required
def projects(request):
    return render(request, 'main/projects.html')
