#----------> Critpgrafar <----------#
def cifra_de_cesar(texto, deslocamento):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    texto_criptografado = ""

    for char in texto:
        if char in alfabeto:
            pos = alfabeto.find(char)
            pos_criptografada = (pos + deslocamento) % 26
            texto_criptografado += alfabeto[pos_criptografada]
        else:
            texto_criptografado += char

    return texto_criptografado


#----------> DesCritpgrafar <----------#
def descriptografar_cifra_de_cesar(texto_criptografado, deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    texto_descriptografado = ''

    for char in texto_criptografado:
        if char in alfabeto:
            pos_criptografada = alfabeto.find(char)
            pos = (pos_criptografada - deslocamento) % 26
            texto_descriptografado += alfabeto[pos]
        else:
            texto_descriptografado += char

    return texto_descriptografado


#----------> Função Main <----------#
def main ():
    escolha = int(input("Escolha a opção abaixo: \n 1) - Criptografar \n 2) - Descriptografar \n Resposta:"))

    if escolha == 1:
        texto = str(input("Digite o texto a ser criptografado:"))
        deslocamento = int(input("Digite a chave: "))
        texto_criptografado = cifra_de_cesar(texto, deslocamento)
        print(texto_criptografado)

    if escolha == 2:
        texto_criptografado = str(input("Digite o texto a ser Descriptografado:"))
        deslocamento = int(input("Digite a chave: "))
        texto_descriptografado = descriptografar_cifra_de_cesar(texto_criptografado, deslocamento)
        print(texto_descriptografado)
    if escolha != 1 and escolha != 2 :
        print("Opção Invalida:")

while True:
    main()
    reiniciar = input("Deseja reiniciar o programa? (s/n): ")
    if reiniciar.lower() != "s":
        break
