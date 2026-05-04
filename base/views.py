from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            # utilisateur connecté → page avec fonctionnalités
            return render(request, 'stages-emsi/home_authenticated.html', {})
        else:
            # utilisateur non connecté → brochures
            return render(request, 'stages-emsi/home_public.html', {})
    
    