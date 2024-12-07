def obter_peso_ideal(altura,sexo):
   return ((72.7 * altura)-58)  if sexo == 'M' else ((62.1 * altura)-44.7)

def main():
   sexo = input("Digite o sexo da pessoa (F ou M)")
   altura = input("Digite a altura em Metros ")

   print("Peso ideal é (kg) :")
   print("%.2f"% obter_peso_ideal(float(altura),sexo))

if __name__ == "__main__":
    main()