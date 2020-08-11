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
        msg = "{0}#{1}#{2}#{3}|"
        return msg.format(self.local, self.reslocal, self.resvisitante, self.visitante)

    def get_local(self):
        return self.local

    def get_visiting(self):
        return self.visitante

    def get_reslocal(self):
        return self.reslocal

    def get_resvisiting(self):
        return self.resvisitante

class Jornada:
    def __init__(self, num, fecha, partidos):
        self.partidos = partidos
        self.num = num
        self.fecha = fecha

    def toString(self):
        msg = self.num + '*' + self.fecha + '*'
        for p in self.partidos:
            msg += p.toString()
        msg += '\n'
        return msg

    def __str__(self):
        msg = ''
        for p in self.partidos:
            msg += p.__str__()
            msg += '\n'
        return msg

    def get_partidos(self):
        return self.partidos


class Temporada:
    def __init__(self, num, jornadas):
        self.num = num
        self.jornadas = jornadas

    def __str__(self):
        msg = self.num + ": "
        for j in self.jornadas:
            msg += j.__str__()
            msg += '\n'
        return msg

    def toString(self):
        msg = self.num + '\n'
        for j in self.jornadas:
            msg += j.toString()
        return msg

    def get_jornadas(self):
        return self.jornadas
