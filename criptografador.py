global frase_criptografada
def cripto(frase):
    global frase_criptografada
    tradutor = "" 
    for letra in frase:
        if letra in "Aa":tradutor = tradutor + "@"
        elif letra in "Bb":tradutor = tradutor + "#"
        elif letra in "Cc":tradutor = tradutor + "&"
        elif letra in "Dd":tradutor = tradutor + "-"
        elif letra in "Ee":tradutor = tradutor + "("
        elif letra in "Ff":tradutor = tradutor +"$"
        elif letra in "Gg":tradutor = tradutor + "+"
        elif letra in "Hh":tradutor = tradutor + "*"
        elif letra in "Ii":tradutor = tradutor + "!"
        elif letra in "Jj":tradutor = tradutor + "{"
        elif letra in "Kk":tradutor = tradutor + "9"
        elif letra in "Ll":tradutor = tradutor + "^"
        elif letra in "Mm":tradutor = tradutor + "["
        elif letra in "Nn":tradutor = tradutor + "º"
        elif letra in "Oo":tradutor = tradutor + "?"
        elif letra in "Pp":tradutor = tradutor + ";"
        elif letra in "Qq":tradutor = tradutor + "2"
        elif letra in "Rr":tradutor = tradutor + "§"
        elif letra in "Ss":tradutor = tradutor + "ª"
        elif letra in "Tt":tradutor = tradutor + "_"
        elif letra in "Uu":tradutor = tradutor + "%"
        elif letra in "Vv":tradutor = tradutor + "~"
        elif letra in "Ww":tradutor = tradutor + "Ç"
        elif letra in "Xx":tradutor = tradutor + ","
        elif letra in "Yy":tradutor = tradutor + "°"
        elif letra in "Zz":tradutor = tradutor + "|"
        else:
            tradutor = tradutor + letra
    frase_criptografada = tradutor
    print(tradutor)



def descripto(frase):
    global frase_criptografada
    tradutor = "" 
    for letra in frase:
        if letra in "@" :tradutor= tradutor+ "a"
        elif letra in "#":tradutor = tradutor + "b"
        elif letra in "&":tradutor = tradutor + "c"
        elif letra in "-":tradutor = tradutor + "d"
        elif letra in "(":tradutor = tradutor + "e"
        elif letra in "$":tradutor = tradutor +"f"
        elif letra in "+":tradutor = tradutor + "g"
        elif letra in "*":tradutor = tradutor + "h"
        elif letra in "!":tradutor = tradutor + "i"
        elif letra in "{":tradutor = tradutor + "j"
        elif letra in "9":tradutor = tradutor + "k"
        elif letra in "^":tradutor = tradutor + "l"
        elif letra in "[":tradutor = tradutor + "m"
        elif letra in "º":tradutor = tradutor + "n"
        elif letra in "?":tradutor = tradutor + "o"
        elif letra in ";":tradutor = tradutor + "p"
        elif letra in "2":tradutor = tradutor + "q"
        elif letra in "§":tradutor = tradutor + "r"
        elif letra in "ª":tradutor = tradutor + "s"
        elif letra in "_":tradutor = tradutor + "t"
        elif letra in "%":tradutor = tradutor + "u"
        elif letra in "~":tradutor = tradutor + "v"
        elif letra in "ç":tradutor = tradutor + "w"
        elif letra in ",":tradutor = tradutor + "x"
        elif letra in "°":tradutor = tradutor + "y"
        elif letra in "|":tradutor = tradutor + "z"
        else:
            tradutor = tradutor + letra
    print(tradutor)

print("************CRIPTOGRAFE SUA FRASE!!!***************\n")
criptografar =(input("Digite sua frase:"))
cripto(criptografar)
decifrar = (input("Deseja traduzir sua frase?:")) 
if decifrar == "sim":
    descripto(frase_criptografada) 
elif decifrar == "nao" :
    print(f"A Frase não foi decifrada:( ")



# while decifrar != "sair":
#     criptografar =(input("Digite sua frase:"))


#     cripto(criptografar)

#     if decifrar == "sim":
#      decifrar = (input("Deseja traduzir sua frase?:"))

#      descripto(decifrar)
     
# else :
#     criptografar =(input("Digite sua frase:"))
#     cripto(criptografar)
#     print(cripto())
    



    
