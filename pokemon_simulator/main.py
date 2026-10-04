import gc
from clases.pokemon import Pokemon, PokemonFuego, PokemonAgua, PokemonPlanta


def pedir_numero(mensaje):
    valor = float(input(mensaje))
    if not Pokemon.validar_estadistica(valor):
        raise ValueError("El valor debe ser positivo.")
    return int(valor) if valor.is_integer() else valor


def mostrar_equipo(equipo):
    if not equipo:
        print("No hay Pokémon capturados.")
        return
    for i, pokemon in enumerate(equipo, start=1):
        print(f"{i}. {pokemon.nombre} - {pokemon._tipo} - Nivel {pokemon.nivel}")


def seleccionar_pokemon(equipo, mensaje="Selecciona un Pokémon: "):
    if not equipo:
        print("No hay Pokémon capturados.")
        return None

    mostrar_equipo(equipo)
    opcion = int(input(mensaje))
    if opcion < 1 or opcion > len(equipo):
        raise ValueError("Selección fuera de rango.")
    return equipo[opcion - 1]


def capturar_pokemon(equipo):
    nombre = input("Nombre del Pokémon: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")

    tipo = input("Tipo (Fuego/Agua/Planta): ").strip().capitalize()
    if tipo not in ("Fuego", "Agua", "Planta"):
        raise ValueError("El tipo debe ser Fuego, Agua o Planta.")

    ataque = pedir_numero("Ataque: ")
    defensa = pedir_numero("Defensa: ")
    salud = pedir_numero("Salud: ")

    clases = {
        "Fuego": PokemonFuego,
        "Agua": PokemonAgua,
        "Planta": PokemonPlanta
    }
    equipo.append(clases[tipo](nombre, ataque, defensa, salud))


def entrenar_pokemon(equipo):
    pokemon = seleccionar_pokemon(equipo)
    if pokemon is None:
        return

    print("Presiona Enter para mejorar todas las estadísticas.")
    entrada = input("O escribe estadísticas separadas por coma (ataque, defensa, salud): ").strip()

    if not entrada:
        pokemon.entrenar()
    else:
        stats = [x.strip().lower() for x in entrada.split(",") if x.strip()]
        if len(stats) > 3:
            raise ValueError("Sólo puedes indicar hasta tres estadísticas.")
        while len(stats) < 3:
            stats.append(None)
        pokemon.entrenar(stats[0], stats[1], stats[2])


def atacar(equipo):
    if len(equipo) < 2:
        print("Necesitas por lo menos dos Pokémon para realizar un ataque.")
        return

    atacante = seleccionar_pokemon(equipo, "Selecciona al atacante: ")
    objetivo = seleccionar_pokemon(equipo, "Selecciona al objetivo: ")

    if atacante is objetivo:
        print("Un Pokémon no puede atacarse a sí mismo.")
        return
    atacante.atacar(objetivo)


def ver_informacion(equipo):
    if not equipo:
        print("No hay Pokémon capturados.")
        return
    for pokemon in equipo:
        pokemon.mostrar_info()


def liberar_pokemon(equipo):
    pokemon = seleccionar_pokemon(equipo)
    if pokemon is None:
        return

    nombre = pokemon.nombre
    equipo.remove(pokemon)

    # Se marca y actualiza el contador aquí para que el resultado sea inmediato.
    if not pokemon._liberado:
        pokemon._liberado = True
        Pokemon._contador_pokemons = max(0, Pokemon._contador_pokemons - 1)
        print(f"{nombre} ha sido liberado ✨")
    del pokemon
    gc.collect()


def menu():
    equipo = []

    while True:
        print("\n========== SIMULADOR DE ENTRENAMIENTO POKÉMON ==========")
        print("1. Capturar Pokémon")
        print("2. Entrenar Pokémon")
        print("3. Atacar")
        print("4. Ver información")
        print("5. Total de Pokémon")
        print("6. Liberar Pokémon")
        print("7. Salir")

        try:
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                capturar_pokemon(equipo)
            elif opcion == "2":
                entrenar_pokemon(equipo)
            elif opcion == "3":
                atacar(equipo)
            elif opcion == "4":
                ver_informacion(equipo)
            elif opcion == "5":
                print(f"Total de Pokémon activos: {Pokemon.total_pokemons()}")
            elif opcion == "6":
                liberar_pokemon(equipo)
            elif opcion == "7":
                print("¡Gracias por usar el simulador Pokémon!")
                break
            else:
                print("Opción no válida. Elige un número del 1 al 7.")

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    menu()
