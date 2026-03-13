# 💻 Exemplo de Código Principal

```python
from simulador_financeiro import simular_emprestimo
from faq_financeiro import responder_pergunta

print("💰 Assistente Financeiro IA")
print("Digite sua pergunta ou escolha uma opção:")
print("1 - Simular empréstimo")
print("2 - Pergunta financeira")

opcao = input()

if opcao == "1":
    valor = float(input("Valor do empréstimo: "))
    taxa = float(input("Taxa de juros (%): "))
    meses = int(input("Número de meses: "))

    resultado = simular_emprestimo(valor, taxa, meses)
    print("Valor final a pagar:", resultado)

elif opcao == "2":
    pergunta = input("Digite sua pergunta: ")
    resposta = responder_pergunta(pergunta)
    print(resposta)
