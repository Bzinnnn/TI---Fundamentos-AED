# funcionario.py

class Funcionario:
    """representa um funcionario do hotel"""
    
    _contador_codigo = 1
    
    def __init__(self, nome, telefone, cargo, salario, codigo=None):
        if codigo:
            self.codigo = codigo
            if codigo >= Funcionario._contador_codigo:
                Funcionario._contador_codigo = codigo + 1
        else:
            self.codigo = Funcionario._contador_codigo
            Funcionario._contador_codigo += 1
        
        self.nome = nome
        self.telefone = telefone
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return f"Funcionario {self.codigo}: {self.nome} - {self.cargo} - R${self.salario:.2f}"
    
    def __repr__(self):
        return f"<Funcionario {self.codigo}>"
    
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'telefone': self.telefone,
            'cargo': self.cargo,
            'salario': self.salario
        }
    
    @staticmethod
    def from_dict(data):
        return Funcionario(
            nome=data['nome'],
            telefone=data['telefone'],
            cargo=data['cargo'],
            salario=data['salario'],
            codigo=data['codigo']
        )
