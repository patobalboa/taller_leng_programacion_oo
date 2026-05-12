from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # Aquí puedes agregar la lógica para autenticar al usuario
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Intento de login con username: {username} y password: {password}")
        # Por ahora, simplemente renderizamos el mismo formulario
    return render(request, 'login.html', {'username': username})

