def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    troca = 0

    menor_quantidade = figurinhas_da_maria if len (figurinhas_da_maria) <= len(figurinhas_do_joao) else figurinhas_do_joao 
    maior_quantidade =  figurinhas_da_maria if len (figurinhas_da_maria) >= len(figurinhas_do_joao) else figurinhas_do_joao 
    
    for indice, numero_de_figurinhas in enumerate(menor_quantidade):
        if not numero_de_figurinhas in maior_quantidade:
            for num in range(indice, len(maior_quantidade)):
                if numero_de_figurinhas != maior_quantidade[num]:
                    aux = maior_quantidade[num]
                    maior_quantidade[num] = numero_de_figurinhas
                    menor_quantidade[indice] = aux
                    troca = troca + 1
                    break
    return troca 



if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
