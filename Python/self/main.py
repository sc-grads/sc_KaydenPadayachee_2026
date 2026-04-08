#Attributes
# class Car:
#     SPEED_LIMIT_KM: float = 140
#
#     def __init__(self, brand: float) -> None:
#         self.brand = brand
#
#     def drive(self, *, speed: float) -> None:
#         if speed > self.SPEED_LIMIT_KM:
#             print(f'Limiter activated: Driving at {self.SPEED_LIMIT_KM} km/h')
#         else:
#             print(f'Driving at {speed}km/h')
#
# def main() -> None:
#     toyota = Car('Toyota')
#     bmw: Car = Car('BMW')
#
#     toyota.drive(speed=200)
#     bmw.drive(speed=210)
#
#     toyota.SPEED_LIMIT_KM = 99
#
#     toyota.drive(speed=200)
#     bmw.drive(speed=210)
#
#
# if __name__ == '__main__':
#     main()

# dangers

class Animal:
    tricks: list[str] = []

    def __init__(self, name) -> None:
        self.name = name

    def teach_trick(self, trick_name: str) -> None:
        self.tricks.append(trick_name)


def main() -> None:
    cat: Animal = Animal("Helios")
    dog: Animal = Animal("Boomer")

    cat.teach_trick("Wash dishes")
    cat.teach_trick("Get a job")
    print(cat.tricks)

    dog.teach_trick('Do finances')
    dog.teach_trick('Invest in stocks')
    print(dog.tricks)
    print(cat.tricks)


if __name__ == "__main__":
    main()