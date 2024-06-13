class ejercicio:

    def __init__(self, ID, ejercicio, repeticiones, tiempo, peso, fortalece, serie, dificultad) -> None:
        self.ID = ID
        self.ejercicio = ejercicio
        self.repeticiones = repeticiones
        self.tiempo = tiempo
        self.peso = peso
        self.fortalece = fortalece
        self.serie = serie
        self.dificultad = dificultad


    def serialize(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'repeticiones': self.repeticiones,
            'serie': self.serie
        }

    def serialize_details(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'repeticiones': self.repeticiones,
            'tiempo': self.tiempo,
            'peso': self.peso,
            'fortalece': self.fortalece,
            'serie': self.serie,
            'dificultad': self.dificultad
        }

# hola
