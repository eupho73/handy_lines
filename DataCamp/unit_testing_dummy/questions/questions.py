from transforming.transform import str_of_int_to_list

def concat_list_int():
    """Question about the result of adding two lists together.
    
    :return: wheter or not the answer is correct as a string.
    """
    l1, l2 = [1, 2], [3, 4]
    print(f"Que renvoie {l1} + {l2} ?")
    reponse = input()
    res = str_of_int_to_list(reponse)  # la réponse en tant que liste
    if res == l1 + l2:
        print("Correct !")
    elif res is None: 
        print("Mauvaise réponse, assurez-vous d'utiliser des listes et des integers.")
    else:
        print("Mauvaise réponse.")

