import threading
import time

class Knight(threading.Thread):
    """Класс Рыцарь является дочерним от базового класса threading.Thread.
        где: name - имя рыцаря, power - сила рыцаря, enemies - количество врагов"""

    def __init__(self, name:str, power:int, enemies:int=100):
        """Конструктор класса"""
        super().__init__()          # вызываем конструктор базового класса
        self.name = name            # сохраняем локальные переменные экземпляра класса
        self.power = power
        self.enemies = enemies

    def run(self):
        """Метод создает и выполняет созданный поток"""
        print(f'{self.name}, на нас напали!')   # начало выполнения потока
        count_days = 0          # количество дней, в которые рыцарь сражался с врагами
        while self.enemies > 0: # цикл, пока враги не закончились ...
            count_days += 1
            time.sleep(1)       # время задежки 1 сек.
            self.enemies -= self.power
            print(f'{self.name} сражается {count_days}..., осталось {self.enemies} воинов.')

        print(f'{self.name} одержал победу спустя {count_days} дней(дня)!')

if __name__ == '__main__':

    # Создание экземпляров класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    # запускаем потоки на выполнение задачи
    first_knight.start()
    second_knight.start()
