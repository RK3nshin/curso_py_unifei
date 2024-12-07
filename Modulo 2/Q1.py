def aplicar_desconto(valor,desconto_percentual):
    return valor * (1-(desconto_percentual /100))


if __name__ == "__main__":
    valor = input("Qual é o valor da conta?")
    desconto_percentual = input("Qual o percentual de desconto deverá ser aplicado?")

    print("O valor final é : ")

    resultado = aplicar_desconto(float(valor),  float(desconto_percentual))

    print(resultado)
