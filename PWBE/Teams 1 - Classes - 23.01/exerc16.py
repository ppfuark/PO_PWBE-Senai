class RedeSocial:
    def __init__(self):
        self.usuarios = {}
        self.posts = {}

    def adicionar_amigo(self, usuario, amigo):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = []
        if amigo not in self.usuarios:
            self.usuarios[amigo] = []
        self.usuarios[usuario].append(amigo)
        print(f"{amigo} foi adicionado como amigo de {usuario}.")

    def publicar_mensagem(self, usuario, mensagem):
        if usuario not in self.posts:
            self.posts[usuario] = []
        self.posts[usuario].append(mensagem)
        print(f"{usuario} publicou: {mensagem}")

    def comentar_post(self, usuario, autor, indice_post, comentario):
        try:
            post = self.posts[autor][indice_post]
            print(f"{usuario} comentou no post de {autor}: {comentario}")
        except IndexError:
            print("Post não encontrado.")

    def buscar_usuario(self, nome):
        if nome in self.usuarios:
            print(f"{nome} encontrado.")
        else:
            print(f"{nome} não encontrado.")
