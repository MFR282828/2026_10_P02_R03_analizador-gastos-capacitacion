# ==============================================================================
# SAGA DE REPOSITORIOS PYTHON 2026
# Repositorio: 2026_10_P02_R03_analizador-gastos-capacitacion
# Principio 2: Control de flujo y estructuras de datos básicas (Nivel: Consolidación)
# ==============================================================================

# --- REGISTROS DE EJEMPLO PRECARGADOS ---
gastos = [
    {"nombre": "Excel intermedio", "categoria": "Ofimática", "costo": 450.0, "participantes": 20},
    {"nombre": "Python básico", "categoria": "Tecnología", "costo": 900.0, "participantes": 15},
    {"nombre": "Seguridad laboral", "categoria": "Seguridad", "costo": 350.0, "participantes": 30},
    {"nombre": "Power BI", "categoria": "Tecnología", "costo": 750.0, "participantes": 12},
    {"nombre": "Liderazgo", "categoria": "Gestión", "costo": 600.0, "participantes": 18},
    {"nombre": "Comunicación", "categoria": "Gestión", "costo": 280.0, "participantes": 25}
]

PRESUPUESTO_INICIAL = 3000.0


# --- FUNCIONES DE VISUALIZACIÓN ---

def mostrar_registros(lista):
    """Muestra los registros de capacitación en formato tabular visual."""
    print("\n--------------------------------------------------------------------------------")
    print(f"{'Nombre':<22} | {'Categoría':<15} | {'Coste (S/)':<12} | {'Participantes':<13}")
    print("--------------------------------------------------------------------------------")
    
    if not lista:
        print("  [Información] La lista de gastos se encuentra vacía.")
        print("--------------------------------------------------------------------------------")
        return

    for reg in lista:
        print(f"{reg['nombre']:<22} | {reg['categoria']:<15} | {reg['costo']:<12.2f} | {reg['participantes']:<13}")
    print("--------------------------------------------------------------------------------")


# --- FUNCIONES DE ANÁLISIS, ACUMULACIÓN Y BÚSQUEDA ---

def calcular_metricas_y_conteos(lista):
    """Calcula el costo total, promedio y conteos por umbrales usando acumuladores y contadores."""
    if not lista:
        return 0.0, 0.0, 0, 0, 0

    costo_total = 0.0
    total_participantes = 0
    count_mayor_500 = 0
    count_mayor_igual_500 = 0

    for reg in lista:
        c = reg["costo"]
        p = reg["participantes"]
        
        costo_total += c
        total_participantes += p

        if c > 500.0:
            count_mayor_500 += 1
        if c >= 500.0:
            count_mayor_igual_500 += 1

    promedio_costo = costo_total / len(lista)
    return costo_total, promedio_costo, count_mayor_500, count_mayor_igual_500, total_participantes


def encontrar_extremos_manualmente(lista):
    """Encuentra manualmente los registros de mayor y menor coste mediante iteración comparativa."""
    if not lista:
        return None, None

    registro_max = lista[0]
    registro_min = lista[0]

    for reg in lista[1:]:
        if reg["costo"] > registro_max["costo"]:
            registro_max = reg
        if reg["costo"] < registro_min["costo"]:
            registro_min = reg

    return registro_max, registro_min


def ordenar_manualmente(lista, ascendente=True):
    """Ordena manualmente los registros por coste creando una copia para no alterar los originales."""
    if not lista:
        return []

    # Copia manual profunda para preservar los datos de origen intactos
    copia = []
    for item in lista:
        copia.append(dict(item))

    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            debe_intercambiar = False
            if ascendente and copia[j]["costo"] > copia[j + 1]["costo"]:
                debe_intercambiar = True
            elif not ascendente and copia[j]["costo"] < copia[j + 1]["costo"]:
                debe_intercambiar = True

            if debe_intercambiar:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp

    return copia


# --- FUNCIONES DE FILTRADO Y EVALUACIÓN PRESUPUESTARIA ---

def filtrar_registros(lista, categoria=None, limite_costo=None, es_maximo=True):
    """Filtra la lista de gastos según categoría o un importe de corte."""
    coincidencias = []
    
    for reg in lista:
        cumple_categoria = True
        cumple_costo = True

        if categoria is not None:
            if reg["categoria"].lower() != categoria.lower():
                cumple_categoria = False

        if limite_costo is not None:
            if es_maximo and reg["costo"] > limite_costo:
                cumple_costo = False
            elif not es_maximo and reg["costo"] < limite_costo:
                cumple_costo = False

        if cumple_categoria and cumple_costo:
            coincidencias.append(reg)

    return coincidencias


def evaluar_presupuesto(costo_total, presupuesto):
    """Evalúa el estado financiero comparando el gasto total contra el presupuesto disponible."""
    print("\n========================================")
    print("        INFORME DE PRESUPUESTO          ")
    print("========================================")
    print(f"Presupuesto inicial:        S/ {presupuesto:.2f}")
    print(f"Coste total acumulado:      S/ {costo_total:.2f}")

    if presupuesto <= 0:
        print("Estado: Presupuesto no válido")
        print("========================================")
        return

    saldo_diferencia = presupuesto - costo_total
    porcentaje = (costo_total / presupuesto) * 100.0 if presupuesto > 0 else 0.0

    print(f"Porcentaje de presupuesto:  {porcentaje:.2f} %")
    print("----------------------------------------")

    if costo_total < presupuesto:
        print(f"Estado: Dentro del presupuesto (Saldo a favor: S/ {saldo_diferencia:.2f})")
    elif costo_total == presupuesto:
        print("Estado: Presupuesto utilizado al 100 % (Saldo: S/ 0.00)")
    else:
        exceso = costo_total - presupuesto
        print(f"Estado: Exceso presupuestario (Déficit / Importe excedido: S/ {exceso:.2f})")

    print("========================================")


# --- MENÚ INTERACTIVO Y FLUJO PRINCIPAL ---

def solicitar_float_positivo(mensaje):
    """Solicita un importe numérico válido rechazando letras o montos negativos."""
    while True:
        entrada = input(mensaje).strip()
        try:
            val = float(entrada)
            if val >= 0:
                return val
            print("  [Error] Debe ingresar un número mayor o igual a 0.")
        except ValueError:
            print("  [Error] Entrada no válida. Ingrese un valor numérico.")


def menu_principal():
    """Ejecuta el menú del Analizador de Gastos de Capacitación."""
    # Referencia local para permitir simulación de lista vacía
    datos_actuales = gastos

    while True:
        print("\n================================================")
        print(" ANALIZADOR DE GASTOS DE CAPACITACIÓN (P02_R03)")
        print("================================================")
        print(" 1. Mostrar todos los registros")
        print(" 2. Calcular coste total y promedio")
        print(" 3. Contar registros por umbrales (S/ 500)")
        print(" 4. Encontrar registros de mayor y menor coste")
        print(" 5. Filtrar registros por categoría o importe")
        print(" 6. Ordenar registros manualmente por coste")
        print(" 7. Informe de presupuesto frente al total")
        print(" 8. Alternar estado de lista (Con datos / Lista vacía)")
        print(" 9. Salir")
        print("================================================")

        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            print("\n--- REGISTROS ACTUALES ---")
            mostrar_registros(datos_actuales)

        elif opcion == "2":
            total, promedio, _, _, part = calcular_metricas_y_conteos(datos_actuales)
            print("\n--- RESUMEN DE TOTALES Y PROMEDIOS ---")
            print(f"Número de actividades:        {len(datos_actuales)}")
            print(f"Coste total acumulado:        S/ {total:.2f}")
            print(f"Coste promedio por actividad: S/ {promedio:.2f}")
            print(f"Total de participantes:       {part}")
            if part > 0:
                print(f"Coste promedio por persona:   S/ {(total / part):.2f}")

        elif opcion == "3":
            _, _, c_mayor, c_mayor_igual, _ = calcular_metricas_y_conteos(datos_actuales)
            print("\n--- CONTEO POR UMBRAL DE S/ 500 ---")
            print(f"Actividades con coste estrictamente mayor a S/ 500 (> 500):  {c_mayor}")
            print(f"Actividades con coste mayor o igual a S/ 500 (>= 500):        {c_mayor_igual}")

        elif opcion == "4":
            reg_max, reg_min = encontrar_extremos_manualmente(datos_actuales)
            print("\n--- EXTREMOS DE COSTE ---")
            if reg_max and reg_min:
                print(f"Mayor coste: {reg_max['nombre']} ({reg_max['categoria']}) - S/ {reg_max['costo']:.2f}")
                print(f"Menor coste: {reg_min['nombre']} ({reg_min['categoria']}) - S/ {reg_min['costo']:.2f}")
            else:
                print("  [Información] Lista vacía. No es posible identificar extremos.")

        elif opcion == "5":
            print("\n--- OPCONES DE FILTRO ---")
            print("a. Filtrar por Categoría")
            print("b. Filtrar por Coste máximo permitida")
            sub_opcion = input("Elija sub-opción (a/b): ").strip().lower()

            if sub_opcion == 'a':
                cat = input("Ingrese la categoría a buscar: ").strip()
                res = filtrar_registros(datos_actuales, categoria=cat)
                print(f"\nResultados encontrados para categoría '{cat}':")
                mostrar_registros(res)
            elif sub_opcion == 'b':
                limite = solicitar_float_positivo("Ingrese el coste máximo: ")
                res = filtrar_registros(datos_actuales, limite_costo=limite, es_maximo=True)
                print(f"\nResultados con coste menor o igual a S/ {limite:.2f}:")
                mostrar_registros(res)
            else:
                print("  [Error] Sub-opción no válida.")

        elif opcion == "6":
            print("\n--- ORDENAMIENTO MANUAL (BUBBLE SORT) ---")
            print("1. Ascendente (Menor a Mayor)")
            print("2. Descendente (Mayor a Menor)")
            sentido = input("Seleccione el orden (1/2): ").strip()

            if sentido == "1":
                ordenados = ordenar_manualmente(datos_actuales, ascendente=True)
                print("\n[Vista Ordenada Ascendente - Datos originales sin cambios]")
                mostrar_registros(ordenados)
            elif sentido == "2":
                ordenados = ordenar_manualmente(datos_actuales, ascendente=False)
                print("\n[Vista Ordenada Descendente - Datos originales sin cambios]")
                mostrar_registros(ordenados)
            else:
                print("  [Error] Opción de ordenamiento no válida.")

        elif opcion == "7":
            total, _, _, _, _ = calcular_metricas_y_conteos(datos_actuales)
            evaluar_presupuesto(total, PRESUPUESTO_INICIAL)

        elif opcion == "8":
            if datos_actuales:
                datos_actuales = []
                print("\n  [Estado cambiado] La lista de datos ahora está VACÍA para pruebas.")
            else:
                datos_actuales = gastos
                print("\n  [Estado cambiado] La lista de datos fue RESTAURADA con los 6 registros.")

        elif opcion == "9":
            print("\n  Gracias por utilizar el Analizador de Gastos de Capacitación. ¡Hasta pronto!")
            break
        else:
            print("\n  [Error] Opción no válida. Ingrese un número entre 1 y 9.")


if __name__ == "__main__":
    menu_principal()