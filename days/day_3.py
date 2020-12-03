class Biome:
    """Class implementing a biome.
    """
    def __init__(self, map_location, ):
        """Initialize the class with a mapped biome. A mapped biome is a
            2D list.
        """
        self.__mapped_biome = self.__read_map(map_location)
        self.size = (len(self.__mapped_biome[0]), len(self.__mapped_biome))

    def __read_map(self, map_location):
        """Generate a mapped biome reading it from a text file.
        """
        map_input = open(map_location, 'r')
        map_input = map_input.read()
        splitted_input = map_input.split('\n')
        mapped_biome = []
        for line in splitted_input:

            splitted_line = list(line) * len(splitted_input)
            mapped_biome.append(splitted_line)

        return mapped_biome

    def get_tile(self, location):
        """Inspect a biome tile
        """
        x, y = location
        try:
            tile = self.__mapped_biome[y][x]
        except IndexError:
            tile = None
        return tile


class Toboggan:
    """Class implementing a tobbogan
    """
    def __init__(self):
        """Initialize the toboggan with an empty biome dictionary
        """
        self.biome_report = {}

    def __update_location(self, x, y, movement_x, movement_y):
        """Update toboggan location
        """
        updated_x = x + movement_x
        updated_y = y + movement_y
        return (updated_x, updated_y)

    def __update_biome_report(self, tile):
        """Update the dictionary containing iformation about the biome
        """
        if tile in self.biome_report:
            self.biome_report[tile] += 1
        else:
            self.biome_report[tile] = 1

    def place_tobbogan(self, location, mapped_biome):
        """Placing the tobbogan on a location on the mapped_biome
        """
        self.biome_report = {}
        x, y = location
        if mapped_biome.get_tile(location=location) is not None:
            setattr(self, 'current_location', location)
        else:
            print('Aborting slide.')

    def slide(self, movement):
        """Slide the toboggan
        """
        x, y = self.current_location
        movement_x, movement_y = movement
        self.current_location = self.__update_location(
            x,
            y,
            movement_x,
            movement_y
        )

    def inspect_biome(self, mapped_biome):
        """Inspect the biome in the current location
        """
        tile = mapped_biome.get_tile(
            location=self.current_location
        )
        if tile is None:
            return True
        else:
            self.__update_biome_report(tile=tile)
            return False

    def visualize_biome_report(self, entry, mapped_biome):
        """Inspect the report from the biome.
        """
        if entry == -1:
            for tile_type, count in self.biome_report.items():

                print(f'Encountered {count} {tile_type} during slide.')

        elif entry not in self.biome_report:
            print('No such an entry in the biome report.')
        else:
            count = self.biome_report[entry]
            print(f'Encountered {count} {entry} during slide.')

        return self.biome_report


def run_simulation(mapped_biome, toboggan, movement_strategies):
    """Simulate a series of slides.
    """
    simulation_report = {}
    for movement_strategy in movement_strategies:

        toboggan.place_tobbogan(
            location=(0, 0),
            mapped_biome=(mapped_biome)
        )

        end_of_slide = False
        while not end_of_slide:

            toboggan.slide(movement=movement_strategy)
            end_of_slide = toboggan.inspect_biome(mapped_biome=mapped_biome)

        print(f'For movement strategy {movement_strategy} the biome report is')
        print('')
        biome_report = toboggan.visualize_biome_report(
            entry=-1,
            mapped_biome=mapped_biome
        )
        print('')
        for tile_type, count in biome_report.items():

            if tile_type in simulation_report:
                simulation_report[tile_type].append(count)
            else:
                simulation_report[tile_type] = [count]

    return simulation_report


if __name__ == '__main__':

    movement_strategies = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    mapped_biome = Biome(
        map_location='data\\day_3.txt'
    )
    toboggan = Toboggan()

    simulation_report = run_simulation(
        mapped_biome=mapped_biome,
        toboggan=toboggan,
        movement_strategies=movement_strategies
    )
