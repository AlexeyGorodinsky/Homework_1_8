class Animals:

    def __init__(self, n, w, h, nof, fr, fp):
        self.name = str(n)  # название животного
        self.weight = w  # вес
        self.height = h  # рост
        self.number_of_feedings = nof  # количетсво кормлений
        self.feed_rate = fr  # обръем корма за одно кормление
        self.farm_product = str(fp)  # продукт животноводства
        self.feed_volume_per_day = nof * fr
        print('\n Животное:', self.name,
              '\n вес, кг:', self.weight,
              '\n рост(размер) животного, см:', self.height,
              '\n число кормлений в день, ед.:', self.number_of_feedings,
              '\n объем корма за одно кормление, кг:', self.feed_rate,
              '\n дневной объем корма, кг:', self.feed_volume_per_day,
              '\n продукт животноводства:', self.farm_product)


class Cows(Animals):

    def __init__(self, n, w, h, nof, fr, fp, lom):
        Animals.__init__(self, n, w, h, nof, fr, fp)
        self.litre_of_milk = lom
        self.weight_of_meat = w * 0.65
        print(' объем молока (коровьего) в сутки, л:', self.litre_of_milk)
        print(' общий вес мяса после раздела, кг:', self.weight_of_meat)


class Goats(Animals):

    def __init__(self, n, w, h, nof, fr, fp, lom):
        Animals.__init__(self, n, w, h, nof, fr, fp)
        self.litre_of_milk = lom
        self.weight_of_meat = w * 0.65
        print(' объем молока (козьего) в сутки, л:', self.litre_of_milk)
        print(' общий вес мяса после раздела, кг:', round(self.weight_of_meat, 1))


class Pigs(Animals):

    def __init__(self, n, w, h, nof, fr, fp):
        Animals.__init__(self, n, w, h, nof, fr, fp)
        self.weight_of_meat = w*0.7
        print(' общий вес мяса после раздела, кг:', round(self.weight_of_meat, 1))


class Sheeps(Animals):

    def __init__(self, n, w, h, nof, fr, fp):
        Animals.__init__(self, n, w, h, nof, fr, fp)
        self.weight_of_meat = w * 0.5
        self.weight_of_wool = w * 0.1
        print(' общий вес настрига (шерсти), кг:', round(self.weight_of_wool, 1))
        print(' общий вес мяса после раздела, кг:', round(self.weight_of_meat, 1))


cow = Cows('корова', 750, 120, 5, 5, 'молоко коровье, мясо(говядина)', 20)
goat = Goats('коза', 50, 75, 5, 2, 'молоко козье', 2.5)
pig = Pigs('свинья', 100, 75, 5, 5, 'мясо(свинина)')
sheep = Sheeps('овца', 50, 75, 5, 2, 'мясо и шерсть')


class Farm_birds(Animals):

    def __init__(self, n, w, h, nof, fr, fp, noe):
        Animals.__init__(self, n, w, h, nof, fr, fp)
        self.number_of_eggs = noe
        print(' количество яиц (в неделю), шт:', self.number_of_eggs)


class Ducks(Farm_birds):

    def __init__(self, n, w, h, nof, fr, fp, noe):
        Farm_birds.__init__(self, n, w, h, nof, fr, fp, noe)
        self.weight_of_meat = w * 0.5
        self.weight_of_fluff = w * 0.05
        print(' вес мяса после раздела, кг:', round(self.weight_of_meat, 1))
        print(' вес пуха, кг:', round(self.weight_of_fluff, 1))


class Сhickens(Farm_birds):

    def __init__(self, n, w, h, nof, fr, fp, noe):
        Farm_birds.__init__(self, n, w, h, nof, fr, fp, noe)
        self.weight_of_meat = w * 0.6
        self.weight_of_fluff = w * 0.03
        print(' вес мяса после раздела, кг:', round(self.weight_of_meat, 1))
        print(' вес пуха, кг:', round(self.weight_of_fluff, 1))


class Geese(Farm_birds):

    def __init__(self, n, w, h, nof, fr, fp, noe):
        Farm_birds.__init__(self, n, w, h, nof, fr, fp, noe)
        self.weight_of_meat = w * 0.7
        self.weight_of_fluff = w * 0.04
        print(' вес мяса после раздела, кг:', round(self.weight_of_meat, 1))
        print(' вес пуха, кг:', round(self.weight_of_fluff, 1))


duck = Ducks('утка', 3, 30, 4, 2, 'яйца мясо пух', 20)
chicken = Сhickens('курица', 3, 30, 4, 2, 'яйца мясо пух', 30)
goose = Geese('гусь', 3, 30, 4, 2, 'яйца мясо пух', 15)
