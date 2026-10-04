class Pokemon:
    _contador_pokemons = 0

    def __init__(self, nombre, ataque, defensa, salud):
        if not self.validar_estadistica(ataque) or not self.validar_estadistica(defensa) or not self.validar_estadistica(salud):
            raise ValueError("Las estadísticas deben ser números positivos.")

        self.nombre = nombre
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud
        self._tipo = "Normal"
        self._liberado = False
        Pokemon._contador_pokemons += 1
        print(f"¡{self.nombre} ha sido capturado! 🎉")

    def __del__(self):
        if hasattr(self, "_liberado") and not self._liberado:
            self._liberado = True
            Pokemon._contador_pokemons = max(0, Pokemon._contador_pokemons - 1)
            if hasattr(self, "nombre"):
                print(f"{self.nombre} ha sido liberado ✨")

    @staticmethod
    def validar_estadistica(valor):
        return isinstance(valor, (int, float)) and valor > 0

    @classmethod
    def total_pokemons(cls):
        return Pokemon._contador_pokemons

    def subir_nivel(self):
        self.nivel += 1
        self.ataque += 2
        self.defensa += 2
        self.salud_maxima += 5
        self.salud += 5

    def entrenar(self, stat1=None, stat2=None, stat3=None):
        self.subir_nivel()

        # Si no se indican estadísticas, subir_nivel ya mejoró las tres.
        if stat1 is None and stat2 is None and stat3 is None:
            print(f"{self.nombre} subió al nivel {self.nivel}.")
            return

        # Con argumentos se da una mejora extra a las estadísticas indicadas.
        for stat in (stat1, stat2, stat3):
            if stat is None:
                continue
            stat = stat.lower()
            if stat == "ataque":
                self.ataque += 2
            elif stat == "defensa":
                self.defensa += 2
            elif stat == "salud":
                self.salud_maxima += 5
                self.salud += 5
            else:
                raise ValueError(f"Estadística no válida: {stat}")

        print(f"{self.nombre} subió al nivel {self.nivel}.")

    def _calcular_dano_base(self, objetivo):
        return max(1, self.ataque - objetivo.defensa)

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} está debilitado y no puede atacar.")
            return
        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya está debilitado.")
            return

        dano = self._calcular_dano_base(objetivo)
        print(f"{self.nombre} ataca a {objetivo.nombre} y causa {dano} puntos de daño.")
        objetivo.recibir_dano(dano)

    def recibir_dano(self, cantidad):
        self.salud = max(0, self.salud - int(cantidad))
        if self.salud == 0:
            print(f"¡{self.nombre} se ha debilitado!")
        else:
            print(f"A {self.nombre} le quedan {self.salud}/{self.salud_maxima} puntos de salud.")

    def mostrar_info(self):
        print("\n--- Información del Pokémon ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self._tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}/{self.salud_maxima}")


class PokemonFuego(Pokemon):
    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Fuego"

    def atacar(self, objetivo):
        if self.salud <= 0 or objetivo.salud <= 0:
            return super().atacar(objetivo)

        dano = self._calcular_dano_base(objetivo)
        if objetivo._tipo == "Planta":
            dano *= 2
            print("¡Es súper efectivo!")
        elif objetivo._tipo == "Agua":
            dano = max(1, dano // 2)
            print("No es muy efectivo...")

        print(f"{self.nombre} ataca a {objetivo.nombre} y causa {dano} puntos de daño.")
        objetivo.recibir_dano(dano)

    def mostrar_info(self):
        super().mostrar_info()
        print("🔥 ¡Arde con pasión!")


class PokemonAgua(Pokemon):
    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Agua"

    def atacar(self, objetivo):
        if self.salud <= 0 or objetivo.salud <= 0:
            return super().atacar(objetivo)

        dano = self._calcular_dano_base(objetivo)
        if objetivo._tipo == "Fuego":
            dano *= 2
            print("¡Es súper efectivo!")
        elif objetivo._tipo == "Planta":
            dano = max(1, dano // 2)
            print("No es muy efectivo...")

        print(f"{self.nombre} ataca a {objetivo.nombre} y causa {dano} puntos de daño.")
        objetivo.recibir_dano(dano)

    def mostrar_info(self):
        super().mostrar_info()
        print("💧 ¡Fluye como el río!")


class PokemonPlanta(Pokemon):
    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Planta"

    def atacar(self, objetivo):
        if self.salud <= 0 or objetivo.salud <= 0:
            return super().atacar(objetivo)

        dano = self._calcular_dano_base(objetivo)
        if objetivo._tipo == "Agua":
            dano *= 2
            print("¡Es súper efectivo!")
        elif objetivo._tipo == "Fuego":
            dano = max(1, dano // 2)
            print("No es muy efectivo...")

        print(f"{self.nombre} ataca a {objetivo.nombre} y causa {dano} puntos de daño.")
        objetivo.recibir_dano(dano)

    def mostrar_info(self):
        super().mostrar_info()
        print("🌿 ¡Crece con fuerza!")
