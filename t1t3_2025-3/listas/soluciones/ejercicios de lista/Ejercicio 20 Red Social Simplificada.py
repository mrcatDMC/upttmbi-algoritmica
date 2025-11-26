#Crea un sistema de posts de red social que: agregue posts al inicio, ordene por likes, mantenga solo los últimos 10, y busque posts.
#Sistema completo con clases y múltiples operaciones.
class Post:
    def __init__(self, texto, likes):
        self.texto = texto
        self.likes = likes
    def __repr__(self):
        return f"Post(texto='{self.texto}', likes={self.likes})"
class RedSocial:
    def __init__(self):
        self.posts = []
    def agregar_post(self, texto, likes):
        nuevo_post = Post(texto, likes)
        self.posts.insert(0, nuevo_post)
        if len(self.posts) > 10:
            self.posts.pop()
        print(f"Post agregado: {nuevo_post}")
    def ordenar_por_likes(self):
        self.posts.sort(key=lambda post: post.likes, reverse=True)
        print("Posts ordenados por likes.")
    def mostrar_posts(self):
        if not self.posts:
            print("No hay posts disponibles.")
        else:
            for post in self.posts:
                print(post)
    def buscar_post(self, texto):
        encontrados = [post for post in self.posts if texto in post.texto]
        if encontrados:
            print("Posts encontrados:")
            for post in encontrados:
                print(post)
        else:
            print("No se encontraron posts con ese texto.")
red_social = RedSocial()
while True:
    print("\nRed Social - Menú")
    print("1- Agregar post")
    print("2- Ordenar posts por likes")
    print("3- Mostrar posts")
    print("4- Buscar post por texto")
    print("5- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        texto = input("Ingresa el texto del post: ")
        try:
            likes = int(input("Ingresa la cantidad de likes: "))
            red_social.agregar_post(texto, likes)
        except ValueError:
            print("Por favor, ingresa un número válido para los likes.")
    elif opcion == "2":
        red_social.ordenar_por_likes()
    elif opcion == "3":
        red_social.mostrar_posts()
    elif opcion == "4":
        texto_busqueda = input("Ingresa el texto a buscar en los posts: ")
        red_social.buscar_post(texto_busqueda)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")