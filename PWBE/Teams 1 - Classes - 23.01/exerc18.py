import calendar

class Calendario:
    def exibir_calendario(self, ano, mes):
        try:
            print(calendar.month(ano, mes))
        except:
            print("Mês ou ano inválido.")

    def verificar_feriado(self, data):
        feriados = {
            "01-01": "Ano Novo",
            "25-12": "Natal",
        }
        data_formatada = data.strftime("%d-%m")
        if data_formatada in feriados:
            print(f"{data} é feriado: {feriados[data_formatada]}")
        else:
            print(f"{data} não é feriado.")

    def calcular_diferenca(self, data1, data2):
        diferenca = abs((data2 - data1).days)
        print(f"A diferença entre as datas é de {diferenca} dias.")
        
