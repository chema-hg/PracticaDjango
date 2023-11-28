def importe_total_carro(request):
    cantidad = 0
    # comprobar si el usuario esta autenticado
    if request.user.is_authenticated:
        # recorremos el carro y vamos contando las cantidades de cada producto.
        if 'carro' in request.session:
            for key, value in request.session['carro'].items():
               cantidad = cantidad + int(value['cantidad'])                
    return {'cantidad_total_carro': cantidad}