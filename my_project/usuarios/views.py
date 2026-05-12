from django.shortcuts import render
from .db import ConexionDB

# Create your views here.
def login_view(request):
    db = ConexionDB()

    sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s AND id_estado = 1"
    sql_tipo_usuario = "SELECT id_tipo_usuario FROM usuarios WHERE email = %s"
   
    if request.method == 'POST':

        # Aquí puedes agregar la lógica para autenticar al usuario
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_estado = db.verificar(sql, [email, password])

        if login_estado:

            tipo_usuario = db.consultar(sql_tipo_usuario, [email])

            if tipo_usuario[0]['id_tipo_usuario'] == 1:
                return render(request, 'portal_vendedor.html')
            
            
            elif tipo_usuario[0]['id_tipo_usuario'] == 2:
                return render(request, 'portal_supervisor.html')
        else:
            print("Login fallido")
        
        # Por ahora, simplemente renderizamos el mismo formulario
    return render(request, 'login.html')

