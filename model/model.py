class Partido:
    def __init__(self, local, visitante, reslocal, resvisitante, jornada):
        self.local = local
        self.visitante = visitante
        self.reslocal = reslocal
        self.resvisitante = resvisitante
        self.jornada = jornada

    def __str__(self):
        msg = "Jornada {0}: {1} {2} - {3} {4}"
        return msg.format(self.jornada, self.local, self.reslocal, self.resvisitante, self.visitante)

    def toString(self):
        msg = "{0} {1} {2} {3} {4} |"
        return msg.format(self.jornada, self.local, self.reslocal, self.resvisitante, self.visitante)
