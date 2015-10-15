__author__ = 'Lucas Amaral'

import unittest
import numbers
from bingo import Jogo


class TestJogo(unittest.TestCase):
    # Cenario: A quantidade de elementos possiveis e correta
    def test_num_elements(self):
        # GIVEN: Um numero desejado de elementos
        tamanho = 15

        # WHEN: Geramos o conjunto populado
        j = Jogo(tamanho)

        # THEN: o tamanho desse conjunto gerado e igual ao entrado
        self.assertEqual(tamanho, len(j.available_num))

    # Cenario: O conjunto de elementos nao tem repeticoes
    def test_unique_elements(self):
        # GIVEN: um conjunto de elementos
        p = Jogo(15)
        unique = True

        # WHEN: comparo esses numeros entre si
        for i in range(len(p.available_num)):
            for j in range(len(p.available_num)):
                if i != j and p.available_num[i] == p.available_num[j]:
                    unique = False
        # THEN: Entao esses numeros nunca terao nenhum igual a si
        self.assertTrue(unique, "Os elementos do conjunto nao sao unicos")

    # Cenario: O resultado de um sorteio e um numero inteiro
    def test_sort_elem(self):
        # GIVEN: um conjunto de elementos
        tam = 15
        p = Jogo(tam)

        # WHEN: um elemento é sorteado
        num = p.sort_num()

        #THEN: Esse elemento é um número inteiro
        self.assertTrue(isinstance(num, numbers.Integral))

    # Cenario: Ao Sortear numero, o conjunto restante deve diminuir
    def test_original_set_cardinality(self):
        # GIVEN: um conjunto de elementos de tamanho N
        tam = 40
        p = Jogo(tam)

        # WHEN: um elemento e sorteado
        num = p.sort_num()

        # THEN: O tamanho final sera 1 elemento a menos que o inicial
        self.assertEqual(tam - 1, len(p.available_num))

    # Cenario: Um elemento sorteado nao pode ser sorteado novamente
    def test_sorted_elem_out(self):
        # GIVEN: um conjunto de elementos nao vazio
        tam = 15
        p = Jogo(tam)

        # WHEN: um elemento e sorteado
        num = p.sort_num()

        # THEN: Esse numero sorteado nao pode estar mais no conjunto inicial
        self.assertFalse(num in p.available_num, "O Elemento sorteado parece ainda estar no Conjunto original")

    #Cenario: Um Elemento sorteado deve estar no conjunto de elementos sorteados
    def test_sorted_elem_in(self):
        # GIVEN: Um conjunto de elementos
        tam = 15
        p = Jogo(tam)

        # WHEN: Um elemento e sorteado
        num = p.sort_num()

        # THEN: Este elemento deve constar no conjunto de elementos sorteados
        self.assertTrue(num in p.picked_num, "O Elemento Sorteado nao consta esta no Array de Elementos sorteados")

    #Cenario: Um elemento nunca estara duplicado no conjunto de elementos sorteados
    def test_already_sorted(self):
        # GIVEN: Um conjunto de elementos
        p = Jogo()

        # WHEN: Um elemento e sorteado
        num = p.sort_num()

        # THEN: Esse elemento so ocorre uma vez no conjunto de elementos sorteados
        self.assertEqual(p.picked_num.count(num), 1)


if __name__ == '__main__':
    unittest.main()
