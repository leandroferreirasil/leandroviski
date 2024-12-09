def cifra_cesar (texto, chave):
    texto_cifrado = ""

    for caractere in texto:
        if caractere.isalpha():
            #Verifica se o caractere é uma letra e ap.
            if caractere.isupper():
                texto_cifrado += chr((ord(caractere) - 65 + chave) % 26 + 65)
            else:
                texto_cifrado += chr((ord(caractere) - 97 + chave) % 26 + 97)

        else:
            #Mantém caracteres não alfabéticos inalter
            texto_cifrado += caractere

    return texto_cifrado


def decifra_cesar(texto_cifrado, chave):

    return cifra_cesar(texto_cifrado, -chave)


# Exemplo
mensagem = "Criptografia é divertida!"
chave = 3

mensagem_cifrada = cifra_cesar(mensagem, chave )
print("Mensagem Cifrada:", mensagem_cifrada)                               


mensagem_decifrada = decifra_cesar(mensagem_cifrada, chave)
print("Mensagem Decifrada:", mensagem_decifrada)

menu= input("Digite uma palavra ou frase:")






