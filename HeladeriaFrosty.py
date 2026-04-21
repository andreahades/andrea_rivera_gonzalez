# App Heladería Frosty

helados = [
    {"nombre": "Chocolate", "precio": 2.5, "stock": 100},
    {"nombre": "Vainilla", "precio": 2.0, "stock": 80},
    {"nombre": "Fresa", "precio": 3.0, "stock": 70}
]

def registrar_sabor(nombre, precio, stock):
    helado = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    helados.append(helado)
    print(f"\nSabor '{nombre}' registrado correctamente.")

def mostrar_helados():
    print("\n===== INVENTARIO DE HELADOS =====")
    
    if len(helados) == 0:
        print("No hay sabores registrados en el inventario.")
    else:
        for i, helado in enumerate(helados, start=1):
            print(f"{i}. {helado['nombre']} | Precio: ${helado['precio']} | Stock: {helado['stock']}")

def eliminar_sabor(nombre):
    for helado in helados:
        if helado["nombre"].lower() == nombre.lower():
            helados.remove(helado)
            print(f"\nSabor '{nombre}' eliminado correctamente.")
            return
    print(f"\nEl sabor '{nombre}' no fue encontrado en el inventario.")

def menu():
    while True:
        print("\n===================================")
        print("     HELADERÍA FROSTY DELIGHTS")
        print("===================================")
        print("1. Mostrar inventario")
        print("2. Agregar un sabor")
        print("3. Eliminar un sabor")
        print("4. Terminar el programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_helados()
        
        elif opcion == "2":
            nombre = input("Ingrese el nombre del sabor: ")
            
            try:
                precio = float(input("Ingrese el precio del sabor: "))
                stock = int(input("Ingrese la cantidad en stock: "))
                
                if precio < 0 or stock < 0:
                    print("\nError: el precio y el stock no pueden ser negativos.")
                else:
                    registrar_sabor(nombre, precio, stock)
            except ValueError:
                print("\nError: debe ingresar valores numéricos válidos para precio y stock.")
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del sabor que desea eliminar: ")
            eliminar_sabor(nombre)
        
        elif opcion == "4":
            print("\n¡Gracias por preferir Heladería Frosty Delights!")
            break
        
        else:
            print("\nOpción no válida. Intente nuevamente.")

menu()