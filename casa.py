class Descontos_Clientes():
    def __init__(self):

        self.clientes = {
            "123.456.789-00":0.1,
            "846.995.364-57":0.2
        }
    def Desconto(self,cpf):

        if cpf in self.clientes:
            return self.clientes[cpf]
        else:
            return 0.0


sistemas = Descontos_Clientes()

cpf_cliente = input("Digite seu cpf (xxx.xxx.xxx-xx): ")
desconto = sistemas.Desconto(cpf_cliente)

if desconto > 0:
    print(f"Você ganhou um desconto de {desconto*100}%!")
else:
    print('Desculpe, você não tem direito ao desconto.')