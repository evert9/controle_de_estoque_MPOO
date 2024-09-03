from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(permanent=True, url='estoque/'), name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),

    path('estoque/<int:pk>/deletar/', views.deletar_produto, name='deletar-produto'),
    path('estoque/', views.estoque, name='estoque'),
    
    path('vendas/', views.vendas, name='vendas'),
    path('relatorios/', views.relatorios, name='relatorios'),

]
