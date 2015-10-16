import random

class Jogo:

    def __init__(self, tam=10):
        self.available_num = []
        self.picked_num = []
        for i in range(0,tam):
            self.available_num.append(i)

    def sort_num(self):
        num = random.randint(0,len(self.available_num)-1)
        self.picked_num.append(self.available_num[num])
        return self.available_num.pop(num)

    def create_card(self):
        card = []
        count = 0
        while count < 9:
            num = random.randint(0,len(self.available_num))
            if num not in card:
                card.append(num)
                count += 1
        return card

    def check_sorted_num(self, sorted, card):
        return sorted in card