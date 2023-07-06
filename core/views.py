from django.shortcuts import render
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.shortcuts import redirect
import requests
#pip install request

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[4]
    venta = Venta()
    venta.total = total
    venta.cliente = request.user
    venta.save()
    for item in carro:
        detalle = Detalle()
        detalle.venta = venta
        detalle.producto = Producto.objects.get(codigo=item[0])
        detalle.precio= item[2]
        detalle.cantidad = item[3]
        detalle.save()
    request.session["carro"] = []
    return redirect(to="carrito")


def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[3] > 1:
                item[3] -= 1
                item[4] = item[2] * item[3]
            else:
                carro.remove(item)
            request.session["carro"] = carro
            return redirect(to="carrito")

def addtocar(request, codigo, precio_oferta):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[3] += 1
            item[4] = item[2] * item[3]
            break
    else:
        if producto.oferta:
            carro.append([codigo, producto.nombre,
                int(precio_oferta), 1, int(precio_oferta)])
        else:
            carro.append([codigo, producto.nombre,
            producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="home")

def addtocar2(request, codigo,):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[3] += 1
            item[4] = item[2] * item[3]
            break
    else:
        carro.append([codigo, producto.nombre,
        producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="home")

# 0 codigo
# 1 nombre
# 2 precio
# 3 cantidad
# 4 total


def carrito(request):
    return render(request, 'core/carrito.html', 
        {"carro":request.session.get("carro", [])})

def limpiar(request):
    request.session.flush()
    return redirect(to="home")
    
# Create your views here.
def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:        
        form = Registro()
    return render(request, 'core/registro.html', {'form':form})

def home(request):
    plantas = Producto.objects.all()
    context = {'plantas':plantas}
    suscrito(request, context)
    print(context)
    return render(request, 'core/index.html', {'plantas':plantas})

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]



def quienes(request):
    return render(request, 'core/quienes.html')

def plantas(request):
    plantas = Producto.objects.all()
    return render(request, 'core/plantas.html', {'plantas':plantas})

def producto(request, codigo):
    plantas = Producto.objects.get(codigo=codigo)
    return render(request, 'core/producto.html', {'codigo':plantas.codigo,'nombre':plantas.nombre,'imagen':plantas.imagen, 'oferta':plantas.oferta,
                'stock':plantas.stock, 'precio':plantas.precio, 'descripcion':plantas.descripcion, 'tachado':plantas.tachado})

def logout(request):
    return logout_then_login(request, login_url="login")

def descuentos(request):
    descuentos = descuento.objects.all()
    return render(request, 'core/descuentos.html', {'lista_descuentos':descuentos})

def historial_compras(request):
    historial = Venta.objects.all()
    return render(request, 'core/historial_compras.html', {'historial':historial})


def producto_lista(request):
    plantas = Producto.objects.all()
    return render(request, 'core/productos_lista.html', {'plantas':plantas})


# Productos

def crearProducto(request):
    datos = {"form":productoForm()}
    if request.method == "POST":
        form = productoForm(request.POST,files=request.FILES)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto agregado!."
    return render(request, 'core/productos_crud.html', datos)

def modificarProducto(request, id):
    productos = Producto.objects.get(codigo=id)
    datos = {'form': productoForm(instance=productos)}
    if request.method == "POST":
        form = productoForm(request.POST,files=request.FILES, instance=productos)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado!"
            datos["form"] = form
    return render(request, 'core/productos_crud.html', datos)

def eliminarProducto(request, id):
    productos = Producto.objects.get(codigo=id)
    productos.delete()
    return redirect(to = "producto_lista")


# Descuentos

def crearDescuento(request):
    datos = {"form":promocionesForm()}
    if request.method == "POST":
        form = promocionesForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Descuento agregado!."
    return render(request, 'core/descuento_crud.html', datos)

def modificarDescuento(request, id):
    Descuento = descuento.objects.get(idDescuento=id)
    datos = {'form': promocionesForm(instance=Descuento)}
    if request.method == "POST":
        form = promocionesForm(request.POST, instance=Descuento)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Descuento Modificado!"
            datos["form"] = form
    return render(request, 'core/descuento_crud.html', datos)


def eliminarDescuento(request,id):
    Descuento = descuento.objects.get(idDescuento=id)
    Descuento.delete()
    return redirect(to = "descuentos")
