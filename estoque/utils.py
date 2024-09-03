from django.db.models import Q

def construir_busca(request, campos):
    busca = request.GET.get('busca')
    filtros = Q()
    if busca:
        for campo in campos:
            filtros |= Q(**{f'{campo}__icontains': busca})
    return filtros

def validar_campos():
    pass