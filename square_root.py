def sqrt(square):
    for number in range(1, square // 2):  # lister les nombres jusqu'à square
        temporary_square = number * number  # multiplier ce nombre par lui-même
        if temporary_square == square:    # regarder est-ce que le résultat est égal à square
            return number  # Retourner le nombre trouver


# print(sqrt(9))  # == 2


def is_prime(primish):
    """
    Les nombres premiers sont les nombres qui sont divisible
    par 1 ET par eux-même uniquement (1 n'est pas un nombre premier)
    """
    for number in range(2, primish):  # On boucle jusqu'à primish
        if (primish % number) == 0:    # On test si number est divisible par ce nombre
            return False    # On retourne faux si il est divisible par ce nombre

    return True


# print(is_prime(97))


def fibonacci(index) -> int:
    """
    0 1
    0 1 1 2 3 5 8 12
    f(x) = f(x - 1) + f(x - 2)
    La nouvelle valeur vaut la précédente plus la précédénte de la précédente
    """
    # On bloque les premières valeurs de la suite
    # puisque on ne peut pas les calculer
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        # On crée une liste avec comme valeurs initiales 0 et 1
        values = [0, 1]
        for temporary_index in range(2, index):
            # On récupère les 2 valeurs précédentes
            value_1 = values[temporary_index - 1] # Au premier tour -1 == le dernier
            value_2 = values[temporary_index - 2] # Au premier tour -2 == l'avant dernier
            # On stock le résultat de l'addition des 2 à la fin d'une liste
            total = value_1 + value_2
            values.append(total)
        # pop() extrait le dernier élément
        # On renvoie le dernier élément
        return values.pop()


# print(fibonacci(5))  # == 3


def fibonacci2(index) -> int:
    """
    0 1
    0 1 1 2 3 5 8 12
    f(x) = f(x - 1) + f(x - 2)
    La nouvelle valeur vaut la précédente plus la précédénte de la précédente
    """
    # On bloque les premières valeurs de la suite
    # puisque on ne peut pas les calculer
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci2(index - 1) + fibonacci2(index - 2)
        # Quand l'index vaut 2
        # fibonaci2(2 - 1) + fibonacci2(2 - 2)
        # fibonaci2(1) + fibonacci2(0)
        # 1            + 0
        # 1

        # Quand l'index vaut 3
        # fibonaci2(3 - 1) + fibonacci2(3 - 2)
        # fibonaci2(2) + fibonacci2(1)
        # 1            + 1
        # 2


print(fibonacci2(5 - 1))  # == 3 # == fibonacci2(4) + fibonacci2(3)
# [1, 2, 3, 4]
#  0  1  2  3 == numéro de la case - 1
