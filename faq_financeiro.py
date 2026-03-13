def responder_pergunta(pergunta):

    pergunta = pergunta.lower()

    if "cartao" in pergunta:
        return "O cartão de crédito permite compras com pagamento posterior."

    elif "emprestimo" in pergunta:
        return "Empréstimos são valores fornecidos por instituições financeiras que devem ser pagos com juros."

    elif "juros" in pergunta:
        return "Juros são o custo do dinheiro emprestado."

    else:
        return "Desculpe, ainda estou aprendendo sobre esse assunto."
