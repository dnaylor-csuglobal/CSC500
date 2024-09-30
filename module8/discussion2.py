class Cat:
    def __init__(self, noise):
        self.__noise = noise

    def make_noise(self):
        print(self.__noise)


tibbles = Cat("meow")
simber = Cat("pur")


# tibbles.make_noise()
# simber.make_noise()

# Cat.make_noise(tibbles)
# Cat.make_noise(simber)

print(tibbles.__noise)