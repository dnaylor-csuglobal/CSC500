
class Cat:
    noise = "meow"


tibbles = Cat()
print(f"Tibbles makes a {tibbles.noise} sound")

Cat.noise = "pur"
print(f"Tibbles makes a {tibbles.noise} sound")


tibbles.noise = "pur"




