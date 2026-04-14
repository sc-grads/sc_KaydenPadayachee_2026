class Connection:
    def __init__(self, connection_type: str, cost: float) -> None:
        print(f'{connection_type} connection established! (Cost: ${cost})')
        self.connection_type = connection_type
        self.cost = cost

    def close_connection(self) -> None:
        print(f'Closing{self.connection_type} connection established!')

def main() -> None:
    internet: Connection = Connection('Internet', 2)
    saterlite: Connection = Connection('Saterlite', 20)

    internet.close_connection()
    saterlite.close_connection()


if __name__ == '__main__':
    main()
