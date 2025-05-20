# autor
#Dilan Felipe Hernandez Guillen
#NRC 102445 2
from pelicula import Pelicula

if __name__ == "__main__":
    # Crear 3 películas
    peli1 = Pelicula(1001, "Matrix", 136, "Wachowski")
    peli2 = Pelicula(1002, "Inception", 148, "Christopher Nolan")
    peli3 = Pelicula(1001, "Matrix Reloaded", 138, "Wachowski")

    # Mostrar películas
    print(peli1)
    print(peli2)
    print(peli3)

    # Probar prestar y devolver
    print(peli1.prestar())
    print(peli1.prestar())  # Ya estaba prestada
    print(peli1.devolver())
    print(peli1.devolver())  # Ya estaba devuelta

    # Costo de reproducción
    print(peli2.costo_reproduccion(25))  # 25 pesos por minuto

    # Comparar películas
    print("¿peli1 y peli3 tienen el mismo código?", peli1 == peli3)
