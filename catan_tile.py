import catan


class CatanTile:
    def __init__(self, index, resource, value, coordinates):
        self.index = index
        self.resource = resource
        self.value = value
        self.coordinates = coordinates
        self.road_slots = []

    def set_road_slots(self, road_slots):
        self.road_slots = road_slots

    def __str__(self):
        return_val = ''
        return_val += 'Tile Number: {}\n'.format(
            self.index
        )
        return_val += 'Resource: {}\n'.format(
            catan.RESOURCE_NAMES[self.resource]
        )
        return_val += 'Value: {}\n'.format(
            self.value
        )
        coordinate_str = ''
        for i in range(len(self.coordinates)):
            coordinate_str += 'Coordinate {}: {}\n'.format(
                i,
                self.coordinates[i]
            )

        return_val += coordinate_str

        return return_val
