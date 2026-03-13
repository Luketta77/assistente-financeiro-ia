# 💰 Assistente Financeiro Inteligente com IA

Este projeto apresenta uma experiência digital de relacionamento financeiro guiada por **Inteligência Artificial Generativa**, com foco em **experiência do usuário (UX)** e interações claras e personalizadas.

A solução utiliza **Python** e conceitos de **IA, análise de dados e linguagem natural** para oferecer suporte financeiro básico ao usuário, como:

- respostas para dúvidas financeiras
- simulações de crédito
- explicações de produtos bancários
- interações inteligentes baseadas em contexto

---

# 🎯 Objetivo do Projeto

Criar um assistente digital capaz de ajudar usuários a entender melhor serviços financeiros e tomar decisões informadas por meio de:

- interpretação de linguagem natural
- respostas contextualizadas
- simulações financeiras simples
- experiência amigável ao usuário

---

# 🚀 Funcionalidades

✔ FAQ inteligente sobre produtos financeiros  
✔ Simulação de empréstimos  
✔ Cálculo de juros simples  
✔ Explicação de conceitos financeiros  
✔ Interação via chat em linguagem natural  

---

# 🧠 Tecnologias Utilizadas

- Python
- Inteligência Artificial
- Processamento de Linguagem Natural
- Estrutura de dados
- Conceitos de UX

---

# 📦 Estrutura do Projeto

assistente-financeiro-ia
│

├── main.py

├── simulador_financeiro.py

├── faq_financeiro.py

└── README.md


🧩 Experiência do Usuário (UX)

Para garantir uma boa experiência, o sistema foi projetado com:

linguagem simples

respostas claras

interação orientada por opções

feedback imediato ao usuário

🔒 Segurança e Boas Práticas

O sistema evita:

exposição de dados sensíveis

decisões financeiras automáticas

recomendações sem contexto

O objetivo é educação financeira e simulação.

🚀 Possíveis melhorias

integração com IA generativa real (OpenAI)

interface web com Streamlit

histórico de conversas

análise de perfil financeiro

dashboards de gastos

👨‍💻 Autor

Projeto desenvolvido por Lucas Ferreira como parte da trilha de Inteligência Artificial, Python e Dados da DIO.


---

# 📂 Código principal (main.py)

```python
from simulador_financeiro import simular_emprestimo
from faq_financeiro import responder_pergunta

print("Assistente Financeiro IA")

while True:

    print("\nEscolha uma opção:")
    print("1 - Simular empréstimo")
    print("2 - Fazer pergunta financeira")
    print("3 - Sair")

    opcao = input()

    if opcao == "1":
        valor = float(input("Valor do empréstimo: "))
        taxa = float(input("Taxa de juros (%): "))
        meses = int(input("Meses: "))

        total = simular_emprestimo(valor, taxa, meses)
        print("Total a pagar:", total)

    elif opcao == "2":
        pergunta = input("Digite sua pergunta: ")
        print(responder_pergunta(pergunta))

    elif opcao == "3":
        break
