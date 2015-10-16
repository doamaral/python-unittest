from bingo import Jogo


p = Jogo(80)

sorteio = p.sort_num()
print(sorteio)

joao = p.create_card()
p.check_sorted_num(sorteio, joao)

pedro = p.create_card()
p.check_sorted_num(sorteio, joao)

joaquim = p.create_card()
p.check_sorted_num(sorteio, joao)

print(joao)
print(pedro)
print(joaquim)
