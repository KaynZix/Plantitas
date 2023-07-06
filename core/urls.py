from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", home, name="home"),    
    path("login", LoginView.as_view(template_name="core/login.html"), name="login"),    
    path("logout", logout, name="logout"),
    path("quienes", quienes, name="quienes"),    
    path("registro", registro, name="registro"),
    path("limpiar", limpiar, name="limpiar"),
    path("carrito", carrito, name="carrito"),
    path("comprar", comprar, name="comprar"),
    path("plantas", plantas, name="plantas"),
    path("producto/<codigo>", producto, name="producto"),
    path("addtocar/<codigo>/<precio_oferta>", addtocar, name="addtocar"),
    path("addtocar2/<codigo>", addtocar2, name="addtocar2"),
    path("dropitem/<codigo>", dropitem, name="dropitem"),
    path("descuentos", descuentos ,name="descuentos"),
    path("historial_compras", historial_compras ,name="historial_compras"),
    path("producto_lista", producto_lista ,name="producto_lista"),
    path('crearproducto', crearProducto, name="crearProducto"),



    path('crearDescuento', crearDescuento, name="crearDescuento"),
    path('modificarDescuento/<id>', modificarDescuento, name="modificarDescuento"),
    path('eliminarDescuento/<id>', eliminarDescuento, name="eliminarDescuento"),

 # Productos

    path('crearproducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),


]
