print("Gestion de Inventario");

Inventario = {
    "cajas": 7,
    "bolsas": 40,
    "paquetes": 15,
    "esferos": 25
};

#funcion de menu
def menu():
    
    opciones = ["Agregar producto", "Eliminar producto", "Mostrar inventario", "Salir del Programa"]
    
    while True:
        print();
        print("Manejo de Inventario")
        print("Seleccione una opción:")
        
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

        n = input("Ingrese una opción: ")
        
        if n.isdigit() and 1 <= int(n) <= 4:
            return int(n);
        else:
            print("Opción inválida. Intente de nuevo.");

#revisa si el producto existe para solo aumentar su cantidad o si no existe para agregarlo
def agregar_producto(inv_productos, nombre_producto, cantidad_producto):
    if str(nombre_producto) in inv_productos:
        inv_productos[nombre_producto] += cantidad_producto;
    else:
        inv_productos[nombre_producto] = cantidad_producto;

# elimina producto y si no existe devuelve no encontrado
def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
    else:
        print("Producto no encontrado.")

def opcion(num, inventario_productos):
    if num == 1:
        producto = input("Ingrese el nombre del producto: ");
        cantidad = input("Ingrese la cantidad: ");
        agregar_producto(inventario_productos, producto, cantidad);
        return True;
    elif num == 2:
        producto = input("Ingrese el nombre del producto a eliminar: ");
        eliminar_producto(inventario_productos, producto);
        return True;
    elif num == 3:
        print("Inventario");
        for productos, cantidades in inventario_productos.items():
            print(f"{productos}: {cantidades} unidades");
        return True;
    else:
        return False;


#Programa Principal

while True:
    seleccion = menu();
    if not opcion(seleccion, Inventario):
        break;  

print("Fin del Programa");