from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Cupon
from .forms import CuponFormulario


@require_POST
def aplicar_cupon(request):
    now = timezone.now()
    form = CuponFormulario(request.POST)
    if form.is_valid():
        codigo = form.cleaned_data['codigo']
        try:
            cupon = Cupon.objects.get(codigo__iexact=codigo,
                                      valido_desde__lte=now,
                                      valido_hasta__gte=now,
                                      activo=True)
            request.session['cupon_id'] = cupon.id
        except Cupon.DoesNotExist:
            request.session['cupon_id'] = None
    return redirect('carro:mostrar')
