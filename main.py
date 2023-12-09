import random
class Cat_life:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 5
        self.eat = 30
        self.energy = 25
        self.alive = True

    def to_study(self):
        print('Час для навчання команд')
        self.progress += 15
        self.gladness -= 5
        self.eat -= 5
        self.energy -= 20

    def to_sleep(self):
        print('Час для сну')
        self.gladness += 10
        self.eat -= 15
        self.energy += 40

    def to_chill(self):
        print('Час для відпочинку')
        self.progress -= 5
        self.gladness += 15
        self.eat -= 5
        self.energy -= 5

    def to_eat(self):
        print('Час для їжі')
        self.gladness += 10
        self.eat += 35
        self.energy += 15

    def to_go_walk(self):
        print('Час для прогулянки')
        self.gladness += 10
        self.eat += -10
        self.energy += -15

    def is_alive(self):
        if self.progress <= -15:
            print('Йди розвивайся!')
            self.alive = False

        elif self.gladness <= -15:
            print('Упс, в тебе депресія.')
            self.alive = False

        elif self.progress >= 250:
            print('Молодець, ти став найрозумнішим котом світу!')
            self.alive = False

        elif self.eat <= -20:
            print('Ти зголоднів.')
            self.alive = False

        elif self.eat >= 250:
            print('Ти став жирним. Тебе здали в притулок >:(')
            self.alive = False

        elif self.energy <= -20:
            print('У тебе не було енергії щоб гратися. Твої господарі здали тебе в притулок!')
            self.alive = False

        elif self.energy >= 250:
            print('У тебе було забагато енерії. Твої господарі здали тебе в притулок!')
            self.alive = False

    def end_of_the_day(self):
        print(f"Щастя - {self.gladness}")
        print(f"Розум - {round(self.progress,2)}")
        print(f"Їжа - {round(self.eat, 3)}")
        print(f"Енергія - {round(self.energy, 4)}")

    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' life'
        print(f"{day:^50}")
        kubik = random.randint(1, 5)
        if kubik == 1:
            self.to_study()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 2:
            self.to_sleep()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 3:
            self.to_chill()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 4:
            self.to_eat()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 5:
            self.to_go_walk()
            self.end_of_the_day()
            self.is_alive()

nick =Cat_life(name='Patrik')
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
