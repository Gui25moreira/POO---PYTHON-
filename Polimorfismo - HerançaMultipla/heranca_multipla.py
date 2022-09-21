class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class BancoBB(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Nice One')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Santander(Funcionario):
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster: 
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Junior(Santander):
    pass

class Pleno(Santander, BancoBB, Hipster):
    pass



gabriel = Junior('Gabriel')
gabriel.busca_perguntas_sem_resposta()
gabriel.mostrar_tarefas()

guilherme = Pleno('Guilherme')
guilherme.busca_perguntas_sem_resposta()
guilherme.busca_cursos_do_mes()

guilherme.mostrar_tarefas()

print(guilherme)