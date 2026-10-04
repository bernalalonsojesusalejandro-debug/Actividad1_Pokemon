# Simulador de Entrenamiento Pokémon

Actividad de Programación Orientada a Objetos para practicar herencia, reutilización de miembros, redefinición de métodos y polimorfismo.

## Estructura

```text
pokemon_simulator/
├── main.py
├── README.md
└── clases/
    └── pokemon.py
```

## Requisitos

- Python 3.10 o superior.
- No requiere librerías externas.

## Ejecución

Desde una terminal, entra a la carpeta del proyecto y ejecuta:

```bash
python main.py
```

## Funciones del menú

1. Capturar Pokémon de tipo Fuego, Agua o Planta.
2. Entrenar un Pokémon y aumentar su nivel.
3. Atacar a otro Pokémon aplicando ventajas y desventajas de tipo.
4. Consultar la información del equipo.
5. Consultar el total de Pokémon activos.
6. Liberar un Pokémon.
7. Salir.

## Conceptos utilizados

- Clase base `Pokemon`.
- Herencia con `PokemonFuego`, `PokemonAgua` y `PokemonPlanta`.
- Uso de `super()`.
- Redefinición de `atacar()` y extensión de `mostrar_info()`.
- Método de clase `total_pokemons()`.
- Método estático `validar_estadistica()`.
- Manejo de errores con `try/except`.
- Polimorfismo al trabajar con todos los tipos de Pokémon desde el mismo equipo.
