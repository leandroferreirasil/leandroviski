import base64

class Criptografia:

    def __init__(self, mensagem_original="",mensagem_criptografia=""):
        self.mensagem_original = mensagem_original
        self.mensagem_criptografada = mensagem_criptografada

    def criptografar_mensagem(self):
        mensagem_bytes = self.mensagem_original.encode("ascii")
        base64_bytes = base64.b64encode(mensagem_bytes)
        base64_mensagem = base64_bytes.decode("ascii")
        self.mensagem_criptografada = base64_mensagem
        print(f"Frase criptografada: {base64_mensagem}")

    def descriptografar_mensagem(self):
        Dbase64_bytes = self.mensagem_criptografada.encode("ascii")
        msg_descripto_bytes = base64.b64decode(Dbase64_bytes)
        self.mensagem_descriptografada = msg_descripto_bytes.decode("ascii")
        print(f"Mensagem descript: {self.mensagem_descriptografada}")


if __name__ == '__main__':
    primeira_mensagem = Criptografia("Estudar python com o professor")
    primeira_mensagem.criptografar_mensagem()
    segunda_mensagem = Criptografia ()
    segunda_mensagem.mensagem_original = input("Digite uma mensagem para cifrar:")
    segunda_mensagem.criptografar_mensagem()
    segunda_mensagem.descriptografar_mensagem()