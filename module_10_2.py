import threading
import  time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self, name, count_enemy = 100):
        counter = 0
        while count_enemy:
            time.sleep(1)
            count_enemy -= self.power
            counter += 1
            print(f'{name}, сражается {counter} день(дня)..., осталось {count_enemy} воинов.')
        print(f'{name} одержал победу спустя {counter} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.name)
        if not (first_knight and second_knight).is_alive():
            print('Все битвы закончились!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()