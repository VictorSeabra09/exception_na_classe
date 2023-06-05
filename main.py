

class Controlador:
    __instanciado = False

    def __init__(self, qualquer):
        if not Controlador.__instanciado:
            self.atributo_qualquer = qualquer
            Controlador.__instanciado = True
        else:
            raise Exception()

# TESTANDO

inst_controlador = Controlador('Atributo 1')

print(inst_controlador, inst_controlador.atributo_qualquer)

inst_controlador2 = Controlador('Atributo 2')


print(inst_controlador2, inst_controlador2.atributo_qualquer)
