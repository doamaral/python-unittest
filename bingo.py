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