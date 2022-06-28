class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
Sonata = Car("Sonata", 2017)
G80  = Car("G80", 2018)

print(f'자동차 모델 : {Sonata.model}, {G80.model}')
print(f'자동차 연식 : {Sonata.year}, {G80.year}')