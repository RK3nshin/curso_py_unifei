def  main():
    numeros = []
    negativos = []
    while True:
        try:
            num = float(input("Digite um número (negativo para parar): "))
            if num < 0:
                negativos.append(num)  
                break  
            else:
                numeros.append(num) 
        except ValueError:
            print("Por favor, digite um número válido.")

    # a) Soma dos números positivos
    soma_positivos = sum(numeros)
    print(f"Soma dos números positivos: {soma_positivos}")

    # b) Média de todos os números lidos
    total_numeros = numeros + negativos
    media_todos = sum(total_numeros) / len(total_numeros) if total_numeros else 0
    print(f"Média de todos os números lidos: {'%.2f' % media_todos}")

    # c) Número com maior valor
    if total_numeros:
        maior_valor = max(total_numeros)
        print(f"Número com maior valor: {maior_valor}")
    else:
        print("Nenhum número foi lido.")

    # d) Todos os números negativos
    print("Números negativos digitados:", negativos)

if __name__ == "__main__":
    main()