from bingo import Jogo


p = Jogo(80)

joao = p.create_card()
pedro = p.create_card()
joaquim = p.create_card()

ganhador = False
ganhadores = []
rodada = 0

while not ganhador and len(p.available_num):
    rodada += 1
    sorteio = p.sort_num()
    print("Numero sorteado: %d" % sorteio)
    if p.check_sorted_num(sorteio, joao):
        print("Joao tem %d" % sorteio)
        elemento = joao.index(sorteio)
        joao.pop(elemento)
        print("Para Joao faltam: %d" % len(joao))
        if not len(joao):
            ganhador = True
            ganhadores.append("Joao")

    if p.check_sorted_num(sorteio, pedro):
        print("Pedro tem %d" % sorteio)
        elemento = pedro.index(sorteio)
        pedro.pop(elemento)
        print("Para Pedro faltam: %d" % len(pedro))
        if not len(pedro):
            ganhador = True
            ganhadores.append("Pedro")

    if p.check_sorted_num(sorteio, joaquim):
        print("Joaquim tem %d" % sorteio)
        elemento = joaquim.index(sorteio)
        joaquim.pop(elemento)
        print("Para Joaquim faltam: %d" % len(joaquim))
        if not len(joaquim):
            ganhador = True
            ganhadores.append("Joaquim")

print(rodada)
print(ganhadores)
print(p.available_num)
