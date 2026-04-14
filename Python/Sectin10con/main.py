class Car:
    __YEAR: int = 2000

    def __init__(self, brand: str, fuel_type: str) -> None:
        self.__brand = brand
        self.__fuel_type = fuel_type

        self.var: str = 'red'

    def drive(self) -> None:
        print(f'Driving: {self.__brand}')

    def __get_description(self) -> None:
        print(f'{self.__brand}: {self.__fuel_type}')

    def display_colour(self) -> None:
        self.__get_description()
        print(f'{self.__brand} is "{self.var.capitalize()}"')

    class Toyota(Car):

